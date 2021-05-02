import kivy
kivy.require("2.0.0")

import os

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '852')
# Config.set('graphics', 'resizable', False)

ASSETS_FOLDER = os.path.abspath(
    os.path.join(
        __file__,
        "..",
        "assets",
    )
)


def image(path: str) -> str:
    return os.path.join(ASSETS_FOLDER, path)


class Picture(Scatter):
    """
    Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    """

    source = StringProperty(None)
    image_ratio = NumericProperty(None)


class CurrentCard(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self.update)
        self.bind(size=self.update)
        self.update()

    def update(self):
        if not self.parent:
            return None
        self.pos = (self.parent.width / 2, self.parent.height)
        return None


class UnderhandApp(App):
    def build(self):
        # the root is created in pictures.kv
        root = self.root

        cur_card = image(
            "cards/Card1.png",
        )

        bg = Image(
                source=image("background.png"),
                # pos=(0, 100)
        )

        root.add_widget(bg)
        layout = RelativeLayout()
        bg.add_widget(layout)
        # load the image
        picture = CurrentCard(
            source=cur_card,
            keep_ratio=True,
            pos=(layout.width / 2, layout.top)
        )
        layout.add_widget(picture)
        return None

    def on_pause(self):
        return True


if __name__ == '__main__':
    UnderhandApp().run()
