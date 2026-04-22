import boto3
import os

s3 = boto3.client('s3')

def proxy_handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))


    # get the name of the bucket from the environment variable
    bucket = os.environ('BUCKET_BUCKET_NAME')

    #Fetch the file 
    response = s3.get_object(Bucket=bucket, Key='index.html')
    html_boday = response['Body'].read().decode('utf-8')


    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html_boday
    }

