import os, boto3, datetime
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

S3 = boto3.client('s3',
    endpoint_url=os.getenv('S3_ENDPOINT','http://localhost:9000'),
    aws_access_key_id=os.getenv('S3_KEY','minio'),
    aws_secret_access_key=os.getenv('S3_SECRET','minio12345'),
    region_name='us-east-1')
BUCKET=os.getenv('S3_BUCKET','files')

app = FastAPI()

@app.get('/presign/upload')
def presign_upload(key: str):
    url = S3.generate_presigned_url('put_object',
        Params={'Bucket': BUCKET, 'Key': key},
        ExpiresIn=3600)
    return {'url': url, 'key': key}

@app.get('/health')
def health(): return {'ok': True}
