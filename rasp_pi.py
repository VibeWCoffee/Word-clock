import time_manager as tm
import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

# Builder.load_file('layout.kv')
class Application(App):
    
    time_manager = None
    application_manager = None
    
    def build(self):
        self.time_manager = tm.Time()
        self.application_manager = Application_Manager()
        return MyLayout(self.time_manager, self.application_manager)

class Application_Manager():
    
    def set_state(self, new_state: int):
        # [0: Time], [1: Date], [2: weather]
        self.state = new_state
        
        if self.state == 0:
            pass
        elif self.state == 1:
            pass
        elif self.state == 2:
            pass 
    
    def get_state(self):
        return self.state
        # Check configs for values
    
class MyLayout(GridLayout):
    
    def __init__(self, time_manager, application_manager, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        
        # Passing in arguments and saving them as class variable 
        self.time_manager = time_manager
        self.application_manager = application_manager
        
        self.cols = 2
        self.add_widget(Label(text="Testing"))
        
    