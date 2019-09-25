import boto3
from botocore.client import Config
import StringIO
import zipfile
import mimetypes

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

site_bucket = s3.Bucket('terrywscrunktv.com')
build_bucket = s3.Bucket('tcrunktvartifacts')

site_zip = StringIO.StringIO()
build_bucket.download_fileobj('terrycrunkartifacts.zip', site_zip)


with zipfile.ZipFile(site_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        site_bucket.upload_fileobj(obj, nm,
            ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
        site_bucket.Object(nm).Acl().put(ACL='public-read')

