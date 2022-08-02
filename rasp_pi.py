

class Application():
    
    # State will keep track of weather to display the time, date, or the weather
    state: int = 0
    
    def __init__(self) -> None:
        
        # Check configs for values
        pass
    
    def set_state(self, new_state: int):
       
        # [0: Time], [1: Date], [2: weather]
        self.state = new_state
        match self.state:
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            
    def get_state(self):
        return self.state
    
    