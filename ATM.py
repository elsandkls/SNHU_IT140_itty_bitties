import sys

#account balance 
account_balance = float(500.25)
 
# custom function
#account balance function 
def print_account_balance(account_balance):
  #input is account_balance
  print("Your current balance:")
  print('{:,.2f}'.format(account_balance))
  return()

# custom function
#process deposit function
def process_deposit(deposit_amount, account_balance):
  #inputs are deposit_amount and account_balance
  account_balance = account_balance + deposit_amount
  print("Deposit was ",'${:,.2f}'.format(deposit_amount),", current balance is ",'${:,.2f}'.format(account_balance))
  return(account_balance)
  #returns account balance

# custom function 
#process withdraw function
def process_withdrawal(withdrawal_amount, account_balance):
  #inputs are withdrawal_amount and account_balance
  if(account_balance > withdrawal_amount):
    account_balance = account_balance - withdrawal_amount
    print("Withdrawal amount was ",'${:,.2f}'.format(withdrawal_amount),", current balance is ",'${:,.2f}'.format(account_balance))
  else:
    print('${:,.2f}'.format(withdrawal_amount),"is greater than your account balance of",'${:,.2f}'.format(account_balance))
    
  return(account_balance)
  #returns account balance

#collect users input
userchoice = input ("What would you like to do?\n")

# excute users actions, (branch) D for deposit
if (userchoice == 'D'):
  deposit_amount = input ("How much would you like to deposit today?\n")
  deposit_amount = float(deposit_amount)
  process_deposit(deposit_amount, account_balance)
  #returns account balance
# excute users actions, (branch) B for print balance
elif(userchoice == 'B'):
  account_balance = print_account_balance(account_balance)
# excute users actions, (branch) W for withdrawal
elif(userchoice == 'W'):
  withdrawal_amount = input ("How much would you like to withdraw today?\n")
  withdrawal_amount = float(withdrawal_amount)
  account_balance = process_withdrawal(withdrawal_amount, account_balance)
  #returns account balance
else:
  print("Thank you for banking with us.\n")
  # end program with "Q" or any other input not defined
