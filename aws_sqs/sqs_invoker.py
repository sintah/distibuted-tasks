import boto3
from .config import ACCESS_KEY, _QUEUE_URL, SECURITY_KEY


sqs = boto3.client('sqs',
                   region_name='eu-central-1',
                   aws_acces_key_id=ACCESS_KEY,
                   aws_secret_access=SECURITY_KEY
                   )