import pygame
import sys

# Inicialización del juego
pygame.init()

# Definir el tamaño de la ventana
ancho = 1280
alto = 720
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Menú de inicio")

# Definir colores
azul = (0, 0, 255)
blanco = (255, 255, 255)
celeste = (176, 224, 230)

# Definir fuentes
fuente_grande = pygame.font.Font(None, 50)
fuente_pequena = pygame.font.Font(None, 30)

# Crear botón
boton_ancho = 270
boton_alto = 50
iniciar_partida_rect = pygame.Rect(ancho // 2 - boton_ancho // 2, alto // 2 - 50, boton_ancho, boton_alto)
salir_rect = pygame.Rect(ancho // 2 - boton_ancho // 2, alto // 2 + 50, boton_ancho, boton_alto)

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if iniciar_partida_rect.collidepoint(evento.pos):
                print("Iniciar Partida")
            elif salir_rect.collidepoint(evento.pos):
                print("Salir")
                pygame.quit()
                sys.exit()

    # Rellenar la ventana con color azul
    ventana.fill(azul)

    # Dibujar los botones
    pygame.draw.rect(ventana, blanco, iniciar_partida_rect)
    iniciar_partida_texto = fuente_grande.render("Iniciar Partida", True, azul)
    ventana.blit(iniciar_partida_texto, (iniciar_partida_rect.x + 20, iniciar_partida_rect.y + 10))

    pygame.draw.rect(ventana, blanco, salir_rect)
    salir_texto = fuente_grande.render("Salir", True, azul)
    ventana.blit(salir_texto, (salir_rect.x + 70, salir_rect.y + 10))

    # Actualizar la ventana
    pygame.display.update()