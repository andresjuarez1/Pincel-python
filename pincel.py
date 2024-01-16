import math

import pygame

ancho_pantalla = 800
alto_pantalla = 600
switch_circule = True

ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)

pygame.draw.rect(ventana, color_pantalla, (0, 0, ancho_pantalla, alto_pantalla))

pygame.display.update()

x0, y0, x1, y1, radio = 0, 0, 0, 0, 0
primer_click = False
ventana.fill(color_pantalla)

circle_body = None
circle = None
lines = []

def calcular_radio(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    radio = distancia / 2
    return radio

while True:
    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            x0, y0 = evento.pos
            init_l = (x0, y0)
            final_l = init_l
            primer_click = True
        if evento.type == pygame.MOUSEMOTION:
            if primer_click:
                if switch_circule:
                    x1, y1 = evento.pos
                    radio = calcular_radio(x0, y0, x1, y1)
                    pygame.draw.rect(ventana, color_pantalla, (0, 0, ancho_pantalla, alto_pantalla))
                    pygame.draw.circle(ventana, color_dibujo, (x0, y0), int(radio))
                    pygame.draw.circle(ventana, color_pantalla, (x0, y0), int(radio) - 15)
                else:
                    x1, y1 = evento.pos
                    init_l = final_l
                    final_l = (x1, y1)
                    newLine = pygame.draw.line(ventana, color_dibujo, init_l, final_l)
                    lines.append(newLine)

        if evento.type == pygame.MOUSEBUTTONUP:
            primer_click = False
            switch_circule = not switch_circule
            if switch_circule:
                for line in lines:
                    xl, yl, _, _, = line
                    pygame.draw.rect(ventana, color_pantalla, (0, 0, ancho_pantalla, alto_pantalla))
                    pygame.draw.circle(ventana, color_dibujo, (xl, yl), int(radio))
                    pygame.draw.circle(ventana, color_pantalla, (xl, yl), int(radio) - 15)
                    pygame.display.update()
                    pygame.time.wait(1)
            lines=[]
        pygame.display.update()

        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()