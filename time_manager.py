from concurrent.futures import thread
import datetime as dt
import pytz as p
import prettytable as pt
import json
import threading as th
class Time():
    
    
    timezone: str = None
    config_timezone: str = json.load(open('config.json'))["timezone"]
    def __init__(self, timezone=None) -> None:
        
        # Check if json_timezone is available and if timezone is NONE to 
        if timezone is None and self.config_timezone is not None:
            print("Setting timezone from config.json")
            timezone = self.config_timezone
            
        # Checking if timezone is valid
        if timezone not in p.all_timezones:
            # Exception might be temporary could replace with a menu to select timezone
            raise Exception('Cannot accept timezone: ' + str(timezone) + '\n' +
                            'config_timezone: ' + str(self.config_timezone))
        elif timezone in p.all_timezones:
            self.timezone = timezone
            print("timezone is valid")

        
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