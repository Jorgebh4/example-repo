# Program calculating investments and home loan repayments
import math

# First we ask them to select what they are looking to calculate
print("""Please Select:
Investment: To calculate the amount of interest you'll earn on your investment.
Bond: To calculate the ammount you'll have topay on a home loan""")
choice = (str(input("""
Enter either investment or bond from the menu above to proceed: 
                    """)))
choice = choice.lower()

# if investment, we get the details
if choice == "investment":
    amount = (int(input("How much money are you depositing? ")))
    interest_rate = (input("""What's your interest rate
                           (without the percentage symbol? """))
    interest_rate = ((float(interest_rate)) / 100)
    years = (int(input("How many years do you plan on investing? ")))
    interest = (str(input("Please select simple or compound interest? ")))
    interest = interest.lower()

    # Now we calculate their investement depending on interest
    if interest == "simple":
        repayment = (amount*(1 + (interest_rate*years)))
        print(f"Your repayment is {repayment}.")

    elif interest == "compound":
        repayment = (amount*math.pow((1 + interest_rate), years))
        print(f"Your repayment is {repayment}.")

    # if neither is selected
    else:
        print("Error, please select 'simple' or 'compound' interest ")


# If they selected bond, we get their investment details
elif choice == "bond":
    house_value = (int(input("What is the value of your house? ")))
    interest_rate = (input("""What's your interest rate
                           (without the percentage symbol? """))
    interest_rate = ((float(interest_rate)) / 100)
    monthly_interest = (interest_rate / 12)
    months = (int(input("How many months will you take to repay the bond? ")))

# Then we calculate the repayment
    repayment = ((monthly_interest*house_value) /
                 (1 - (1 + monthly_interest) ** (- months)))
    print(f"Your repayment is {repayment}.")


else:
    print("Error, please select 'investment' or 'bond': ")
