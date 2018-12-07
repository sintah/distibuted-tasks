import boto3
import time
from .aws_config import ACCESS_KEY, DEAD_LETTER_QUEUE_URL, SECURITY_KEY

# To run python -m aws_sqs.dead_letter_consumer
sqs = boto3.client('sqs',
                   region_name='eu-central-1',
                   aws_access_key_id=ACCESS_KEY,
                   aws_secret_access_key=SECURITY_KEY
                   )

if __name__ == "__main__":
    print("Starting worker listening on {}".format(DEAD_LETTER_QUEUE_URL))
    while True:
        response = sqs.receive_message(
            QueueUrl=DEAD_LETTER_QUEUE_URL,
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
            except Exception as e:
                print("Exception in worker > ", e)
            finally:
                sqs.delete_message(QueueUrl=DEAD_LETTER_QUEUE_URL, ReceiptHandle=message.get('ReceiptHandle'))
            time.sleep(1)

print("Stopped dead letter queue")
