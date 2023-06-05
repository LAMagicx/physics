import pygame, sys
import numpy as np
import vector, line

# pygame setup
screen_width, screen_height = 750, 750
FPS = 60
pygame.display.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.DOUBLEBUF)
clock = pygame.time.Clock()

B = 10
r = 1
N = 1
T = 2
dt = 1/T
scl = 1
mouse_x, mouse_y = -1, -1
light_source = vector.init(330, 230)
light_source_dir = vector.init(-1,0.3) * 10000

line_positions = np.array([line.init(0, 0, 0, screen_height),
                           line.init(0, screen_height, screen_width, screen_height),
                           line.init(screen_width, screen_height, screen_width, 0),
                           line.init(screen_width, 0, 0, 0),
                           line.init(0, 0, 100, 700),
                           line.init(200,200,300,300),
                           line.init(500,500,300,600)])

loop = True
while loop:
    for event in pygame.event.get():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                loop = False
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            mouse_click_x, mouse_click_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            mouse_release_x, mouse_release_y = pygame.mouse.get_pos()

    screen.fill((51,51,51))
    light_pos = light_source
    light_dir = (np.array([mouse_x, mouse_y]) - light_pos) * 1000
    lines = [light_pos]
    for b in range(B):
        intersections = []
        for l1 in line_positions:
            p1 = light_pos
            p2 = p1 + light_dir
            l2 = line.init(p1[0], p1[1], p2[0], p2[1])
            intersect, s, t = line.intersect(l1, l2)
            if 0 < s < 1 and 0 < t < 1:
                s1 = line.vector(l1)
                s1n = s1 / vector.norm(s1)
                ut = vector.init(-s1n[1], s1n[0])
                s2 = light_dir
                s3 = s2 - 2 * vector.dot(s2, ut) * ut
                intersections.append([s, t, intersect, s3])
                pygame.draw.circle(screen, (255, 0, 0), intersect, int(s*10))
        if intersections:
            s, t, i, v = min(intersections, key=lambda x:x[0])
            light_pos = i
            light_dir = v
            lines.append(i)


    if len(lines) > 1:
        pygame.draw.lines(screen, (200, 200, 200), False, lines, 1)
    ## draw lines
    for l in line_positions:
        pygame.draw.line(screen, (100, 100, 100), l[0], l[1], 2)
    

    pygame.display.flip()
    clock.tick(FPS)

pygame.display.quit()

