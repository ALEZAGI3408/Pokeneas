import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-por-defecto'
    S3_BUCKET = os.environ.get('pokebucket2.0')
    S3_KEY = os.environ.get('ASIAUOFEB7K7M7353TPZ')
    S3_SECRET = os.environ.get('GAYC0kIA0fa/0gyDAJAxy+cbCg5jkiZISKuunJmg')
    S3_LOCATION = f'https://{S3_BUCKET}.s3.amazonaws.com/'
