import pygame
import sys
import os
from main import generate_melody_to_file, scale_var, note_var
from scales import scale  # Importa la escala desde tu archivo scales.py

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
width = 800
height = 600

# Definir file_path como una cadena vacía antes de usarla
file_path = ""

# Función para cambiar la escala desde la interfaz gráfica
def change_scale(new_scale):
    global scale_var, file_path  # Agrega file_path a las variables globales
    scale_var = new_scale
    generate_melody_to_file(file_path)  # Regenera la melodía cuando cambia la escala

# Función para cambiar la nota desde la interfaz gráfica
def change_note(new_note):
    global note_var, file_path  # Agrega file_path a las variables globales
    note_var = new_note
    generate_melody_to_file(file_path)  # Regenera la melodía cuando cambia la nota

# Función para generar la melodía y guardarla en un archivo MIDI
def generate_and_save_melody():
    global file_path
    user_desktop = os.path.expanduser("~/Desktop")
    file_path = os.path.join(user_desktop, "melodia.mid")
    generate_melody_to_file(file_path)

# Crear la ventana
screen = pygame.display.set_mode((width, height))

# Título de la ventana
pygame.display.set_caption("App Musica")

# Color
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Color de fondo (negro)
background_color = black

# Texto 1
font = pygame.font.Font(None, 45)
text = font.render("Generador de melodías.", True, green)
text_rect = text.get_rect()
text_rect.center = (width // 2, height // 9)

# Texto 2
text2 = pygame.font.Font(None, 45)
text2_rendered = text2.render("Escala:", True, green)
text2_rect = text2_rendered.get_rect()
text2_rect.center = (width // 2, height // 3)

# Texto 3
text3 = pygame.font.Font(None, 45)
text3_rendered = text3.render("Nota:", True, green)
text3_rect = text3_rendered.get_rect()
text3_rect.center = (width // 2, height // 1.8)

# Variables iniciales para la escala y la nota
scale_var = "Major"
note_var = "c"

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if text2_rect.collidepoint(event.pos):
                # Mostrar una lista de opciones para cambiar la escala
                scale_options = list(scale.keys())
                selected_scale_index = scale_options.index(scale_var)
                selected_scale_index = (selected_scale_index + 1) % len(scale_options)
                new_scale = scale_options[selected_scale_index]
                change_scale(new_scale)
            elif text3_rect.collidepoint(event.pos):
                # Mostrar una lista de opciones para cambiar la nota
                note_options = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
                selected_note_index = note_options.index(note_var)
                selected_note_index = (selected_note_index + 1) % len(note_options)
                new_note = note_options[selected_note_index]
                change_note(new_note)
            elif generate_button.collidepoint(event.pos):
                generate_and_save_melody()

    # Rellenar la pantalla con el color de fondo
    screen.fill(background_color)

    # Dibujar el texto en la pantalla
    screen.blit(text, text_rect)
    screen.blit(text2_rendered, text2_rect)
    screen.blit(text3_rendered, text3_rect)

    # Dibujar la escala actual
    escala_x = width // 2
    escala_y = height // 2.5
    escala_var_rendered = text3.render(scale_var, True, red)
    escala_var_rect = escala_var_rendered.get_rect()
    escala_var_rect.center = (escala_x, escala_y)
    screen.blit(escala_var_rendered, escala_var_rect)

    # Dibujar la nota actual
    nota_x = width // 2
    nota_x_y = height // 1.6
    note_var_rendered = text3.render(note_var, True, red)
    note_var_rect = note_var_rendered.get_rect()
    note_var_rect.center = (nota_x, nota_x_y)
    screen.blit(note_var_rendered, note_var_rect)

    # Dibujar el botón "Generar Melodía"
    boton_x = width // 2
    boton_x_y = height // 1.3  # Ajusta esta posición para mover el botón hacia abajo

    # Calcula el ancho y alto del botón
    boton_ancho = 200
    boton_alto = 50

    # Crea el rectángulo del botón
    generate_button = pygame.Rect(boton_x - boton_ancho / 2, boton_x_y - boton_alto / 1.3, boton_ancho, boton_alto)

    # Dibuja el botón
    pygame.draw.rect(screen, green, generate_button)

    # Calcula el centro del botón para el texto
    generate_text_rect = generate_button.copy()
    generate_text_rect.topleft = (boton_x - boton_ancho / 2, boton_x_y - boton_alto / 2)

    # Define el texto del botón "Generar Melodía"
    font = pygame.font.Font(None, 36)
    generate_text = font.render("Generar Melodía", True, white)

    # Dibuja el texto en el botón
    screen.blit(generate_text, generate_text_rect)

    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()

