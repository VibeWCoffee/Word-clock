import datetime as dt
import pytz as p
import prettytable as pt

 
class Time():
    
    
    timezone: str = None
    
    def __init__(self, timezone) -> None:
        
        if timezone not in p.all_timezones:
            raise Exception('Timezone that was inputed cannot be accepted')
        elif timezone == None:
            self.menu()
        else:
            self.timezone = timezone

    # Creating a menu 
    def menu(self):
        
        # Menu wil be ran only if tz is not set in config
        
        # Creating a pretty table
        
        # Display pretty table
        
        # Ask for input
        
        # Save input in config
        pass
    
    ### GETTERS && SETTERS ###
    
    # Return time in the format [HR][MIN][SEC][MIL]
    def get_time(self) -> list:
        
        
        return []

    # Return date MM/DD/YYYY
    def get_date(self) -> list:
        return [self.month, self.day]
    
    # Return self.time
    def get_timezone(self) -> str:
        return self.timezone
    
    # Getting the list of timezones and print it in a table
    def get_timezone_list(self) -> list:
        return p.all_timezones
    
    def set_state(self, state: int):
        self.state = state
        































# If you read this you are cringe