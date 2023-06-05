"""
Solver file that contains the calculations for the engine
"""
import vector
import time
import numpy as np

G = np.array([0.0, 1.0])


class Solver:
    # global parameters go here
    def __init__(self, objects, fps, steps, walls=None):
        self.objects = objects
        self.dt = 1 / steps
        self.fps = fps
        self.steps = steps
        self.walls = walls

    def update(self, event):
        while True:
            if event.is_set():
                break
            start_time = time.time()
            for i in range(self.steps):
                for obj in self.objects:
                    obj.update_acceleration(obj.calculate_resistance())
                self.wall_collide()
                self.solve_collisions()
                self.update_positions()
            time_spent = time.time() - start_time
            if 1 / self.fps - time_spent > 0:
                time.sleep(1 / self.fps - time_spent)
        print("stopping update thread")

    def update_positions(self):
        for obj in self.objects:
            obj.update_position(self.dt)

    def wall_collide(self):
        for obj in self.objects:
            intersection_points = self.walls.get_intersections(obj)
            if len(intersection_points) > 0:
                for p, dist in intersection_points:
                    n = vector.normalise(p - obj.curr_pos)
                    delta = (obj.radius - dist) * 2
                    obj.curr_pos = obj.curr_pos - n * delta
                    # obj.prev_pos = obj.curr_pos

    def solve_collisions(self):
        for i in range(len(self.objects)):
            obj1 = self.objects[i]
            for j in range(i + 1, len(self.objects)):
                obj2 = self.objects[j]
                collision_axis = obj1.curr_pos - obj2.curr_pos
                dist = vector.norm(collision_axis)
                if 0 < dist < obj1.radius + obj2.radius:
                    n = collision_axis / dist
                    delta = obj1.radius + obj2.radius - dist
                    obj1.curr_pos += 0.5 * delta * n
                    obj2.curr_pos -= 0.5 * delta * n
