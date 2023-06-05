"""
File containing line and static object classes
"""

import pygame
import vector
import numpy as np


class Line:
    def __init__(self, A, B, r=2, c="#c8c8c8"):
        self.A = np.array(A)
        self.B = np.array(B)
        self.v = self.B - self.A
        self.r = r
        self.color = c

    def get_equation(self):
        if self.v[0] == 0:
            print("cannot give equation of vertical line")
            return None, None
        m = self.v[1] / self.v[0]
        b = self.A[1] - m * self.A[0]
        return m, b

    def projected_point(self, p):
        e1 = self.v
        e2 = p - self.A
        dot_val = vector.dot(e1, e2)
        len2 = e1[0] ** 2 + e1[1] ** 2
        p = self.A + (dot_val * e1) / len2
        return p

    def point_on_line(self, p, e=1e-6):
        cp = (p[1] - self.A[1]) * self.v[0] - (p[0] - self.A[0]) * self.v[1]
        if abs(cp) > e:
            return False
        # dp = vector.dot(p - self.A, self.v)
        dp = (p[0] - self.A[0]) * self.v[0] + (p[1] - self.A[1]) * self.v[1]
        if dp < 0:
            return False
        sl = vector.dist_quick(self.A, self.B)
        if dp > sl:
            return False
        return True

    def bounding_box(self, p, r):
        pass

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.A, self.B, self.r)


class StaticObject:
    def __init__(self, lines):
        self.lines = lines

    def get_intersections(self, obj, e=1e-6):
        intersection_points = []
        for line in self.lines:
            projected_point = line.projected_point(obj.curr_pos)
            if line.point_on_line(projected_point, e=e):
                d = vector.dist(projected_point, obj.curr_pos)
                if d < obj.radius:
                    intersection_points.append([projected_point, d])
        return intersection_points
