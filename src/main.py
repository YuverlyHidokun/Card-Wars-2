import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.objects.deck import Deck
from src.objects.player import Player
from src.system.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

pygame.init()

fuente = pygame.font.SysFont(None, 36)

pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cards Wars 2 - Fase 1")
clock = pygame.time.Clock()

# Juego
mazo = Deck()
jugador1 = Player("Jugador 1")
jugador2 = Player("Jugador 2")
jugador1.robar_cartas(mazo)
jugador2.robar_cartas(mazo)

# Asigna las cartas a las posiciones iniciales de la mano
jugador1.colocar_cartas_iniciales(y=400)
jugador2.colocar_cartas_iniciales(y=100)

jugadores = [jugador1, jugador2]
turno_actual = 0
carta_seleccionada = None

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = evento.pos
            for carta in jugadores[turno_actual].mano:
                if carta.rect.collidepoint(pos):
                    carta_seleccionada = carta
                    carta.arrastrando = True
                    carta.offset_x = carta.rect.x - pos[0]
                    carta.offset_y = carta.rect.y - pos[1]

        elif evento.type == pygame.MOUSEBUTTONUP:
            if carta_seleccionada:
                carta_seleccionada.arrastrando = False
                carta_seleccionada = None
                turno_actual = 1 - turno_actual  # Cambia de jugador

    if carta_seleccionada and carta_seleccionada.arrastrando:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        carta_seleccionada.rect.x = mouse_x + carta_seleccionada.offset_x
        carta_seleccionada.rect.y = mouse_y + carta_seleccionada.offset_y

    pantalla.fill((30, 30, 30))

    # Dibuja la mano del jugador actual
    jugadores[turno_actual].draw_mano(pantalla)

    turno_texto = fuente.render(f"Turno de: {jugadores[turno_actual].nombre}", True, (255, 255, 255))
    pantalla.blit(turno_texto, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
