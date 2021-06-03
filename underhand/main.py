import copy, random, kivy, os
kivy.require("2.0.0")

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ReferenceListProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.config import Config
from kivy.clock import Clock
Window.size = (480, 852)
# Config.set('graphics', 'width', '480')
# Config.set('graphics', 'height', '852')
# Config.set('graphics', 'resizable', False)

from cards.cards import CARDS

ASSETS_FOLDER = os.path.abspath(
    os.path.join(
        __file__,
        "..",
        "assets",
    )
)

CARD_SIZE = 0.27

kv = f"""
#:kivy 2.0.0

<BG>:
    size_hint: None, None
    
<UnderhandGame>:
    orientation: 'vertical'
    BG:
        size: self.parent.size

    EventCard:
        size_hint_x: {CARD_SIZE}
        pos_hint: {{"center_x":0.5, "center_y": 0.86}}
        allow_stretch: True
"""

Builder.load_string(kv)


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


X_STEP = 0.33
START = 0.17
DECK_SIZE = 3
CURRENT_DECK = random.sample(CARDS, k=DECK_SIZE)
CURRENT_DECK_SHUFFLE = copy.copy(CURRENT_DECK)
random.shuffle(CURRENT_DECK_SHUFFLE)
CURRENT_CARD = CURRENT_DECK[0]

CURRENT_OPTIONS = {}


class EventCard(Image):

    options_enabled: BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = CURRENT_CARD.picture_path
        self.options_enabled = False

    # noinspection PyMethodMayBeStatic
    def on_options_enabled(self, instance, value):
        print(value)

    def add_text(self, dt, option, cl, option_card):
        print("added text")
        label = Label(
                # pos_hint={"center_y": 0.95,},
                pos_hint={"top": 1, "right": 1.1},
                size_hint=(1, None),
                # pos=(0, 0),
                text=option.name,
                color=(0, 0, 0),
                # text_size=(option_card.texture_size[0], None)
                # pos=(100, 100)
        )

        label.bind(
            width=lambda *x: label.setter('text_size')(
                label, (label.width + 10, None),
                # texture_size=lambda *y: label.setter('height')(label, label.texture_size[1])
            )
        )
        cl.add_widget(label)
        print(option_card.size)
        return False

    def create_child(self, dt, option_card, option):
        cl = RelativeLayout(
            pos=option_card.pos,
            size=option_card.size,
        )
        option_card.add_widget(cl)
        # print("created child")
        if option.is_available:
            Clock.schedule_once(
                lambda dt, option=option, cl=cl, option_card=option_card: self.add_text(
                    dt, option, cl, option_card
                )
            )

        return False

    def on_touch_down(self, *args, **kwargs):
        for i, option in enumerate(CURRENT_CARD.options):
            if not self.options_enabled:
                option_card = OptionCard(
                    size_hint_x=CARD_SIZE,
                    size_hint_y=0.25,
                    pos_hint={"center_x": START + i * X_STEP, "center_y": 0.62},
                    allow_stretch=True,
                    # op_id=i + 1,
                    source=option.picture_path,
                )
                self.parent.add_widget(option_card)

                CURRENT_OPTIONS[f"option_{i + 1}"] = option_card

                Clock.schedule_once(
                        lambda dt, option_card=option_card, option=option: self.create_child(
                            dt, option_card, option)
                )
            else:
                val = CURRENT_OPTIONS[f"option_{i + 1}"]
                self.parent.remove_widget(val)
        self.options_enabled = not self.options_enabled
        return None

    def update(self, *args):
        if not self.parent:
            return None
        print("HERE")
        self.pos = (self.parent.children[0].width / 2, self.parent.height)
        return None


class OptionCard(Image):

    id = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source = kwargs["source"]
        # self.id = f"option_{op_id}"


class BG(Image):
    def __init__(self, **kwargs):
        super(BG, self).__init__(**kwargs)
        self.source = image("background.png")


class UnderhandGame(FloatLayout):
    def __init__(self, **kwargs):
        super(UnderhandGame, self).__init__(**kwargs)


class UnderhandApp(App):
    def build(self):
        return UnderhandGame()

    def on_pause(self):
        return True


if __name__ == '__main__':
    UnderhandApp().run()
