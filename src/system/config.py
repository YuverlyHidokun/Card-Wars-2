import os

def get_asset_path(*path_parts):
    return os.path.join(os.path.dirname(__file__), '..', 'assets', *path_parts)


# Colores y constantes base
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
COLOR_BG = (30, 30, 30)