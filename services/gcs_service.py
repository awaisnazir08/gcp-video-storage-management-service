from google.cloud import storage
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
    r'D:\5th Semester\Cloud Computing\Project\storage-management-service\first-scout-444113-h2-72968e1f4f18.json')
class GCSService:
    def __init__(self, bucket_name):
        self.client = storage.Client(project='first-scout-444113-h2', credentials=credentials)
        self.bucket = self.client.bucket(bucket_name)

    def upload_file(self, filename, file):
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file)

    def delete_file(self, filename):
        blob = self.bucket.blob(filename)
        blob.delete()
