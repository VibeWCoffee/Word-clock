import time_manager as tm
import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


class Application(App):
    
    time_manager = None
    application_manager = None
    
    def build(self):
        self.time_manager = tm.Time()
        self.application_manager = Application_Manager()
        return MyLayout(self.time_manager, self.application_manager)

class Application_Manager():
    # Setting the default state
    state = 0
    
    def set_state(self, new_state: int):
        # [0: Time], [1: Date], [2: weather]
        self.state = new_state
        
    def get_state(self):
        return self.state

    
class MyLayout(GridLayout):
    
    time_manager = None
    time_text = None
    application_manager = None
    
    def __init__(self, time_manager, application_manager, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        
        # Passing in arguments and saving them as class variable 
        self.time_manager = time_manager
        self.application_manager = application_manager
        
        self.cols = 2
        self.time_text = Label(text=self.collect_label())
        self.add_widget(self.time_text)
        
        Clock.schedule_interval(lambda dt: self.label_update(), 1)

    def collect_label(self) -> str:
        
        if  self.application_manager.get_state() == 0:
            return "Time is " + self.time_manager.get_time()
            
        elif self.application_manager.get_state() == 1:
            return "The weather is "
        elif self.application_manager.get_state() == 2:
            return "The date is "
    
    def label_update(self) -> None:
        self.time_text.text = self.collect_label()

    
    