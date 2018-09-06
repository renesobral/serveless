import json
import boto3
import zipfile
import StringIO
import mimetypes

from botocore.client import Config

def lambda_handler(event, context):
    objT = AWSMoveProduction()
    objT.run()
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }

class AWSMoveProduction(object):
    def __init__(self):
        pass

    def run(self):
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
        my_git_bucket = s3.Bucket('renesobral.build')
        my_publish =  s3.Bucket('renesobral')
        file_men = StringIO.StringIO()
        my_git_bucket.download_fileobj('mycode.zip', file_men)

        with zipfile.ZipFile(file_men) as myzip:
            for file_name in myzip.namelist():
                print file_name
                file = myzip.open(file_name)
                my_publish.upload_fileobj(file, file_name,
                                          ExtraArgs={'ContentType': mimetypes.guess_type(file_name)[0]})
                my_publish.Object(file_name).Acl().put(ACL='public-read')