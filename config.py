import os
from dotenv import load_dotenv


load_dotenv()


USER_SERVICE_URL = os.getenv('USER_SERVICE_URL')
MONGODB_URI = os.getenv('MONOGDB_URI')
GCS_BUCKET = os.getenv('GCS_BUCKET')

