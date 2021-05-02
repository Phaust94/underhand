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


class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''

    source = StringProperty(None)
    image_ratio = NumericProperty(None)


class UnderhandApp(App):
    def build(self):
        # the root is created in pictures.kv
        root = self.root

        cur_card = os.path.abspath(
            os.path.join(
                __file__, "..",
                "assets/cards/Card1.png"
            )
        )
        # load the image
        picture = Picture(
            source=cur_card,
            do_rotation=False, do_scale=False,
            do_translation_y=False,
            image_ratio=1,
        )
        # add to the main field
        root.add_widget(picture)
        return None

    def on_pause(self):
        return True


if __name__ == '__main__':
    UnderhandApp().run()
