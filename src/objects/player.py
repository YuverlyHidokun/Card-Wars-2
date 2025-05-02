class Player:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def robar_cartas(self, deck, cantidad=3):
        for _ in range(cantidad):
            carta = deck.robar()
            if carta:
                self.mano.append(carta)

    def draw_mano(self, pantalla):
        for carta in self.mano:
            carta.draw(pantalla)


    def colocar_cartas_iniciales(self, y=400):
        espacio = 100
        for idx, carta in enumerate(self.mano):
            carta.rect.topleft = (50 + idx * espacio, y)
