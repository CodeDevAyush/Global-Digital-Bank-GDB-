class Account:

    def __init__(self, accountNumber, name, age, initialBalance, accountType):
        
        self.accountNumber = accountNumber
        self.name = name

        # Age should be at least 18
        if age < 18:
            self.age = 18
        else:
            self.age = age

        # Only Savings and Current are allowed
        if accountType == "Savings" or accountType == "Current":
            self.accountType = accountType
        else:
            self.accountType = "Savings"

        # Set minimum balance according to account type
        if self.accountType == "Savings":
            if initialBalance < 500:
                self.balance = 500
            else:
                self.balance = initialBalance
        else:
            if initialBalance < 1000:
                self.balance = 1000
            else:
                self.balance = initialBalance

        self.status = "Active"
        self.pin = None

    def deposit(self, amount):

        if self.status == "Inactive":
            return False

        if amount <= 0:
            return False

        self.balance = self.balance + amount
        return True

    def withdraw(self, amount, pin):

        if self.status == "Inactive":
            return False

        if not self.verifyPin(pin):
            return False

        if amount <= 0:
            return False

        # Check minimum balance
        if self.accountType == "Savings":
            minimumBalance = 500
        else:
            minimumBalance = 1000

        if self.balance - amount < minimumBalance:
            return False

        self.balance = self.balance - amount
        return True

    def closeAccount(self):

        if self.status == "Inactive":
            return False

        self.status = "Inactive"
        return True

    def reopenAccount(self):

        if self.status == "Active":
            return False

        self.status = "Active"
        return True

    def setPin(self, pin):

        if pin >= 1000 and pin <= 9999:
            self.pin = pin
            return True

        return False

    def verifyPin(self, pin):

        if self.pin is not None and self.pin == pin:
            return True

        return False

    def hasPin(self):

        if self.pin is not None:
            return True

        return False

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBalance(self):
        return self.balance

    def getAccountType(self):
        return self.accountType

    def getStatus(self):
        return self.status

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age