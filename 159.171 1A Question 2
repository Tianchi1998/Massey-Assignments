#The function below generates a list of people the user needs to buy birthday gifts for.
birthday_gift_list=[]
def list_of_people(the_number_of_gifts):
    for i in range(the_number_of_gifts):
        the_name=str(input("Enter name %d: "%(i+1)))
        birthday_gift_list.append(the_name)
    print(birthday_gift_list)

#Let the user enter the number of gifts needed to buy.
the_number_of_gifts=int(input("How many birthday gifts do you need to buy? "))

#Then call the function.
list_of_people(the_number_of_gifts)

#This function below caculates and prints every person's budget and the total budget.
def budget():
    total=0
    for person in birthday_gift_list:
        money=int(len(person)*10)
        total=total+money
        print("My budget for a gift for %s is: $%d"%(person,money))
    print("My total birthday gift budget is: $%d"%(total))

#Call the new function.
budget()
