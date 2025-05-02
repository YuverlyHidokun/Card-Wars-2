import pygame

class Card:
    def __init__(self, nombre, elemento, poder, imagen):
        self.nombre = nombre
        self.elemento = elemento
        self.poder = poder
        self.imagen = self.cargar_imagen(imagen)
        self.rect = self.imagen.get_rect()
        self.arrastrando = False

    def cargar_imagen(self, path):
        try:
            imagen = pygame.image.load(path).convert_alpha()
            return imagen
        except:
            # Placeholder gris si no se encuentra imagen
            surf = pygame.Surface((80, 120))  # Tamaño de la carta
            surf.fill((180, 180, 180))
            pygame.draw.rect(surf, (0, 0, 0), surf.get_rect(), 2)
            return surf

    def draw(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)

    def update_position(self, pos):
        self.rect.center = pos
