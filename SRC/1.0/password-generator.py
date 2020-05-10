#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random

def menu():
    cls()
    print(
"""Now,tell me - what are your requirements for the passwords:

1. Capital and small letters, numbers and special characters
2. Capital and small letters and numbers
3. Capital and small letters and special characters
    
    """)

    try: 
        choiceStr=int(input("What is your choice? \n"))
    except ValueError:
        print("You should choose a number between 1 to 3")
        return menu()
    except KeyboardInterrupt:
        print("Keyboard interrupt error! ")
        return menu()
    except:
        print("General error!")
    else:
        if(choiceStr>3 or choiceStr<1):
            cls()
            print("You should choose a number between 1 to 3")
            return menu()
        else:
            return choiceStr

def decide():
    #password lenght selection
    try:
        charCount = int(input("How many characters per password should be generated: \n"))
    except ValueError:
        print("You should type a number! ")
        return decide()
    except KeyboardInterrupt:
        print("Keyboard interrupt error! ")
        return decide()
    except:
        print("General error")
        return decide()
    else:
        if(charCount<8):
            cls()
            print("You should choose a number 8 or greater")
            return decide()
        elif(charCount>36):
            cls()
            print("There is completely no reason for a such a large number")
            return decide()
    #password count selection
    try:
        passCount = int(input("How many passwords should be generated: \n"))
    except ValueError:
        print("You should type a number! ")
        return decide()
    except KeyboardInterrupt:
        print("Keyboard interrupt error! ")
        return decide()
    except:
        print("General error")
        return decide()
    else:
        if(passCount<1):
            cls()
            print("You should choose a number 1 or greater")
            return decide()
        elif(passCount>1000000):
            cls()
            print("There is completely no reason for such a big number")
            return decide()
    return charCount, passCount

#saving to the file in A mode 
def save2file(password):
    try:
        file = open("Passwords.txt",'a')
    except IOError as e:
        print(e.test_strerror)
    else:
        file.write(password)
        file.write("\n")
        file.close()

#check if the password has at least 5 letters (small or Capital but at least 1 of each)
#and at least 1 number or/and at least 1 special character (depends from selection from menu())
def checkPassword(password, complexity):
    if(complexity==1):
        countC=0
        countS=0
        countN=0
        countSpec=0
        for i in password:
            for j in varListC:
                if(i==j):
                    countC+=1
        for i in password:
            for j in varListS:
                if(i==j):
                    countS+=1 
        for i in password:
            for j in varListN:
                if(i==j):
                    countN+=1 
        for i in password:
            for j in varListSpec:
                if(i==j):
                    countSpec+=1 
        if(countC>=1 and countS>=1 and countC+countS>=5 and countN>=1 and countSpec>=1):
            return True
        else:
            return False
    elif(complexity==2):
        countC=0
        countS=0
        countN=0
        for i in password:
            for j in varListC:
                if(i==j):
                    countC+=1
        for i in password:
            for j in varListS:
                if(i==j):
                    countS+=1 
        for i in password:
            for j in varListN:
                if(i==j):
                    countN+=1 
        if(countC>=1 and countS>=1 and countC+countS>=5 and countN>=1):
            return True
        else:
            return False
    elif(complexity==3):
        countC=0
        countS=0
        countSpec=0
        for i in password:
            for j in varListC:
                if(i==j):
                    countC+=1
        for i in password:
            for j in varListS:
                if(i==j):
                    countS+=1 
        for i in password:
            for j in varListSpec:
                if(i==j):
                    countSpec+=1 
        if(countC>=1 and countS>=1 and countC+countS>=5 and countSpec>=1):
            return True
        else:
            return False
    else:
        print("General error")
        return False
    

#clearing file content                                                
def clearFile():
    try:
        file = open("Passwords.txt",'w')
    except IOError as e:
        print(e.test_strerror)
    else:
        file.close()

#clearing screen (works on both linux/mac and windows based systems)
def cls():
    if(os.name=='nt'):
        os.system("cls")
    else:
        os.system("clear")  
        
def generatePassword(length,complexity):
    if(complexity==1):
        password='';
        i=0
        while i<length:
            password=password + varListCombinedAll[random.randint(0,len(varListCombinedAll)-1)]
            i+=1
        if(checkPassword(password,complexity)==True):
            return password
        else:
            generatePassword(length,complexity)
    elif(complexity==2):
        password='';
        i=0
        while i<length:
            password=password + varListCombinedCharPlusNumbers[random.randint(0,len(varListCombinedCharPlusNumbers)-1)]
            i+=1
        if(checkPassword(password,complexity)==True):
            return password
        else:
            generatePassword(length,complexity)
    elif(complexity==3):
        password='';
        i=0
        while i<length:
            password=password + varListCombinedCharPlusSpec[random.randint(1,len(varListCombinedCharPlusSpec)-1)]
            i+=1
        if(checkPassword(password,complexity)==True):
            return password
        else:
            generatePassword(length,complexity)
    else:
        print("General error")
        main()
        
def main(): 
    
    complexity= menu()
    decideVar = decide()
    length=decideVar[0]
    count=decideVar[1]
    cls()
    i=0
    while i<count:
        password=generatePassword(length,complexity)
        if(password!=None):
            if(i%(count/5)==0):
                cls()
                print("{:1} %".format(i/count*100))
                
            if (count==1):
                print("The password is: ",password)
            save2file(password)
            i+=1
    
    print("Passwords saved to the file Passwords.txt")
        
varListC=['A','B','C','D','E','F','G','H','I','J','K','L','M',
                 'N','O','P','Q','R','S','T','U','W','X','Y','Z']
varListS=['a','b','c','d','e','f','h','h','i','j','k','l','m',
                 'n','o','p','q','r','s','t','u','w','x','y','z']
varListN=['1','2','3','4','5','6','7','8','9','0']
varListSpec=['@','#','!','$','%','?','>','<','.',',',']','[','}','{','+','-','_','^','=','&','*']
varListCombinedAll = varListC + varListS + varListN + varListSpec
varListCombinedCharPlusNumbers = varListC + varListS + varListN
varListCombinedCharPlusSpec = varListC + varListS + varListSpec   
clearFile()
main()
