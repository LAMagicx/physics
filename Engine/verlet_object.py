"""
Contains an Verlet Object class
"""

## import modules
import numpy as np
import pygame
from vector import norm, normalise

FG_COLOR = (200, 200, 200)


class Object:
    def __init__(self, curr_pos, prev_pos, acc, r=10, color="#c8c8c8"):
        self.curr_pos = curr_pos
        self.prev_pos = prev_pos
        self.acc = acc
        self.radius = r
        self.color = color

    def update_position(self, dt):
        """updates the objects position based on verlet system"""
        vel = self.curr_pos - self.prev_pos
        self.prev_pos = self.curr_pos
        self.curr_pos = self.curr_pos + vel + self.acc * dt * dt
        self.acc = np.zeros(shape=(len(self.acc),)).astype(float)

    def update_acceleration(self, acc):
        """adds a new force to the acc"""
        self.acc += acc

    def calculate_resistance(self):
        vel = self.curr_pos - self.prev_pos
        p = 5
        air_resistance = p / 2 * norm(vel) ** 2 * normalise(vel)
        return -air_resistance

    def draw(self, SCREEN):
        pygame.draw.circle(SCREEN, self.color, self.curr_pos.astype(int), self.radius)
