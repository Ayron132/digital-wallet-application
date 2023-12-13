class Account ():
  def __init__(self, name, cpf, password, balance, credit, phoneCredit):
    self.name = name
    self.cpf = cpf
    self.password = password
    self.balance = int(balance)
    self.historic = []
    self.credit = int(credit)
    self.loyaltyPoints = 0
    self.phoneCredit = int(phoneCredit)

  def mobileRechargeAndBillPayment(self, amount, password, paymentType):
    if self.wrongPassword(password):
      return None

    if paymentType not in ['credit', 'debit']:
      print("Invalid payment type")
      return None

    if paymentType == 'credit':
      self.credit -= amount
    elif paymentType == 'debit':
      self.balance -= amount

    self.phoneCredit += amount
    self.historic.append(["Mobile Recharge/Bill Payment", amount])
    self.notification(True, "Mobile Recharge/Bill Payment") 

  def wrongPassword(self, password):
    if self.password != password:
      return True
    return False
  
  def deposit(self, amountToDeposit, password):
    if (self.wrongPassword(password)): 
      return None

    if amountToDeposit < 0:
      print('You cannot deposit a negative amount')
      return None
    
    self.historic.append(["Deposit", amountToDeposit])
    self.notification(True, "Deposit")
    self.balance = self.balance + amountToDeposit
    self.addLoyaltyPoints()
    return self.balance
  
  def getName(self):
    return self.name
  
  def getPhoneCredit(self, password):
    if (self.wrongPassword(password)):
      return None
    return self.phoneCredit
        
  def getBalance(self, password):
    if (self.wrongPassword(password)):
      return None
    return self.balance
  
  def getLoyaltyPoints(self, password):
    if (self.wrongPassword(password)):
      return None
    return self.loyaltyPoints
  
  def getCredit(self, password):
    if (self.wrongPassword(password)):
      return None
    return self.credit
  
  def getPayment(self, amountToDeposit, whoSent):
    self.balance = self.balance + amountToDeposit
    self.historic.append(["Payment from " + whoSent, amountToDeposit])
    self.notification(True, "Payment received")
    return self.balance
  
  def notification(self, notificationStatus, message):
    if(notificationStatus):
      print(message, 'successfully')
      return None
    
    print(message, "not completed")
  
  def makePayment(self, amountToDeposit, accountToPay, password):
    if (self.wrongPassword(password)):
      return None
    
    self.historic.append(["Payment made to " + accountToPay.getName(), amountToDeposit])
    accountToPay.getPayment(amountToDeposit, self.name)
    self.balance = self.balance - amountToDeposit
    self.notification(True, "Payment")
    self.addLoyaltyPoints()
    return self.balance

  def getHistoric(self, password):
    if (self.wrongPassword(password)):
      return None

    if (len(self.historic)) == 0:
      print('Has no historic')
      return None
    
    for x in range(len(self.historic)):
      print(self.historic[x][0], "----->", self.historic[x][1])

  def addLoyaltyPoints(self):
    self.loyaltyPoints += 1
  
  def securePaymentProcessing(self, transactionAmount, password):
    if self.wrongPassword(password):
      return None

  def linkAccount(self, accountToLink, password):
    if self.wrongPassword(password):
      return None

    self.linkedAccounts.append(accountToLink)

  def peerToPeerTransfer(self, amountToTransfer, recipientAccount, password):
    if self.wrongPassword(password):
      return None

    if amountToTransfer < 0 or amountToTransfer > self.balance:
      print('Invalid transfer amount')
      return None

    self.balance -= amountToTransfer
    recipientAccount.balance += amountToTransfer
    self.historic.append(["Peer-to-Peer Transfer to " + recipientAccount.getName(), amountToTransfer])
    self.notification(True, "Peer-to-Peer Transfer")
    recipientAccount.notification(True, "Received Peer-to-Peer Transfer from " + self.getName())

account1 = Account("John Doe", "123456789", "password123", 1000, 500, 50)
account2 = Account("Jane Doe", "987654321", "password456", 800, 300, 30)

account1.linkedAccounts = []

account1.linkAccount(account2, "password123")
account1.peerToPeerTransfer(200, account2, "password123")
account1.mobileRechargeAndBillPayment(20, "password123", "debit")

account1.getHistoric("password123")
print('balance', account1.getBalance("password123"))
