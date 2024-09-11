#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[13]:


#this is for transfer
def tranfer (amount):
    if amount < 500:
        print("Sorry you can transfer above than 500")
    else:
        Bank = input("Enter you bank  : ")
        bank = ["HBL","ABL","NBP","UBL"]
        if Bank not in bank:
            print("Invalid Bank")
            return False
        else:
            print("You have with transfer",amount," successfully")
            return True
#This is for balance checking        


# In[14]:


#This is for balance checking        
def balance(Bank):
    bank = ["HBL","ABL","NBP","UBL"]
    if Bank not in bank:
        print("Invalid Bank")
        return False
    else:
        print("Your current balance is 45000")
        return True


# In[15]:


#This is for withdraw
def withdraw (amount):
    if amount < 500:
        print("Sorry you can withdraw above than 500")
    else:
        Bank = input("Enter you bank  : ")
        bank = ["HBL","ABL","NBP","UBL"]
        if Bank not in bank:
            print("Invalid Bank")
            return False
        else:
            print("You have withdraw ",amount," successfully")
            return True


# In[ ]:


import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Replace with a secure way to store and retrieve hashed passwords
hashed_password = hash_password("1234")  # For demonstration only

print("Welcome to ATM")

while True:
    q=input("If you want to continou press Yes/No")
    a = input("Enter your ATM Card and press A: ")
    if a.lower() == 'a':
        pin = getpass.getpass("Enter your 4-digit PIN: ")
        if hash_password(pin) == hashed_password:
            print("Thank you. What would you like to do?")
            print("Press 1 to Withdraw")
            print("Press 2 to Balance checking")
            print("Press 3 to Transfer")
            option = int(input())
            if option == 1:
                
                amount = int(input("Enter amount to withdraw: "))
                print(withdraw(amount))
            elif option == 2:
                bank = input("Enter your bank")
                print(balance(bank))
            elif option == 3:
                ammount = int(input("Enter amount to withdraw: "))
                print(transfer(ammount))
     
   
            
            else:
               print("Invalid option")
        else:
            print("Incorrect password")
    
    else:
        print("Invalid card input")

if q.lower() =="yes":
    break


# In[ ]:




