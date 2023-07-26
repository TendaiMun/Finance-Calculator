#The following is a Python program that allows the user to access two different financial calculators:
#an investment calculator and a home loan repayment calculator.

import math

while True:
      
    print('''Finance Calculator Menu

    investment - to calculate the amount of interest you'll earn on an investment 
    bond       - to calculate the amount you'll have to pay on a home loan 
    e          - to exit
    \n''')
    selection = input("Select 'investment' or 'bond' from the menu to proceed, or 'e' to exit: \n")

    if selection.lower() == "investment": 
        amount = int(input("Enter the amount of money that you are depositing: \n"))
        interest_rate = int(input("Enter the interest rate (as a percentage e.g 8 not 8%): \n"))
        years = int(input("The number of years you plan on investing for: \n"))
        interest = input("Input whether you want 'simple' or 'compound' interest: \n")

    #Determining the output interest which user will get depending on interest type they entered.
        if interest == "simple":
            print(f'The future value of your investment will be: {round(amount*((1 + (interest_rate/100))*years),2)})')
        elif interest == "compound":
            print(f'The future value of your investment will be: {round(amount * math.pow((1+(interest_rate/100)),years),2)})')

                
    #How the user capitalises their 'bond' selection should not affect how the program proceeds
    #If bond is selected, request the following from user
    elif selection.lower() ==  "bond":
        present_value = int(input("Enter the present value of the house: \n"))    
        bond_interest = int(input("Enter the interest rate (as a percentage e.g 8 not 8%): \n"))
        months = int(input("Enter the number of months you plan to repay the bond: \n"))
        print("Your bond repayment will be: ")
        bond_answer = ((bond_interest/12) * present_value)/(1 - (1+(bond_interest/12))**(-months))
        print(round(bond_answer,2))

    elif selection.lower() == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have not made your selection or you made an invalid selection. Please try again.")
    