'''
Alert class
By Jonah Raef
10-17-2024

Alerts are intended to be stored in an array.
Might make the class itself into an array containing objects of itself.
'''

print('Running: Alert.py')

class Alert:
    alertType = ""
    alertDescription = ""
    alertTime = 0.0
    alertFrequency = "daily" #[hourly, daily, weekly, monthly] (subject for more options in the future)
    recur = 0 #boolean: 0 for no; 1 for yes

    '''
    alertType: string
    alertDescription: string
    alertTime: double
    recur: bool
    alertFrequency: string
    '''
    def __init__(self, alertType, alertDescription, alertTime, alertFrequency, recur):
        self.alertType = alertType
        self.alertDescription = alertDescription
        self.alertTime = alertTime
        self.alertFrequency = alertFrequency
        self.recur = recur

    def isRecurring(self):
        return self.alertFrequency is not None


