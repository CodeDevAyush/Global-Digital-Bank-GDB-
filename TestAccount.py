from Account import Account


print("==================================================")
print("  GLOBAL DIGITAL BANK - ACCOUNT TEST")
print("==================================================")

# 1. Creating Account
print(">>> 1. Creating Account")

account1 = Account(1001, "John Doe", 25, 1000.0, "Savings")

print("Account created!")
print("Account #", account1.getAccountNumber(), "|",
      account1.getName(), "(" + str(account1.getAge()) + " yrs) |",
      account1.getAccountType(), "| ₹" + str(account1.getBalance()), "|",
      account1.getStatus())


# 2. Deposit Money
print(">>> 2. Deposit Money")

result = account1.deposit(500.0)

if result:
    print("Depositing ₹500.0: SUCCESS")
    print("New balance: ₹" + str(account1.getBalance()))

result = account1.deposit(-100.0)

if result:
    print("Depositing ₹-100.0: SUCCESS")
else:
    print("Depositing ₹-100.0: FAILED (Invalid amount)")


# 3. Withdraw Money
print(">>> 3. Withdraw Money")

result = account1.withdraw(200.0)

if result:
    print("Withdrawing ₹200.0: SUCCESS")
    print("New balance: ₹" + str(account1.getBalance()))

result = account1.withdraw(2000.0)

if result:
    print("Withdrawing ₹2000.0: SUCCESS")
else:
    print("Withdrawing ₹2000.0: FAILED (Insufficient balance)")

print("Current balance: ₹" + str(account1.getBalance()))


# 4. Creating Another Account
print(">>> 4. Creating Another Account")

account2 = Account(1002, "Jane Smith", 30, 2000.0, "Current")

print("Account #", account2.getAccountNumber(), "|",
      account2.getName(), "(" + str(account2.getAge()) + " yrs) |",
      account2.getAccountType(), "| ₹" + str(account2.getBalance()), "|",
      account2.getStatus())


# 5. All Accounts
print(">>> 5. All Accounts")

print("Account #", account1.getAccountNumber(), "|",
      account1.getName(), "(" + str(account1.getAge()) + " yrs) |",
      account1.getAccountType(), "| ₹" + str(account1.getBalance()), "|",
      account1.getStatus())

print("Account #", account2.getAccountNumber(), "|",
      account2.getName(), "(" + str(account2.getAge()) + " yrs) |",
      account2.getAccountType(), "| ₹" + str(account2.getBalance()), "|",
      account2.getStatus())


print("==================================================")
print("  TEST COMPLETED!")
print("==================================================")