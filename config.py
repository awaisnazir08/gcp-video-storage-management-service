import os

USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://user-management-service:5000')
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
GCS_BUCKET = os.getenv('GCS_BUCKET', 'streaming_video_storage_bucket')
