import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-por-defecto'
    S3_BUCKET = os.environ.get('S3_BUCKET')
