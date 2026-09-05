from AccountEnhanced import Account


print("============================================================")
print("ENHANCED ACCOUNT TEST (BOOLEAN RETURNS)")
print("============================================================")


# Test 1: Valid Account Creation
print(">>> Test 1: Valid Account Creation")

account1 = Account(1001, "John Doe", 25, 1000.0, "Savings")

pinStatus = "Yes" if account1.hasPin() else "No"

print("Account #", account1.getAccountNumber(), "|",
      account1.getName(), "(" + str(account1.getAge()) + " yrs) |",
      account1.getAccountType(), "| ₹" + str(account1.getBalance()), "|",
      account1.getStatus(), "| PIN:", pinStatus)


# Test 2: Invalid Age
print(">>> Test 2: Invalid Age (under 18)")

print("Creating account with age 16")

account2 = Account(1002, "Young Kid", 16, 300.0, "Savings")

print("Age auto-corrected to:", account2.getAge())

pinStatus = "Yes" if account2.hasPin() else "No"

print("Account #", account2.getAccountNumber(), "|",
      account2.getName(), "(" + str(account2.getAge()) + " yrs) |",
      account2.getAccountType(), "| ₹" + str(account2.getBalance()), "|",
      account2.getStatus(), "| PIN:", pinStatus)


# Test 3: Invalid Account Type
print(">>> Test 3: Invalid Account Type")

print('Creating account with type "Invalid"')

account3 = Account(1003, "Test User", 25, 300.0, "Invalid")

print("Account type defaulted to:", account3.getAccountType())

pinStatus = "Yes" if account3.hasPin() else "No"

print("Account #", account3.getAccountNumber(), "|",
      account3.getName(), "(" + str(account3.getAge()) + " yrs) |",
      account3.getAccountType(), "| ₹" + str(account3.getBalance()), "|",
      account3.getStatus(), "| PIN:", pinStatus)


# Test 4: Minimum Balance on Creation
print(">>> Test 4: Minimum Balance Enforcement on Creation")

print("Creating Savings account with ₹300 (below minimum)")

account4 = Account(1004, "Bob Wilson", 25, 300.0, "Savings")

print("Balance auto-corrected to minimum: ₹" + str(account4.getBalance()))

pinStatus = "Yes" if account4.hasPin() else "No"

print("Account #", account4.getAccountNumber(), "|",
      account4.getName(), "(" + str(account4.getAge()) + " yrs) |",
      account4.getAccountType(), "| ₹" + str(account4.getBalance()), "|",
      account4.getStatus(), "| PIN:", pinStatus)


# Test 5: Withdrawal with Minimum Balance
print(">>> Test 5: Withdrawal with Minimum Balance")

# Current account needs at least ₹1000
account5 = Account(1005, "Alice Brown", 30, 1200.0, "Current")

account5.setPin(1234)

pinStatus = "Yes" if account5.hasPin() else "No"

print("Initial: Account #", account5.getAccountNumber(), "|",
      account5.getName(), "(" + str(account5.getAge()) + " yrs) |",
      account5.getAccountType(), "| ₹" + str(account5.getBalance()), "|",
      account5.getStatus(), "| PIN:", pinStatus)

result = account5.withdraw(200.0, 1234)

if result:
    print("Withdrawing ₹200.0: SUCCESS")
    print("New balance: ₹" + str(account5.getBalance()))
else:
    print("Withdrawing ₹200.0: FAILED")

print("After withdrawal: Account #", account5.getAccountNumber(), "|",
      account5.getName(), "(" + str(account5.getAge()) + " yrs) |",
      account5.getAccountType(), "| ₹" + str(account5.getBalance()), "|",
      account5.getStatus(), "| PIN:", pinStatus)

result = account5.withdraw(900.0, 1234)

if result:
    print("Withdrawing ₹900.0: SUCCESS")
else:
    print("Withdrawing ₹900.0: FAILED (Minimum balance violation)")

print("Current balance: ₹" + str(account5.getBalance()))


# Test 6: Account Status Management
print(">>> Test 6: Account Status Management")

account6 = Account(1006, "Charlie Green", 35, 2000.0, "Savings")

pinStatus = "Yes" if account6.hasPin() else "No"

print("Initial: Account #", account6.getAccountNumber(), "|",
      account6.getName(), "(" + str(account6.getAge()) + " yrs) |",
      account6.getAccountType(), "| ₹" + str(account6.getBalance()), "|",
      account6.getStatus(), "| PIN:", pinStatus)

result = account6.closeAccount()

if result:
    print("Closing account: SUCCESS")
else:
    print("Closing account: FAILED")

print("After close: Account #", account6.getAccountNumber(), "|",
      account6.getName(), "(" + str(account6.getAge()) + " yrs) |",
      account6.getAccountType(), "| ₹" + str(account6.getBalance()), "|",
      account6.getStatus(), "| PIN:", pinStatus)


result = account6.deposit(500.0)

if result:
    print("Depositing ₹500.0 to closed account: SUCCESS")
else:
    print("Depositing ₹500.0 to closed account: FAILED (Account inactive)")


result = account6.reopenAccount()

if result:
    print("Reopening account: SUCCESS")
else:
    print("Reopening account: FAILED")

print("After reopen: Account #", account6.getAccountNumber(), "|",
      account6.getName(), "(" + str(account6.getAge()) + " yrs) |",
      account6.getAccountType(), "| ₹" + str(account6.getBalance()), "|",
      account6.getStatus(), "| PIN:", pinStatus)


# Test 7: PIN Protection
print(">>> Test 7: PIN Protection")

account7 = Account(1007, "Diana Prince", 28, 1500.0, "Savings")

result = account7.setPin(1234)

if result:
    print("Setting PIN 1234: SUCCESS")
else:
    print("Setting PIN 1234: FAILED")

result = account7.withdraw(200.0, 1234)

if result:
    print("Withdrawing ₹200.0 with correct PIN (1234): SUCCESS")
    print("New balance: ₹" + str(account7.getBalance()))
else:
    print("Withdrawing ₹200.0 with correct PIN (1234): FAILED")


result = account7.withdraw(100.0, 9999)

if result:
    print("Withdrawing ₹100.0 with incorrect PIN (9999): SUCCESS")
else:
    print("Withdrawing ₹100.0 with incorrect PIN (9999): FAILED (Incorrect PIN)")


account8 = Account(1008, "No Pin User", 25, 1500.0, "Savings")

result = account8.withdraw(100.0, 1234)

if result:
    print("Withdrawing ₹100.0 with PIN not set: SUCCESS")
else:
    print("Withdrawing ₹100.0 with PIN not set: FAILED (PIN not set)")


# Test 8: All Accounts Summary
print(">>> Test 8: All Accounts Summary")

accounts = [
    account1,
    account2,
    account3,
    account4,
    account5,
    account6,
    account7
]

for account in accounts:

    pinStatus = "Yes" if account.hasPin() else "No"

    print("Account #", account.getAccountNumber(), "|",
          account.getName(), "(" + str(account.getAge()) + " yrs) |",
          account.getAccountType(), "| ₹" + str(account.getBalance()), "|",
          account.getStatus(), "| PIN:", pinStatus)


print("============================================================")
print("ENHANCED TEST COMPLETED!")
print("============================================================")