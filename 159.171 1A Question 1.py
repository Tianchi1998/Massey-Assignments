# The function below caculates the amount of money that should be repaid each week.
def weekly_pay_back(loan_amount,number_of_weeks):
    result=loan_amount/number_of_weeks
    return result

# The 7 and 8 lines ask the user to enter his information.
loan_amount=int(input("Enter an amount: "))
number_of_weeks=int(input("Enter a number of weeks: "))

# Then we call the function and print the result.
repay=weekly_pay_back(loan_amount,number_of_weeks)
print("You must repay $%0.2f per week to repay a loan of $%d in %d weeks."%(repay,loan_amount,number_of_weeks))
