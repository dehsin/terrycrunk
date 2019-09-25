import boto3
from botocore.client import Config
import zipfile

def lambda_handler(event, context):
    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
    
    site_bucket = s3.Bucket('terrywscrunktv.com')
    build_bucket = s3.Bucket('tcrunktvartifacts')
    
    
    build_bucket.download_file('terrycrunkartifacts.zip', '/tmp/terrycrunkartifacts.zip')
    
    
    with zipfile.ZipFile('/tmp/terrycrunkartifacts.zip') as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            site_bucket.upload_fileobj(obj, nm)
            site_bucket.Object(nm).Acl().put(ACL='public-read')

    return 'done'

