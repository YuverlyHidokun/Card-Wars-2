CARDS_WARS_2/
├── assets/
│   ├── fonts/
│   ├── images/
│   │   ├── cartas/
│   │   ├── fondos/
│   │   └── icons/
│   └── sounds/
│
├── src/
│   ├── core/                # Lógica principal
│   │   ├── game.py          # Bucle y fases del juego
│   │   ├── turn_manager.py  # Manejo de turnos
│   │   └── element_logic.py # Reglas entre elementos
│
│   ├── objects/             # Clases base del juego
│   │   ├── card.py
│   │   ├── deck.py
│   │   ├── player.py
│   │   └── board.py
│
│   ├── system/              # Soporte general
│   │   ├── config.py        # Constantes
│   │   ├── input.py         # Controles personalizables
│   │   └── assets.py        # Carga de imágenes/sonidos
│
│   ├── ui/                  # Interfaz y animaciones
│   │   ├── drag.py          # Drag & drop
│   │   ├── menus.py
│   │   └── effects.py       # Animaciones visuales
│
│   └── main.py
│
└── README.md

🧩 Plan de Desarrollo por Fases
🔹 Fase 1: Núcleo del Juego
Cartas (Card) con atributos: nombre, elemento, poder, imagen

Mazo (Deck) y jugador (Player)

Tablero básico (Board)

Turnos y fases simples: robar, jugar

Interfaz inicial + drag & drop funcional

🔹 Fase 2: Estrategia Avanzada
Sistema de elementos:

Fuego > Planta

Planta > Agua

Agua > Fuego

Poder variable

Posicionamiento afecta resultados

Efectos por sinergia o combo de cartas

🔹 Fase 3: Modos de Juego
2 jugadores locales

IA básica para 1 jugador:

Selección de carta por elemento favorable

Interfaz para elegir modo

🔹 Fase 4: Refinamiento
Estados alterados: quemado, congelado, enraizado

Efectos visuales, sonidos y transiciones

Menús: opciones gráficas, controles, dificultad IA

Guardado/carga de configuración

