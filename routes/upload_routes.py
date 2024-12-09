from flask import Blueprint, request, jsonify
from services.user_service import UserService
from ..utils.alerts import send_storage_alert

def upload_blueprint(gcs_service, mongo_service, user_service_url):
    upload_bp = Blueprint('upload', __name__)

    @upload_bp.route('/upload', methods=['POST'])
    def upload_video():
        token = request.headers.get('Authorization', '').split(' ')[-1]
        user = UserService.validate_token(token, user_service_url)
        if not user:
            return jsonify({"error": "Unauthorized"}), 401

        username = user['username']
        user_storage = mongo_service.find_user_storage(username)
        if not user_storage:
            user_storage = mongo_service.initialize_user_storage(username, 50 * 1024 * 1024)  # 50MB

        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files['file']
        file_size = len(file.read())
        file.seek(0)

        if user_storage['used_storage'] + file_size > user_storage['total_storage']:
            return jsonify({"error": "Upload would exceed storage limit"}), 403

        filename = f"{username}/{file.filename}"
        gcs_service.upload_file(filename, file)

        mongo_service.update_storage(username, {
            '$inc': {'used_storage': file_size},
            '$push': {'files': {'filename': filename, 'size': file_size}}
        })

        storage_percentage = (user_storage['used_storage'] + file_size) / user_storage['total_storage'] * 100
        if storage_percentage >= 80:
            send_storage_alert(username, storage_percentage)

        return jsonify({"message": "File uploaded successfully"}), 200

    return upload_bp
