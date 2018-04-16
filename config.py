import os


class Config(object):
    CONSUMER_KEY = os.getenv("Consumer_key")
    CONSUMER_SECRET = os.getenv("Consumer_secret")
    ACCESS_TOKEN = os.getenv("Access_token")
    ACCESS_TOKEN_SECRET = os.getenv("Access_token_secret")
