from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class Simple(App):
	def build(self):

		b=Button(text="Click")

		return b

if __name__ == '__main__':
	Simple().run()
