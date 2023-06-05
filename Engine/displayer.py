"""
Script contains a class that shows the screen
and houses functions that update it
"""

import pygame

pygame.display.init()

BG_COLOR = (51, 51, 51)
FPS = 20

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()


class Display:
    def __init__(self, objects, fps):
        self.objects = objects
        self.stopped = False
        self.fps = fps

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stopped = True

    def draw_objects(self):
        for obj in self.objects:
            obj.draw(SCREEN)

    def main(self, event):
        self.stopped = False
        while not self.stopped:
            if event.is_set():
                self.stopped = True
            self.handle_events()
            SCREEN.fill(BG_COLOR)
            self.draw_objects()
            pygame.display.update()
            CLOCK.tick(self.fps)
        print("stopping display thread")
        event.set()
        pygame.quit()
