'''
AlertManager class
By Jonah Raef
10-17-2024
'''

import Alert #import works if Alert.py in local directory

class AlertManager:
    alertsList = [] #list contaiing a list of Alert objects

    def addAlert(self, type, description, time, frequency, recur):
        self.alertType = type
        self.alertDescription = description
        self.alertTime = time
        self.alertFrequency = frequency
        self.alertsList.append(Alert(type, description, time, frequency, recur))

    def removeAlert(self, alert):
        self.alertsList.remove(alert)

    def modifyAlert(self, alert):
        print('What aspect of this alert would you like to modify?')
        print('1. Type\n2. Description\n3. Time\n4. Frequency\n5. Recurrance')
        user_input = input("")

        match user_input:
            case "1":
                new_type = input("Enter the new type: ")
                alert.alert_type = new_type
            case "2":
                new_description = input("Enter the new description: ")
                alert.alert_description = new_description
            case "3":
                try:
                    new_time = float(input("Enter the new time (e.g., 15.5 for 3:30 PM): "))
                    alert.alert_time = new_time
                except ValueError:
                    print("Invalid time format. Please enter a number.")
            case "4":
                new_frequency = input("Enter the new frequency (e.g., daily, weekly): ")
                alert.alert_frequency = new_frequency
            case "5":
                # Assuming recurrence is toggled on/off
                if alert.isRecurring():
                    alert.alert_frequency = None
                    print("Recurrence turned off.")
                else:
                    new_frequency = input("Enter the recurrence frequency (e.g., daily, weekly): ")
                    alert.alert_frequency = new_frequency
                    print("Recurrence turned on.")
            case _:
                print("Invalid input.")