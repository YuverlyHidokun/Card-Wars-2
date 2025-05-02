import random
import os
from .card import Card
from src.system.config import get_asset_path

class Deck:
    def __init__(self):
        self.cartas = []
        self.generar_cartas()
        random.shuffle(self.cartas)

    def generar_cartas(self):
        elementos = ['fuego', 'agua', 'planta']
        for elemento in elementos:
            for i in range(1, 6):
                nombre = f"{elemento}_{i}"
                poder = random.randint(1, 10)
                imagen = get_asset_path("images", "cartas", elemento, f"{i}.png")
                self.cartas.append(Card(nombre, elemento, poder, imagen))

    def robar(self):
        return self.cartas.pop() if self.cartas else None
