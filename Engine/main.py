"""
Main script file
imports classes and runs them
"""

import static
import displayer
import verlet_object
import vector
import solver
from threading import Thread, Event

objects = []
n = 20
for _ in range(n):
    p = vector.random(100, 300) + vector.init(200, 0)
    objects.append(verlet_object.Object(p, p, vector.init(0, 0), r=20))

screen_width = displayer.SCREEN_WIDTH
screen_height = displayer.SCREEN_HEIGHT

walls = static.StaticObject(
    [
        static.Line([0, 0], [screen_width, 0]),
        static.Line([screen_width, 0], [screen_width, screen_height]),
        static.Line([0, screen_height], [screen_width, screen_height]),
        static.Line([0, 0], [0, screen_height]),
        static.Line([100, screen_height - 100], [300, screen_height - 300]),
        static.Line(
            [300, screen_height - 350], [screen_width - 50, screen_height - 400]
        ),
    ]
)

stop_event = Event()

update_fps = 30
update_steps = 30
display_fps = 45

engine = solver.Solver(objects, update_fps, steps=update_steps, walls=walls)
update_thread = Thread(target=engine.update, args=(stop_event,))

update_thread.start()

display = displayer.Display(objects + walls.lines, display_fps)
display_thread = Thread(target=display.main, args=(stop_event,))
display_thread.start()
