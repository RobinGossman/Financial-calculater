import math

# i started the financial calculater by printing out 3 statement
# the 1st statement explains to the user what to do
# the 2nd and 3rd 1 explains to the user what the inputs are namely bond and investement.

print("Choose either 'investment' or 'bond' from menu below: \n")
print("Investment         -to calculate the amount of interest you'll earn on interest.")
print("Bond               -to calculate the amount you'll have to pay on a home loan. \n")

# I then wrote a input statement requesting the user to input whhich option they would like.
# i stored the users input in a variable called menu select.

menu_select=input("Enter either 'investment' or 'bond':").lower()

# i then used if condition with or so that the user would be able to input the word in caps or small letters
# if user input was investment the program would ask user for details needed for investment.
# it would store users input in the variables namely money_deposit, interest_rate, num_years & interest.

if menu_select == "investment":
    print("You have selected investment. \n")
    money_deposit=float(input("Enter how much money you are depositing:"))     
    interest_rate=int(input("Enter the interest rate:"))
    num_years=int(input("Enter the amount of years you would like to invest for:"))
    interest=input("Would you like 'simple' or 'compound' Interest?:").lower()

# below i have 2 indented if statements which are dependant on users input for interest.
# if user puts in simple it would calculate simple interest using all users input variables.
# then it would print out the answer

    if interest == "simple" :
        simple_interest = money_deposit * (1 + interest_rate / 100 * num_years)
        print("The amount with simple interest is R",simple_interest)

# if user enters compound it would calculate the simple interest for the investment.
# then it would print out the answer

    if interest == "compound" :
        compound_interest = money_deposit * math.pow((1 + interest_rate / 100), num_years)
        compound_int=round(compound_interest, 2)
        print("The amount with compound interest is R",compound_int)

# i used elif if user entered bond and used or so whether user enters it in caps or small letters the program would still run
# it would print they have selected bond
# once they entered bond it would ask them for the details below
# and store the details in variables called value_house, monthly_interest, num_months.
# it would then calculate bond_repayment and print out a statement with the answer.

elif menu_select == "bond":
    print("You have selected bond. \n")    
    value_house = int(input("Enter present value of house eg. 100000:"))
    interest_rate = int(input("Enter the interest rate eg. 7:"))
    num_months = int(input("Enter number of months in which bond will be repaid eg. 120:"))

    monthly_interest = (interest_rate / 100)
    monthly_interest = (monthly_interest / 12)
    bond_repayment =(monthly_interest*value_house) / (1 - (1 + monthly_interest)**(- num_months))
    bond_repayment = round(bond_repayment, 2)
    print("Your bond repayment is R",bond_repayment)             

# i used an else statement so if user does not input bond or interest correctly.
# it would print out an error message saying that.

else:
    print("You have not selected one of the available options.")    
    


     
                  



