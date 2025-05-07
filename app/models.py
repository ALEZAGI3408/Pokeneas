import random
import socket

class Pokenea:
    def __init__(self, id, nombre, altura, habilidad, imagen, frase):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.habilidad = habilidad
        self.imagen = imagen
        self.frase = frase
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'altura': self.altura,
            'habilidad': self.habilidad,
            'container_id': socket.gethostname()
        }

# Lista de Pokeneas
pokeneas = [
    Pokenea(1, "ElRano", "0.15m", "Lenguetazo Asesino", "Elrano.png", "¡Ribbit!"),
    Pokenea(2, "SanValentin", "1.65m", "Seducción paisa", "SanValentin.jpg", "San valen valen tin valen tin, ¡qué chimba!"),
    Pokenea(3, "ElJuicioso", "1.80m", "Juicio Final", "ElJuicioso.jpg", "Hoy quedamos 3-0 con la ayuda de Dios."),
    Pokenea(4, "Daironman", "1.60m", "Resistencia al licor", "Daironman.jpg", "Un guaro no se le niega a nadie, ni en las buenas ni en las malas."),
    Pokenea(5, "Zarco", "1.75m", "Hurto", "Zarco.jpg", "Como me voy a dejar meter ese ganzo ciego ome."),
    Pokenea(6, "WeedSuarez", "1.68m", "Los plones en la torre", "WeedSuarez.jpg", "Que mas pues mis carelokitos!"),
    Pokenea(7, "NosePai", "1.72m", "Nose pai", "NosePai.jpg", "Nose pai"),
    Pokenea(8, "Toloteli", "1.67m", "Camuflaje Nocturno", "Toloteli.jpg", "Pierde el junior, pierde mi familia porque los enciendo a todos."),
    Pokenea(9, "Tin", "1.73m", "Sacar la lengua", "Tin.jpg", "Este parcero quisque tin"),
    Pokenea(10, "Baiter", "1.78m", "Nutricion", "Baiter.jpg", "Doctor baiter, doctor baiter.")
]

def get_random_pokenea():
    return random.choice(pokeneas)
