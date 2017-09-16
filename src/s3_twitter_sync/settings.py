from os import environ


TWITTER_CONSUMER_KEY = environ.get('TWITTER_CONSUMER_KEY', '')
TWITTER_SECRET = environ.get('TWITTER_SECRET', '')
TWITTER_ACCESS_TOKEN = environ.get('TWITTER_ACCESS_TOKEN', '')
TWITTER_ACCESS_TOKEN_SECRET = environ.get('TWITTER_ACCESS_TOKEN_SECRET', '')
TWITTER_USERNAME = environ.get('TWITTER_USERNAME', '')

AWS_S3_BUCKET_NAME = environ.get('AWS_S3_BUCKET_NAME', '')
AWS_S3_TWITTER_PATH = environ.get('AWS_S3_TWITTER_PATH', '')