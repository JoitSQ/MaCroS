
from PIL import Image
import pystray


class BG:
    def __init__(self, class_1):
        from Configparser import Config

        self.ui = class_1
        self.config = Config(class_1)
        self.tray_icon = ''
        self.ui.window.protocol("WM_DELETE_WINDOW", self.tray_minimize)

    def tray_minimize(self):
        self.ui.trayed = True
        self.ui.window.withdraw()
        image = Image.open(str(rf"{self.config.resource_path('Images/icon.png')}"))

        menu = pystray.Menu(
            pystray.MenuItem("Open MaCroS", self.window_show),
            pystray.MenuItem("Quit", self.exit_tray)
        )

        self.tray_icon = pystray.Icon(
            "MaCroS",
            image,
            "MaCroS",
            menu
        )

        self.tray_icon.run()


    def window_show(self, icon):
        icon.stop()
        self.ui.trayed=False
        self.ui.window.after(0, self.ui.window.deiconify)


    def exit_tray(self, icon):
        icon.stop()
        self.ui.window.after(0, self.ui.window.destroy)

