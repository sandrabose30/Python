import datetime

class BankAccount:

  def __init__(self, username, initial_deposit=0.0):
    self.username = username
    self.balance = initial_deposit
    self.filename = f"{self.username}_ledger.txt"

    self._log(f"Account created with initial deposit:{initial_deposit}")

  def _log(self, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(self.filename, "a") as file:
      file.write(f"[{timestamp}] {message}\n")

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      self._log(f"Deposited: ({amount} | Balance:){self.balance}")
      print(f"Successfully deposited Rs.{amount}.")
    else:
      print("Deposit amount must be greater than zero.")

  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      self._log(f"Withdraw: ({amount} | Balance:){self.balance}")
      print(f"Successfully withdraw Rs.{amount}.")
    elif amount > self.balance:
      print("Error: Insufficient funds!")
    else:
      print("Withdrawal amount must be greater than zero.")

  def check_balance(self):
    print(f"Current Balance for {self.username}: Rs.{self.balance}")
    return self.balance

  def view_transactions(self):
    print(f"\n--- Transaction History for {self.username} ---")
    try:
      with open(self.filename, "r") as file:
        print(file.read())
    except FileNotFoundError:
      print("No transaction history found.")

def main():
  print("Welcome to the Bank System")
  name = input("Enter your username to create an account: ").strip()
  initial = float(input("Enter initial deposit amount: "))

  my_account = BankAccount(name, initial)
  print(f"\nAccount successfully created for {name}!")

  while True:
    print("\n--- Menu ---")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
      amount = float(input("Enter amount to deposit: "))
      my_account.deposit(amount)
    elif choice == "2":
      amount = float(input("Enter amount to withdraw: "))
      my_account.withdraw(amount)
    elif choice == "3":
      my_account.check_balance()
    elif choice == "4":
      my_account.view_transactions()
    elif choice == "5":
      print("Thank you for banking with us. Goodbye!")
      break
    else:
      print("Invalid choice! Please select a number from 1 to 5.")


if __name__ == "__main__":
  main()