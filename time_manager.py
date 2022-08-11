
from datetime import datetime as dt
import pytz
import prettytable as pt
import json
class Time():
    
    
    timezone: str = None
    config_timezone: str = json.load(open('config.json'))["timezone"]
    
    # Checks validity of the timezone on initialization
    def __init__(self, timezone=None) -> None:
        
        # Check if json_timezone is available and if timezone is NONE to 
        if timezone is None and self.config_timezone is not None:
            print("Setting timezone from config.json")
            timezone = self.config_timezone
              
        # Checking if timezone is valid
        if timezone not in pytz.all_timezones:
            # Exception might be temporary could replace with a menu to select timezone
            raise Exception('Cannot accept timezone: ' + str(timezone) + '\n' +
                            'config_timezone: ' + str(self.config_timezone))
        elif timezone in pytz.all_timezones:
            self.timezone = timezone
            print("timezone is valid")

    ### GETTERS && SETTERS ###
    
    # Return time in the format [HR][MIN][SEC][MIL]
    def get_time(self) -> str:
        return str(dt.now(pytz.timezone(self.timezone)))

    # Return the date
    # Return date MM/DD/YYYY
    def get_date(self) -> list:
        pass
    
    # Return self.time
    def get_timezone(self) -> str:
        return self.timezone
    
    # Getting the list of timezones and print it in a table
    def get_timezone_list(self) -> list:
        return pytz.all_timezones
    
        

class Weather():
    pass





























# If you read this you are cringe