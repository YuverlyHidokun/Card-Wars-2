import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_asset_path(*partes):
    return os.path.join(BASE_DIR, 'assets', *partes)

# Colores y constantes base
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
