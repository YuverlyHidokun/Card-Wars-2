import pygame
from src.objects.player import Player
from src.objects.deck import Deck
from src.ui.drag import manejar_drag
from src.system.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def iniciar_juego():
    pygame.init()

    pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Cards Wars 2 - Fase 1")
    clock = pygame.time.Clock()

    # Crear mazo y jugadores
    mazo = Deck()
    jugador1 = Player("Jugador 1")
    jugador2 = Player("Jugador 2")
    jugador1.robar_cartas(mazo)
    jugador2.robar_cartas(mazo)

    # Colocar cartas iniciales
    jugador1.colocar_cartas_iniciales(y=400)
    jugador2.colocar_cartas_iniciales(y=100)

    jugadores = [jugador1, jugador2]
    turno_actual = 0
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            # Llamamos al manejador de drag-and-drop
            manejar_drag(evento, jugadores[turno_actual])

            if evento.type == pygame.MOUSEBUTTONUP:
                turno_actual = 1 - turno_actual  # Cambia de jugador

        pantalla.fill((30, 30, 30))  # Fondo

        # Dibuja la mano del jugador actual
        jugadores[turno_actual].draw_mano(pantalla)

        # Muestra el texto de turno
        turno_texto = pygame.font.SysFont(None, 36).render(f"Turno de: {jugadores[turno_actual].nombre}", True, (255, 255, 255))
        pantalla.blit(turno_texto, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
