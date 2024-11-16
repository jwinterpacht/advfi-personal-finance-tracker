import MainUI

def home_screen_operations(entry):
    selection = int(entry) #can safely cast this because we already validated
    
    match selection:
        case 1:
            MainUI.MainUI.income_management_menu()
        
        case 2:
            MainUI.MainUI.spending_managment_menu()
        
        case 3:
            MainUI.MainUI.asset_management_menu()
        
        case 4:
            MainUI.MainUI.liability_management_menu()
        
        case 5:
            MainUI.MainUI.financial_reports_menu()
        
        case 6:
            MainUI.MainUI.retrieve_transactions()
        
        case 7:
            MainUI.MainUI.alert_center_menu()
        
        case 8:
            MainUI.MainUI.program_settings_menu()
        
        case 9:
            exit(0)