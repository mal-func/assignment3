import random
class Bank:
  def __init__(self,name,acType,balance):
    self.customerName = name
    self.customerNo = int(random.random()*10000000000)
    self.accountType = acType
    self.balance = balance
  
  def deposit(self,depo):
    self.balance = self.balance+ depo
    print('Account Number ',self.customerNo)
    print('Name '+self.customerName)
    print('Amount Deposited '+str(depo))
    print('Balance: Rs. '+ str(self.balance))
  
  def withdrawal(self,withdrawalAmt):
    if withdrawalAmt >self.balance:
      print('Message')
      print('You do not have sufficient balance in your account')
      print('Balance '+ str(self.balance))
    else:
      self.balance = self.balance - withdrawalAmt
      print('Withdrawal Amount: Rs. '+str(withdrawalAmt))
      print('Balance: Rs. '+str(self.balance))


name = input('Enter the customer name: ')
acType = input('Enter the account type: ')
print('Enter 1 to deposit')
print('Enter 2 to withdrawal')
ch = int(input('Enter your choice!! '))
if ch == 1:
  depo = int(input('Enter the amount to be deposited: '))
  ob = Bank(name,acType,50000)
  ob.deposit(depo)
if ch == 2:
  withdrawal = int(input('Enter the amount to be withdrawal: '))
  ob = Bank(name,acType,50000)
  ob.withdrawal(withdrawal)
