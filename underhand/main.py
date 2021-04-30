from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image


class CurrentCard(Widget):
    pass


class UnderhandApp(App):
    def build(self):
        layout = GridLayout(cols=3, rows=3, row_default_height=40)

        return PongGame()


if __name__ == '__main__':
    UnderhandApp().run()
