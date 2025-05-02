import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# main.py
from src.core.game import iniciar_juego


if __name__ == "__main__":
    iniciar_juego()