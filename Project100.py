class ATM:
    def __init__(self,card_number,pin):
        self.card_number=card_number
        self.pin=pin
    def checkBalance(self):
        print('Your balance is 50000')
    def withdrawal(self,amount):
        newAmount = 50000-amount
        print('You have withdrawn' + str(amount))
        print('You have' + str(newAmount) )

def main():
    card_number=int(input('Enter card number'))
    pin=int(input('Enter pin'))
    newUser=ATM(card_number,pin)
    print('Choose your activity')
    print('1. Balance inquiry') 
    print('2. Withdrawal')
    activity = int(input('Enter your activity number'))
    if(activity==1):
        newUser.checkBalance()
    elif(activity==2):
        amount=int(input("Enter amountot be withdrawn"))
        newUser.withdrawal(amount)
    else:
        print('Enter a valid number')

main()