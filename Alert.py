'''
Alert class
By Jonah Raef
10-17-2024

Alerts are intended to be stored in an array.
Might make the class itself into an array containing objects of itself.
'''

import datetime
from enum import Enum

#11-5: updated to add alertType enum

class alertType(Enum):
    ALARM = 1
    NOTIFICATION = 2
    SILENT_NOTIFICATION = 3


class Alert:
    alertType = ""
    alertDescription = ""
    alertTime = 0.0
    alertFrequency = "daily" #[hourly, daily, weekly, monthly] (subject for more options in the future)
    recur = 0 #boolean: 0 for no; 1 for yes

    '''
    alertType: string
    alertDescription: string
    alertTime: datetime
    recur: bool
    alertFrequency: string
    '''
    def __init__(self, alertType, alertDescription, alertTime: datetime, alertFrequency, recur):
        self.alertType = alertType
        self.alertDescription = alertDescription
        self.alertTime = alertTime
        self.alertFrequency = alertFrequency
        self.recur = recur

    def isRecurring(self):
        return self.alertFrequency is not None
    
    def setTime(self):
        time_str = input("Enter time in the following format: HH:MM")
        try:
            the_time = datetime.datetime.strptime(time_str, "%H:%M").time()
            self.alertTime = the_time
        except ValueError:
            print("Invalid time format. Must use HH:MM")


