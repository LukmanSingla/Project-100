class Atm():
    def __init__(self, availCash, accBalance):
        self.availableCash = availCash
        self.accBalance = accBalance

    def ask(self):
        self.cardNo = input('Please enter the card number : ')
        self.pinNo = input('Please enter the PIN number : ')
        self.transactionType = input('Please enter transactionType : ').lower()
        self.start()

    def start(self):
        if self.transactionType == 'withdraw':
            self.withdraw()
        elif self.transactionType == 'balanceenquiry':
            self.balanceEnquire()
        else:
            self.transactionType = input('Please enter again : ')
            self.start()

    def withdraw(self):
        withdrawlAmount = int(input('Please enter the amout to withdraw : '))
        if withdrawlAmount < self.accBalance and withdrawlAmount < self.availableCash:
            print('Please collect the cash...')
            self.availableCash = self.availableCash-withdrawlAmount
            self.accBalance = self.accBalance-withdrawlAmount
            self.ask()
        else:
            print("Please enter lower amount")

    def balanceEnquire(self):
        print("You have rupees", self.accBalance, ' in your account')
        self.ask()


myAtm = Atm(1234632, 100000)
myAtm.ask()
