import boto3
import json
import uuid
from .aws_config import ACCESS_KEY, _QUEUE_URL, SECURITY_KEY

# To run python -m aws_sqs/sqs_invoker.py
sqs = boto3.client('sqs',
                   region_name='eu-central-1',
                   aws_access_key_id=ACCESS_KEY,
                   aws_secret_access_key=SECURITY_KEY
                   )


def send_report_results():
    for i in range(1, 21):
        body = json.dumps({'jobId': 'test01', 'data': {'topping': [
            {'id': '5001', 'type': 'Chery'},
            {'id': '5002', 'type': 'Glazed'},
            {'id': '5005', 'type': 'Sugar'},
            {'id': '5007', 'type': 'Powdered Sugar'},
            {'id': '5006', 'type': 'Chocolate with Sprinkles'},
            {'id': '5003', 'type': 'Chocolate'},
            {'id': '5004', 'type': 'Maple'}]
        }})
    res = sqs.send_message(
        QueueUrl=_QUEUE_URL,
        MessageBody=body
    )
    print(res)
    # Example of answer:
    # {
    #   'MD5OfMessageBody': 'f736a466010b88b62463ef6d7be63eb3',
    #   'MessageId': 'a9c4fb9f-b659-4a81-a20b-3065ea0d444c',
    #   'ResponseMetadata': {
    #       'RequestId': '17bf41ed-8396-5b53-b5a9-156eb319aa1e',
    #       'HTTPStatusCode': 200,
    #       'HTTPHeaders': {
    #           'x-amzn-requestid': '17bf41ed-8396-5b53-b5a9-156eb319aa1e',
    #           'date': 'Thu, 06 Dec 2018 14:12:31 GMT',
    #           'content-type': 'text/xml',
    #           'content-length': '378'
    #          },
    #       'RetryAttempts': 0
    #       }
    #   }

    print('SUCCESS')


send_report_results()
