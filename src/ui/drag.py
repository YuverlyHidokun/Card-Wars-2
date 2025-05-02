import pygame

carta_seleccionada = None  # Variable global dentro de este módulo

def manejar_drag(evento, jugador_actual):
    global carta_seleccionada

    if evento.type == pygame.MOUSEBUTTONDOWN:
        pos = evento.pos
        for carta in jugador_actual.mano:
            if carta.rect.collidepoint(pos):
                carta_seleccionada = carta
                carta.arrastrando = True
                carta.offset_x = carta.rect.x - pos[0]
                carta.offset_y = carta.rect.y - pos[1]

    elif evento.type == pygame.MOUSEMOTION:
        if carta_seleccionada and carta_seleccionada.arrastrando:
            mouse_x, mouse_y = evento.pos
            carta_seleccionada.rect.x = mouse_x + carta_seleccionada.offset_x
            carta_seleccionada.rect.y = mouse_y + carta_seleccionada.offset_y

    elif evento.type == pygame.MOUSEBUTTONUP:
        if carta_seleccionada:
            carta_seleccionada.arrastrando = False
            carta_seleccionada = None
