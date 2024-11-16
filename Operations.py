import MainUI


def home_screen_operations(entry):
    selection = int(entry)  # can safely cast this because we already validated

    match selection:
        case 1:
            MainUI.income_management_menu()

        case 2:
            MainUI.spending_managment_menu()

        case 3:
            MainUI.asset_management_menu()

        case 4:
            MainUI.liability_management_menu()

        case 5:
            MainUI.financial_reports_menu()

        case 6:
            MainUI.retrieve_transactions()

        case 7:
            MainUI.alert_center_menu()

        case 8:
            MainUI.program_settings_menu()

        case 9:
            exit(0)
