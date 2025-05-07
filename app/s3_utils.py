import boto3
from flask import current_app
from botocore.exceptions import ClientError
import logging
import os

def get_s3_client():
    """
    Crea un cliente S3 usando credenciales del entorno
    """
    try:
        # Usar credenciales explícitas si están disponibles
        if all(key in os.environ for key in ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY']):
            return boto3.client(
                's3',
                aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
                aws_session_token=os.environ.get('AWS_SESSION_TOKEN')
            )
        
        # Usar credenciales del entorno o del rol de instancia EC2
        return boto3.client('s3')
    except Exception as e:
        print(f"Error al crear cliente S3: {str(e)}")
        return None

def get_image_url(image_name):
    """
    Genera la URL para acceder a una imagen en S3
    """
    bucket_name = os.environ.get('S3_BUCKET')
    if not bucket_name:
        print("Variable de entorno S3_BUCKET no configurada")
        return None
    
    # Método 1: Construir la URL directamente (más simple y confiable)
    # Este método funciona si el bucket tiene acceso público
    return f"https://{bucket_name}.s3.amazonaws.com/{image_name}"
    
    # Método 2: Generar una URL prefirmada (si necesitas control de acceso)
    # try:
    #     s3_client = get_s3_client()
    #     if not s3_client:
    #         return None
    #     
    #     url = s3_client.generate_presigned_url(
    #         'get_object',
    #         Params={'Bucket': bucket_name, 'Key': image_name},
    #         ExpiresIn=3600  # URL válida por 1 hora
    #     )
    #     return url
    # except Exception as e:
    #     print(f"Error al generar URL prefirmada: {str(e)}")
    #     return None

def list_bucket_objects(bucket_name):
    """
    Lista todos los objetos en un bucket
    """
    try:
        s3_client = get_s3_client()
        if not s3_client:
            return []
            
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        return response.get('Contents', [])
    except ClientError as e:
        print(f"Error al listar objetos del bucket: {str(e)}")
        return []
