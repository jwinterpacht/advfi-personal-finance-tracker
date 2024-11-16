"""
Idea for this class:
When you are in MainUI getting user input, you will always be able to just call the corresponding validator by doing
Validator.validate_class_name_entry(entry)
and it will return true if input is valid and false if not
High Cohesion
Low Coupling


"""

#used to check if a string is an integer
#internal private method to help prevent code reuse
def _validate_integer(entry: str) -> bool:
    try:
        int(entry)
        return True
    except:
        print("Please be sure to enter an integer")
        return False

#another private method to check if the input integer is a valid selection
def _validate_selection_range(entry: str, low_end: int, high_end: int) -> bool:
    selection = int(entry)
    if selection > high_end or selection < low_end:
        print("Please enter an integer between {} and {}".format(low_end, high_end))
        return False
    return True


#
def validate_home_screen_entry(entry: str) -> bool:
    low_end = 1
    high_end = 9
    
    if(not _validate_integer(entry)):
        return False
    
    return _validate_selection_range(entry, low_end, high_end)


def validate_income_management_menu_entry(entry: str) -> bool:
    low_end = 0
    high_end = 3

    if not _validate_integer(entry):
        return False
    
    return _validate_selection_range(entry, low_end, high_end)

