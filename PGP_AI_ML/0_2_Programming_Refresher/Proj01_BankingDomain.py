'''
Created on 4 Oct. 2021

@author: praka
'''
import random
class bank():
    # Bank Object helps to identify the Bank
    def __init__(self, IFSC_Code, bankName, branchName, loc):
        self.IFSC_Code  = IFSC_Code
        self.bankName   = bankName
        self.branchName = branchName
        self.loc        = loc
        
class customer():
    # Customer Object helps to identify the Customer
    # Name, Address, Contact Details are Optional, required at time of registering customer
    # Otherwise to be identified from Customer ID
    def __init__(self, cid, name='', address='', contactdetails=''):
        self.CustomerID     = cid
        self.custname       = name
        self.address        = address
        self.contactdetails = contactdetails
        self.validCustomer  = False
        self.validateCid()
        
    def validateCid(self):
        # Validate Customer ID
        if (len(self.CustomerID) != 8):
            print("Invalid Customer ID, Customer ID Length is 8 Digits")
            self.validCustomer = False
        else:
            self.validCustomer = True
class account(bank):
    # Account Object is base object for all Accounts Type
    # Bank Details are optional as it is only needed during Account Creation
    # Otherwise it will be identified using Account Number
    # Account ID is optional too, as it will be identified using Customer ID 
    # Balance is optional as it is derived value
    def __init__(self, accid, cust, IFSC_Code='', bankName='', branchName='', loc='', bal=0.000 ):
        self.AccountID = accid
        self.customer = cust
        self.balance = bal
        super().__init__(IFSC_Code=IFSC_Code, bankName=bankName, branchName=branchName, loc=loc)
        
    def getAccountInfo(self):
        print("\n****Customer Details****")
        print("Customer ID: ", self.customer.CustomerID)
        print("Name: ", self.customer.custname)
        print("Address: ", self.customer.address)
        print("Phone/Mobile: ", self.customer.contactdetails)
        print("\n****Account Details****")
        print("Account ID: ", self.AccountID)
        print("IFSC Code: ", self.IFSC_Code)
        print("Bank Name: ", self.bankName)
        print("Branch Name: ", self.branchName)
        print("Branch Address: ", self.loc)
        print("Your Account Balance: ", self.getBalance())
        return
    
    def deposit(self,amt,flag=True):
        self.balance += amt
        print("Amount deposited is: ", amt, " and New Account Balance is: ", self.balance)
        return
    
    def withdraw(self,amt):
        if(amt > self.balance ):
            print("Insufficient Fund: Account Balance is: ", self.balance)
        else:
            self.balance -= amt
            print("Amount withdrawn is: ", amt, " and New Account Balance is: ", self.balance)
        return
    
    def getBalance(self):
        return self.balance
    
class savingAccount(account):
    # Saving Account Type
    # For Saving Account Default Min Balance is set to 2000
    def __init__(self, accid, cust, IFSC_Code='', bankName='', branchName='', loc='', bal=0.000, minBal=2000):
        self.SminBalance = minBal
        super().__init__(accid=accid, cust=cust, IFSC_Code=IFSC_Code, bankName=bankName, branchName=branchName, loc=loc, bal=bal)
        
    
    def getSavingAccountInfo(self):
        super().getAccountInfo()
        return
    
    def getBalance(self):
        return super().getBalance()
    
    def withdraw(self, amt):
        newbal = self.balance - amt
        if(newbal < self.SminBalance ):
            print("Insufficient Fund: Account Balance is: ", self.balance, " . Minimum balance required for this account is :", self.SminBalance)
        else:
            self.balance -= amt
            print("Amount withdrawn is: ", amt, " and New Account Balance is: ", self.balance)
        return
    
    def deposit(self, amt, flag=True):
        super().deposit(amt, flag=flag)
        return 
    
class customerSupport():
    def __init__(self):
        self.customerChoice = ''
        self.customerID = 00000000
        
        
    def identifyCustomer(self):
        print("Welcome to Your Bank -- We make your finances simple\n")
        existing = input("Are you existing Customer Y/N: ").upper()
        
        if (existing == 'Y'):
            self.existingCustomer()
        else:
            self.newCustomer()
            
    def newCustomer(self):
        openAcc = input("Would you like to open a Saving Account with us Y/N: ").upper()
        
        if (openAcc == 'Y'):
            self.openAccount()
        else:
            print("Thanks for your time, we appreciate it. Visit us Again")
            
    def existingCustomer(self):
        self.customerID = input("Enter your 8 digits Customer ID: ")
        self.customer = customer(self.customerID)
        
        if(self.customer.validCustomer == True):
            print("We are experiencing server issue right now. Please try again later. \nSorry for Inconvenience Caused")
            
    def allowCustomerAction(self):
        # Request First Choice
        self.getCustomerChoice()
        
        # Stay in the session until user chose to exit
        while(self.customerChoice != 'X'):
            
            if(self.customerChoice == 'C'):   # Check Balance
                bal = self.customerAccount.getBalance()
                print("Your Account Balance is: ", bal)
            elif(self.customerChoice == 'D'): # Deposit
                depositAmt = float(input("Please enter the amount you would like to deposit: "))
                self.customerAccount.deposit(depositAmt)
            elif(self.customerChoice == 'W'): # Withdraw
                withdrawAmt = float(input("Please enter the amount you would like to withdraw: "))
                self.customerAccount.withdraw(withdrawAmt)
                
            # Request Choice Again   
            self.getCustomerChoice()
        print("We appreciate our relationships. Please visit again")
        
        return 
    
    def getCustomerChoice(self):
        print("\nWhat would you like to do today")
        print("* C for Checking Balance")
        print("* D for Deposit")
        print("* W for Withdrawal")
        print("* X for Exit")
        self.customerChoice = str(input("Please enter one of the above choices: ")).upper() # Convert Input to Upper Case for Consistency
        return
    
    def openAccount(self):
        # Get Customer Details
        name = input("Enter your name: ").upper()
        address = input("Enter your address: ").upper()
        contact = input("Enter your phone/mobile#: ")
        cid = str(random.randint(10000000, 99999999 )) # Random Customer ID generation for Demo
        
        # Create Customer Object
        self.customer = customer(cid, name, address, contact)
        
        # Get Bank Branch Info
        postcode = input("Enter the post code of Bank Branch, where you would like to open the account: ")
        
        # Defaulting Bank Information for Demo Purpose
        ifscCode   = "YRBNKIF" + postcode
        bankName   = "Your Bank"
        branchName = "Your Bank Branch " + postcode
        street     = "Your Branch, At Your Street, Your City," + postcode
        amount     = float(input("Please confirm Initial Deposit Amount >= 2000.000 Local Currency : "))
        accid      = str(random.randint(100000000,999999999))
        self.customerAccount = savingAccount(accid=accid, cust=self.customer, IFSC_Code=ifscCode, bankName=bankName, branchName=branchName, loc=street, bal=amount )
        
        print("\nCongratulations! Your Account is open Please make Initial Deposit to Activate your Account")
        
        # Get Saving Account Info
        self.customerAccount.getSavingAccountInfo()
        
    def printSummary(self):
        print("\n****Customer Info****")
        print("\nCustomer ID: ", self.customer.CustomerID)
        print("\nName: ", self.customer.custname)
        print("\nAddress: ", self.customer.address)
        print("\nPhone/Mobile: ", self.customer.contactdetails)
        print("\nAccount ID", self.customerAccount.AccountID)

        
# Create Instance of Customer Support
selfServe = customerSupport()

# Identify the Customer
selfServe.identifyCustomer()

# Allow Customer to Transact
if(selfServe.customer.validCustomer == True):
    selfServe.allowCustomerAction()


    