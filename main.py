import os

os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

from kivy.app import App
from kivy.uix.label import Label


class MinhaApp(App):

    def build(self):
        return Label(text="Olá, Kivy!")


MinhaApp().run()