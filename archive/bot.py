from dotenv import load_dotenv
from flask import Flask, request
from google.cloud import storage
import datetime
import google.auth
import json
import openai
import os
import pathlib

datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
load_dotenv()
open_ai_key = os.getenv("OPENAI_API_KEY")
completion = openai.Completion()

user = '5037547138'
bot_name = 'reggie'



# Class for working with Google Cloud Storage
class GCStorage:
    def __init__(self, storage_client):
        self.client = storage_client

    # Create a bucket
    def create_bucket(self, bucket_name, storage_class, bucket_location='US'):
        bucket = self.client.bucket(bucket_name)
        bucket.storage_class = storage_class
        return self.client.create_bucket(bucket, bucket_location)        

    # Get a bucket
    def get_bucket(self, bucket_name):
        return self.client.get_bucket(bucket_name)

    # List all buckets
    def list_buckets(self):
        buckets = self.client.list_buckets()
        return [bucket.name for bucket in buckets]

    # Upload a file to a bucket
    def upload_file(self, bucket, blob_destination, file_path):
        blob = bucket.blob(blob_destination)
        blob.upload_from_filename(file_path, content_type='application/json')
        return blob

    # List all blobs in a bucket
    def list_blobs(self, bucket_name):
        return self.client.list_blobs(bucket_name)
    
    def download_blob(self, bucket_name, blob_name, file_path):
        bucket = self.client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(file_path)
        return blob
    
    
    def load_file(self, bucket, blob_name):
        bucket = storage_client.get_bucket(bucket)
        blob = bucket.blob(blob_name)
        data = json.loads(blob.download_as_string(client=None))
        return data
    

project_id = 'gpt-pdsbot'
bucket_name = 'gpt_chat_logs'
working_dir = pathlib.Path.cwd()
client = storage.Client(project = project_id )
bucket = client.bucket(bucket_name, project_id)
chat_file_folder = working_dir.joinpath('chat_logs')
file_path = chat_file_folder.joinpath('{}_{}_chat.json'.format(user, bot_name))
file_name = ('{}_{}_chat.json'.format(user, bot_name))
STORAGE_CLASSES = ('STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE')

storage_client = storage.Client(project = project_id )
   
# Initializing the GCP storage class and loading the chat log file
gcs = GCStorage(storage_client)
 

#
# ========================================================
# Called functions that will work correctly

# create_chat_log_file(user, bot_name)
# upload_chat_log_file(bucket_name, file_path)

# data = gcs.load_file(bucket, file_name)
# print(data )

# # =========================================================


# Create a bucket if it doesn't exist and chat log management functions

def get_or_create_bucket(bucket_name):
    if not bucket_name in gcs.list_buckets():
        gcs.create_bucket(bucket_name, STORAGE_CLASSES[0])
    else:
        gcs.get_bucket(bucket_name)
        
        
# Create a new chat log file in the local chat_logs folder
def create_chat_log_file(user, bot_name):
    # TODO This function requires me to manually load the starting json 
    # Opportunity to integrate the startup exeperience while solving this manual operation
    filename = f'{user}_{bot_name}_chat.json'
    file_path = chat_file_folder.joinpath(filename)
    with open(file_path, 'w') as f:
        f.write('')
    return file_path

# upload the chat log file to the bucket
def upload_chat_log_file(bucket_name, file_path):
    name = f'{user}_{bot_name}_chat.json'
    filename = name
    bucket = gcs.get_bucket(bucket_name)
    blob = gcs.upload_file(bucket, filename, file_path)
    return blob




