class Player:
    CARDS_IN_HAND = 5  # Definir una constante para la cantidad de cartas iniciales

    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def robar_cartas(self, deck, cantidad=CARDS_IN_HAND):
        """Robar cartas del mazo y añadirlas a la mano del jugador."""
        for _ in range(cantidad):
            carta = deck.robar()
            if carta:
                self.mano.append(carta)

    def draw_mano(self, pantalla):
        """Dibuja las cartas en la pantalla"""
        for carta in self.mano:
            carta.draw(pantalla)

    def colocar_cartas_iniciales(self, y=400):
        """Coloca las cartas en posiciones iniciales sobre la pantalla."""
        espacio = 100
        for idx, carta in enumerate(self.mano):
            carta.rect.topleft = (50 + idx * espacio, y)

