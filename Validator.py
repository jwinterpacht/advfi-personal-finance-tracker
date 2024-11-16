"""
Idea for this class:
When you are in MainUI getting user input, you will always be able to just call the corresponding validator by doing
Validator.validate_class_name_entry(entry)
and it will return true if input is valid and false if not
High Cohesion
Low Coupling


"""





def validate_home_screen_entry(entry: str):
    try:
        selection = int(entry)
        print(selection)
        return True
    except:
        print("Please be sure to enter a number")
        return False


