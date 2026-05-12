from UInit import UI
import time


class Anim():

    def __init__(self):
        global counter
        self.namespace = 'Anim'
        counter = 1

    def fade(self, window):
        global counter
        # Check if alpha counter is above zero
        while counter > 0:
            # If is - destroy shit
            UI.text.destroy()
            UI.error.destroy()

            # Sleeping for this to be slower than instant
            time.sleep(.03)
            # ...and lower opacity counter
            counter -= 0.05
            # Update window's opacity
            window.attributes('-alpha', counter)
            # If counter reaches zero meaning the window is completely opaque
        if counter <= 0:
            # Make UI appear
            UI.bFrame1.pack(side='left', anchor='nw', padx=5, pady=5)
            UI.glass.pack(padx=30, pady=30, fill="both", expand=True)
            # Start fading the window back
            UI.mainmenuinit()
            self.fadeback(window)

    def fadeback(self, window):
        global counter
        while counter < 1:
            time.sleep(.03)
            counter += 0.05
            window.attributes('-alpha', counter)
