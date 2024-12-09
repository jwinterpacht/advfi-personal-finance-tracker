from datetime import date
from typing import List, Dict
import TransactionList
import MainUI

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class SpendingReport:
    def __init__(self, transaction_list: TransactionList):
        super().__init__()
        self._total_spending_last_month = 0.0
        self._expense_entries_last_month = []
        for expense in transaction_list._expense_transactions:
            if expense.get_is_within_last_month():
                self._expense_entries_last_month.append(expense)
                self._total_spending_last_month += expense.get_amount()
        self._total_spending = transaction_list.get_total_expenses()

    # Getters
    def get_expense_entries_last_month(self):
        return self._expense_entries_last_month

    def get_total_spending(self):
        return self._total_spending
    
    def get_total_spending_last_month(self):
        return self._total_spending_last_month


    # Setters
    def set_expense_entries_last_month(self, expense_entries_last_month: List[float]):
        self._expense_entries_last_month = expense_entries_last_month
        self._total_spending = sum(self.income_entries_last_month)

    def set_total_spending(self, total_spending: float):
        self._total_spending = total_spending
    
    def set_total_spending_last_month(self, total_spending_last_month: float):
        self._total_spending_last_month = total_spending_last_month

    def generate_report(self):
        spending_report = f"Spending Report\n-----------------\nTotal lifetime spending: ${self._total_spending}\n\nTotal spending from last month: ${self._total_spending_last_month}\n\nEach spending entry from last month:\n"
        for expense in self._expense_entries_last_month:
            spending_report += f"{expense.print_transaction()}\n"
        MainUI.MainUI.utility_print(spending_report)

    def to_string(self) -> str:
        spending_report = f"Spending Report\nTotal lifetime spending: ${self._total_spending}\n\nTotal spending from last month: ${self._total_spending_last_month}\n\nEach spending entry from last month:\n"
        for expense in self._expense_entries_last_month:
            spending_report += f"{expense.print_transaction()}\n"
        return spending_report

    # We can use validate_file_name to validate input 
    def generate_pdf_report(self, filename: str, transaction_list: TransactionList):
        # Create a canvas object for the PDF
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter  # 8.5 x 11 inches

        # Title of the report
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, height - 40, "Spending Report")
        
        # Subtitle with date
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 60, f"Generated on: {date.now().strftime('%B %d, %Y')}")

        # Total spending
        c.drawString(100, height - 100, f"Total lifetime spending: ${self._total_spending:.2f}")
        c.drawString(100, height - 120, f"Total spending from last month: ${self._total_spending_last_month:.2f}")

        # Each spending entry
        y_position = height - 160
        c.drawString(100, y_position, "Each spending entry from last month:")

        y_position -= 20  # Adjusting for the next line
        c.setFont("Helvetica", 10)
        for expense in self._expense_entries_last_month:
            if y_position < 40:  # If we're near the bottom, start a new page
                c.showPage()
                c.setFont("Helvetica", 10)
                y_position = height - 40  # Reset y_position for the new page
            c.drawString(100, y_position, expense.print_transaction(transaction_list))
            y_position -= 15  # Move down for the next entry

        # Save the PDF to the file
        c.save()
        print(f"PDF report saved as {filename}")