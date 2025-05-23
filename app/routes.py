from flask import Blueprint, jsonify, render_template
from app.models import get_random_pokenea
from app.s3_utils import get_image_url
import socket
import os

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/pokenea', methods=['GET'])
def get_pokenea_json():
    pokenea = get_random_pokenea()
    return jsonify(pokenea.to_dict())

@main_bp.route('/', methods=['GET'])
def show_pokenea():
    pokenea = get_random_pokenea()
    image_url = get_image_url(pokenea.imagen)
    
    # Si no se pudo generar la URL, usar una imagen de placeholder
    if not image_url:
        image_url = f"https://via.placeholder.com/300x200?text={pokenea.nombre}"
    
    container_id = socket.gethostname()
    return render_template('pokenea.html', 
                          pokenea=pokenea, 
                          image_url=image_url, 
                          container_id=container_id)
