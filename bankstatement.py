balance=0
amount=0
choice=""

while True:
 print("1) Deposit")
 print("2) Withdraw")
 print("3) Print Balance")
 print("4) Quit")
 
 choice=input("Enter Choice:")
 choice = choice.strip()
 
 if (choice == "1"):
  amount=float(input("Enter Amount: "))
  balance+=amount
  print("Deposited:", amount, "New Balance:", balance)
 elif (choice =="2"):
  amount=float(input("Enter Amount: "))
  balance -= amount
  print("Withdrew:", amount, "New Balance:", balance)
 elif (choice == "3"):
  print("Balance:", balance)
 elif (choice =="4"):
  #print("Quit",Quit)
  break
 else:
  print("Invalid Option, Please Try again.")