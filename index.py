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

  def addPhoneCredit(self, credit, password, type):
    if (self.passwordCheck(password)): 
      return None
    
    if(type == 'credit'):
      self.credit -= credit
    elif(type == 'debit'):
      self.balance -= credit
    else:
      print("Invalid credit type")
      return None

    self.phoneCredit += credit;  

  def passwordCheck(self, password):
    print('Sorry, incorrect password')
    return self.password == password
  
  def deposit(self, amountToDeposit, password):
    if (self.passwordCheck(password)): 
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
    if (self.passwordCheck(password)):
      return None
    return self.phoneCredit
        
  def getBalance(self, password):
    if (self.passwordCheck(password)):
      return None
    return self.balance
  
  def getLoyaltyPoints(self, password):
    if (self.passwordCheck(password)):
      return None
    return self.loyaltyPoints
  
  def getCredit(self, password):
    if (self.passwordCheck(password)):
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
    if (self.passwordCheck(password)):
      return None
    
    self.historic.append(["Payment made to " + accountToPay.getName(), amountToDeposit])
    accountToPay.getPayment(amountToDeposit, self.name)
    self.balance = self.balance - amountToDeposit
    self.notification(True, "Payment")
    self.addLoyaltyPoints()
    return self.balance

  def getHistoric(self, password):
    if (self.passwordCheck(password)):
      return None

    if (len(self.historic)) == 0:
      print('Has no historic')
      return None
    
    for x in range(len(self.historic)):
      print(self.historic[x][0], "----->", self.historic[x][1])

  def addLoyaltyPoints(self):
    self.loyaltyPoints += 1

  