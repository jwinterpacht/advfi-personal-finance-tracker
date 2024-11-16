import main

def home_screen_operations(entry):
    selection = int(entry) #can safely cast this because we already validated
    
    match selection:
        case 1:
            main.MainUI.income_management_menu()
        
        case 2:
            main.MainUI.spending_managment_menu()
        
        case 3:
            main.MainUI.asset_management_menu()
        
        case 4:
            main.MainUI.liability_management_menu()
        
        case 5:
            main.MainUI.financial_reports_menu()
        
        case 6:
            main.MainUI.retrieve_transactions()
        
        case 7:
            main.MainUI.alert_center_menu()
        
        case 8:
            main.MainUI.program_settings_menu()
        
        case 9:
            exit(0)