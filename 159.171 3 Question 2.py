addressbook = {}     #This is the outside dictionary.
def add():
    one_person_details = {}   #This is the inside dictionary.
    nickname = input("The nickname is: ")
    if nickname == "":      #This IF statement is for aborting the add command.
        return
    if nickname in addressbook:     #This IF statement is for the nickname that has ever been seen.
        answer = input("Should the new entry replace the existing one for this nickname?(yes/no) Your answer: ")
        if answer == "no":
            nickname = input("The new nickname is: ")   #To give this new entry a new nickname which is different from the first one.
        elif answer == "yes":
            pass
    name = input("The name is: ")
    address = input("The address is: ")
    phone_no = input("The phone number is: ")
    one_person_details["name"] = name
    one_person_details["address"] = address
    one_person_details["phone_no"] = phone_no
    one_person_details["nickname"] = nickname
    addressbook[nickname] = one_person_details


def find():
    nickname = input("The nickname you want to search: ")
    if nickname == "":
        return
    nickname = nickname.capitalize()
    if nickname in addressbook:
        name = addressbook[nickname]["name"]
        address = addressbook[nickname]["address"]
        phone_no = addressbook[nickname]["phone_no"]
        print(name)
        print(address)
        print(phone_no)
    else:
        print("There is no entry with this nickname.")


def delete():
    nickname = input("The nickname: ")
    if nickname == "":
        return
    if nickname in addressbook:
        name = addressbook[nickname]["name"]
        address = addressbook[nickname]["address"]
        phone_no = addressbook[nickname]["phone_no"]
        print("Name: " + name)
        print("Address: " + address)
        print("Phone-no: " + phone_no)
        answer = input("Is this the correct one to be deleted?   Your answer(yes/no): ")
        if answer == "yes":
            addressbook.pop(nickname)
        elif answer == "no":
            pass
    else:
        print("Sorry,there is no this nickname in this addressbook.")


def list_all():
    times = 0
    for key in addressbook:
        times = times + 1
        print(str(times) + "     " + addressbook[key]["nickname"])
        print("      " + addressbook[key]["name"])
        print("      " + addressbook[key]["address"])
        print("      " + addressbook[key]["phone_no"] + "\n")


def main():
    print("""*** My	Contacts ***
   f –	find
   a –	add new entry
   d –	delete
   l –	list all
   q –	quit""")
    command = input("Command: ")
    if command == "f":
        find()
        main()
    elif command == "a":
        add()
        main()
    elif command == "d":
        delete()
        main()
    elif command == "l":
        list_all()
        main()
    elif command == "q":
        exit()


main()
