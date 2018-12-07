import boto3
import json
from .aws_config import ACCESS_KEY, QUEUE_URL, SECURITY_KEY

# To run python -m aws_sqs.consumer
sqs = boto3.client('sqs',
                   region_name='eu-central-1',
                   aws_access_key_id=ACCESS_KEY,
                   aws_secret_access_key=SECURITY_KEY
                   )

if __name__ == "__main__":
    print("Starting worker listening on {}".format(QUEUE_URL))
    while True:
        response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            AttributeNames=['All'],
            MessageAttributeNames=[
                'string',
            ],
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,
        )
        messages = response.get('Messages', [])
        for message in messages:
            try:
                print("Message Body > ", message.get('Body'))
                body = json.loads(message.get('Body'))
                if not body.get('jobId', None):
                    print("Job Id is not provided")
                else:
                    job_id = body['jobId']
                    print("Running Job Id {}".format(job_id))
                print('Received and deleted message: {}'.format(message))
                sqs.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=message.get('ReceiptHandle'))
            except Exception as e:
                print("Exception in worker > ", e)
                # Do nothing, so AWS SQS will move the dead letter to dead letter queue
print("Stopped consumer")
