class Account:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.balance = 0

    def debit(self, amount):
        if self.category in ['Assets', 'Expenses']:
            self.balance += amount
        else:
            self.balance -= amount

    def credit(self, amount):
        if self.category in ['Assets', 'Expenses']:
            self.balance -= amount
        else:
            self.balance += amount

class JournalEntry:
    def __init__(self, date, description):
        self.date = date
        self.description = description
        self.lines = []

    def add_line(self, account, debit=0, credit=0):
        self.lines.append((account, debit, credit))

class DoubleEntryBookkeeping:
    def __init__(self):
        self.accounts = []
        self.journal_entries = []

    def create_account(self, name, category):
        account = Account(name, category)
        self.accounts.append(account)
        return account

    def record_journal_entry(self, journal_entry):
        for account, debit, credit in journal_entry.lines:
            account.debit(debit)
            account.credit(credit)
        self.journal_entries.append(journal_entry)

    def trial_balance(self):
        print("Account Name        Debits   Credits")
        print("-" * 40)
        total_debits = total_credits = 0
        for account in self.accounts:
            debits = credits = 0
            if account.balance > 0:
                if account.category in ['Assets', 'Expenses']:
                    debits = account.balance
                else:
                    credits = account.balance
            elif account.balance < 0:
                if account.category in ['Assets', 'Expenses']:
                    credits = -account.balance
                else:
                    debits = -account.balance
            print(f"{account.name: <20} {debits: >8.2f} {credits: >8.2f}")
            total_debits += debits
            total_credits += credits
        print("-" * 40)
        print(f"{'Total': <20} {total_debits: >8.2f} {total_credits: >8.2f}")

if __name__ == "__main__":
    bookkeeping = DoubleEntryBookkeeping()

    # Create accounts
    cash = bookkeeping.create_account("Cash", "Assets")
    sales_revenue = bookkeeping.create_account("Sales Revenue", "Revenue")
    rent_expense = bookkeeping.create_account("Rent Expense", "Expenses")

    # Record a journal entry for a sale
    sale_entry = JournalEntry("2023-03-01", "Sale of goods")
    sale_entry.add_line(cash, debit=1000)
    sale_entry.add_line(sales_revenue, credit=1000)

    bookkeeping.record_journal_entry(sale_entry)

    # Record a journal entry for rent payment
    rent_entry = JournalEntry("2023-03-02", "Rent payment")
    rent_entry.add_line(cash, credit=500)
    rent_entry.add_line(rent_expense, debit=500)
    bookkeeping.record_journal_entry(rent_entry)

    # Display trial balance
    bookkeeping.trial_balance()
