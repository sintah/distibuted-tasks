import base64
from random import choice
from string import ascii_letters, digits

from .aws_config import QUEUE_URL, ACCESS_KEY, SECURITY_KEY
from .sqs_client_ext import SQSClientExtended

# To run: python -m aws_sqs.bulk_message
if __name__ == "__main__":

    sqs = SQSClientExtended(aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECURITY_KEY,
                            aws_region_name='eu-central-1',
                            s3_bucket_name='tiptapcode-sqs-data')

    _100mb_large_string = ''.join([choice(ascii_letters + digits) for i in range(100)]) #104857600

    # message = "_100mb_large_string"

    message = _100mb_large_string

    sqs.send_message(QUEUE_URL, message)

    res = sqs.receive_message(QUEUE_URL)

    for message in res:
        sqs.delete_message(QUEUE_URL, message.get('ReceiptHandle'))
