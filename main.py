from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivmob import KivMob ,TestIds
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import *
from kivy.uix.textinput import TextInput
import random
from nltk import word_tokenize

import plyer
import time
class myfuck(GridLayout):
    def __init__(self,**kwargs):
        super(myfuck, self).__init__(**kwargs)
        Window.size=(300,500)
        Window.clearcolor=(1,1,1,1)
        



        with self.canvas.before :
            Rectangle(source='font.png',pos=(0,0),size=(300,502))
        self.b=Button(text='next',pos=(200,60),size_hint=(None,None),size=(70,30),background_color=(1,0,1,1))
        self.b.bind(on_press=self.red)
        self.add_widget(self.b)


    def red(self,instance):
        i=0
        for i in range(0,13):
            p='1.png'
            with self.canvas.before :
                Rectangle(source=p,pos=(0,0),size=(300,502))
        









            

class TestApp(App):

    def build(self):
        return myfuck()

if __name__ == '__main__':
    TestApp().run()
