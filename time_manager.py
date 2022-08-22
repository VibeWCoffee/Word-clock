
from datetime import datetime as dt
import pytz
import json
class Time():
    
    
    timezone: str = None
    config_timezone: str = json.load(open('config.json'))["timezone"]
    
    # Checks validity of the timezone on initialization
    def __init__(self, timezone=None) -> None:
       
        # Timezone validity check
        if timezone in pytz.all_timezones:
            self.timezone = timezone
        elif self.config_timezone in pytz.all_timezones:
            self.timezone = self.config_timezone
        else:
            raise Exception('Incorrect timezone')
    
            
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