from google.cloud import storage

class GCSService:
    def __init__(self, bucket_name):
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)

    def upload_file(self, filename, file):
        blob = self.bucket.blob(filename)
        blob.upload_from_file(file)

    def delete_file(self, filename):
        blob = self.bucket.blob(filename)
        blob.delete()
