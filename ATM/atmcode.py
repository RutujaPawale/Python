def balanceInquiry():
    global balance
    print("Your current balance is:",balance,"\n \n")
    repeat()

def cashDeposit():
    global balance
    dep_amt=int(input("Enter the amount you want to deposit:"))
    balance=balance+dep_amt
    print("Cash deposited successfully!! \n")
    balanceInquiry()
    repeat()

def cashWithdraw():
    global balance
    with_amt=int(input("Enter the amount you want to withdraw:"))
    if with_amt>balance:
        print("Insufficient balance!!\n")
    else:
        balance =balance-with_amt
        print(with_amt,"withdrawn successfully!!\n",balanceInquiry())
    repeat()

def repeat():
    num =int(input("Enter your choice:"))
    str(num).strip()

    if num == 1:
        balanceInquiry()
    elif num == 2:
        cashDeposit()
    elif num == 3:
        cashWithdraw()
    elif num == 4:
        print("Thank you !!")
        exit()
    else:
        print("Invalid Input!")


balance=5000

print("\t \t",30*'*')
print("\t \t \tWelcome to SBI ATM")
print("\t \t",30*'*')
print("\n1. Check Balance")
print("2. Deposit cash")
print("3. Withdraw Cash")
print("4. Exit")

repeat()
