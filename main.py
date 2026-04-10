import sys

class InsufficientFundsError(Exception):
    pass

class InvalidPinError(Exception):
    pass

class AtmAccount:
    def __init__(self, accountHolder, pin, initialBalance):
        self.__accountHolder = accountHolder
        self.__pin = pin
        self.__balance = initialBalance
        self.__transactionHistory = []

    def checkPin(self, inputPin):
        if self.__pin != inputPin:
            raise InvalidPinError("Incorrect PIN entered.")
        return True

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactionHistory.append(f"Deposited: Rs {amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientFundsError("You do not have enough balance.")
        if amount <= 0:
            return False
        self.__balance -= amount
        self.__transactionHistory.append(f"Withdrew: Rs {amount}")
        return True

    def showHistory(self):
        if not self.__transactionHistory:
            print("No transactions yet.")
        for item in self.__transactionHistory:
            print(item)

def startAtm():
    userAccount = AtmAccount("Shreyanth", "1234", 5000)
    
    print("--- Welcome to the Student Bank ATM ---")
    
    try:
        entryPin = input("Enter your 4-digit PIN: ")
        userAccount.checkPin(entryPin)
    except InvalidPinError as e:
        print(e)
        return

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            print(f"Current Balance: Rs {userAccount.getBalance()}")
        
        elif choice == "2":
            try:
                amt = float(input("Enter deposit amount: "))
                if userAccount.deposit(amt):
                    print("Deposit successful.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            try:
                amt = float(input("Enter withdrawal amount: "))
                userAccount.withdraw(amt)
                print("Please collect your cash.")
            except InsufficientFundsError as e:
                print(e)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            print("--- History ---")
            userAccount.showHistory()

        elif choice == "5":
            print("Thank you for using our ATM. Goodbye!")
            sys.exit()
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    startAtm()