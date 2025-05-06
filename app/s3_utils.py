import boto3
from flask import current_app
from botocore.exceptions import ClientError
import logging
from config import Config

def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=Config.S3_KEY,
        aws_secret_access_key=Config.S3_SECRET
    )

def get_image_url(image_name):
    """
    Genera la URL para acceder a una imagen en S3
    """
    return f"{Config.S3_LOCATION}{image_name}"

def upload_file_to_s3(file, bucket_name, acl="public-read"):
    """
    Función para subir un archivo a S3
    """
    try:
        s3_client = get_s3_client()
        s3_client.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True
