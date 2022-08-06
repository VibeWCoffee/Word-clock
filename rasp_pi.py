import time_manager as tm

class Application():
    
    # State will keep track of weather to display the time, date, or the weather
    state: int = 0
    time_manager = None
    
    def __init__(self) -> None:
        self.time_manager = tm.Time()
        # Check configs for values
        pass
    
    def set_state(self, new_state: int):
       
        # [0: Time], [1: Date], [2: weather]
        self.state = new_state
        match self.state:
            case 0:
                print("Displaying the Time")
            case 1:
                print("Displaying the Date")
            case 2:
                print("Displaying the Weather")
            
    def get_state(self):
        return self.state
    
    