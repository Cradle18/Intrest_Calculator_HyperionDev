import math

#This is a finance calculator programme, allows the user to choose between an investment calculator and a bond calculator.

"""Please note when reviewing this, i have completed what the question has asked, 
which is to provide the total amount of investment including the interest.
I have been getting conflicting reviews, on what i need to do, if the below code is wrong, please can it be explained why,
as i have had a mentor call about this task and they believe i have done it right. """

print("Welcome to the interest calculator. Please select between the two below options.")
print("\nInvestment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to repay on a home loan.")

bond_or_investment = input("\nPlease enter ether 'investment' or 'bond' from the menu above to proceed: ").lower()

#The statement below calculates the amount of interest they would get on there investment or amount that would need to be repayed on a bond.

#User chooses investment. 
if bond_or_investment == "investment":
    #The below variable names are named as they are to help with the formula.
    p_deposit = int(input(f"You have chosen {bond_or_investment}, please enter the amount you wish to deposit: "))
    r_interest_rate = int(input("\nPlease enter the interest rate: ")) / 100
    t_years = int(input("Please enter the number of years you plan to invest: "))
    interest = input("Please enter wether you would like ether 'compound' or 'simple' interest: ").lower()
    
    if interest == "compound":
        a_total_amount = round(p_deposit * math.pow((1+r_interest_rate), t_years))
        print(str(f"\nYou're total investment will be £{a_total_amount}"))
    elif interest == "simple":
        a_total_amount = round(p_deposit * (1 +  r_interest_rate * t_years))
        print(str(f"\nYou're total investment will be £{a_total_amount}"))
    else:
        print("Invalid input!")
#user selects bond
elif bond_or_investment == "bond":
    p_house_value = int(input("\nPlease enter the value of the property: "))
    r_interest_rate = int(input("Please enter the interest rate: ")) / 100
    n_months = int(input("Please enter the number of months for the bond: "))
    i = r_interest_rate/12
    repayment = round((i * p_house_value)/(1 - (1 + i)**(-n_months)))
    print(f"\nYour monthly repayments will be £{repayment} over {n_months} months.")
else:
    print("You have not entered a valid response.")

