class BankAccount:

  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
    
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("desosited ${}. New Balance : ${}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit amount . pls deposit a positive amount.")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdraw ${}. New Balance : ${}".format(amount,self.__account_balance))
    else:
      print("invalid withdrawal amount or insufficient balance")
      
  def display_balance(self):
    print("account balance for{} (amount #{}): ${}".format(self.__account_holder_name, 
         self.__account_number, self.__account_balance))
account = BankAccount(account_number ="12345678910",
                      account_holder_name ="Hari",
                      initial_balance = 10000.0)

account.display_balance()
account.deposit(5000.0)
account.withdraw(100.0)
account.display_balance()