from UInit import UI
import time
import threading

ui = UI()
class Anim():
    counter = 1

    def __init__(self):
        global counter
        self.namespace = 'Anim'

    def fade(self, window):
        time.sleep(2)
        global counter
        # Check if alpha counter is above zero
        while Anim.counter > 0:
            # print('disoper')
            # Sleeping for this to be slower than instant
            time.sleep(.03)
            # ...and lower opacity counter
            Anim.counter -= 0.05
            # Update window's opacity
            window.attributes('-alpha', Anim.counter)
            # If counter reaches zero meaning the window is completely opaque

        while Anim.counter < 1:
            # print('oper')
            time.sleep(.03)
            Anim.counter += 0.05
            window.attributes('-alpha', Anim.counter)
        # print('dan')
