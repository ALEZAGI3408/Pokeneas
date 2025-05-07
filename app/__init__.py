from flask import Flask
from app.config import Config
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    logger.debug("Aplicación Flask inicializada")
    return app
