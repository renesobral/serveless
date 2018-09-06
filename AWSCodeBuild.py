import json
import boto3
import zipfile
import StringIO
import mimetypes

from botocore.client import Config

def lambda_handler(event, context):
    objT = AWSMoveProduction()
    try:
        objT.run(event)
    except:
        objT.publish("Error on deployment:")
        raise


    objT.publish("Sucess deployed")
    job = event.get('CodePipeline.job')

    if job:
        codepipeline = boto3.client('codepipeline')
        codepipeline.put_job_success_result(jobId=job["id"])

    return {
        "statusCode": 200,
        "body": json.dumps('Hello from Lambda!')
    }

class AWSMoveProduction(object):
    def __init__(self):
        pass

    def publish(self, message):
        sns = boto3.resource('sns')
        topic = sns.Topic('arn:aws:sns:us-east-1:572667294264:DeployBuild')
        topic.publish(Subject='Build Finshed', Message=message)

    def run(self, event):

        job = event.get('CodePipeline.job')
        location = { "bucketName": 'renesobral.build', "objectKey": "mycode.zip"}

        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3Location"]

        print "Building from: " + str(location)
        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
        my_git_bucket = s3.Bucket(location["bucketName"])
        my_publish =  s3.Bucket('renesobral')
        file_men = StringIO.StringIO()
        my_git_bucket.download_fileobj(location["objectKey"], file_men)

        with zipfile.ZipFile(file_men) as myzip:
            for file_name in myzip.namelist():
                print file_name
                file = myzip.open(file_name)
                my_publish.upload_fileobj(file, file_name,
                                          ExtraArgs={'ContentType': mimetypes.guess_type(file_name)[0]})
                my_publish.Object(file_name).Acl().put(ACL='public-read')
