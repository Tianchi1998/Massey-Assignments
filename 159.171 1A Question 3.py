# The function below generates and prints the speech.
def generate_the_speech():
    print("""    Welcome to Best Man's Speech Generator!
    Please provide the following to help
    create a new speech""")
    user_name=input("Enter your name: ")
    grooms_name=input("Enter the grooms name: ")
    brides_name=input("Enter the brides name: ")
    number=int(input("Enter a number less than 10: "))
    age=int(input("Age you met the groom: "))
    where=input("Where did the bride and groom meet? ")
    descriptive_word_1=input("How would you describe the groom?")
    descriptive_word_2=input("How would you describe the bride?")
    animal=input("Name an animal: ")
# Next is the speech.
    content="""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Here is your speech %s:
Good evening everyone! For those who don't know me, I'm %s.
I met %s when we were %d. Right away, I knew he was a %s
kid and the perfect friend for me. He was always a hit with the
ladies even at the young age of %d. Then along came %s and
everything changed. It takes a %s girl to tame the %s that
is %s. I remember they met at %s and within the space
of %d minutes he was smitten! He told me way back then
"%s is the girl I'm going to marry" and here we are!
Ladies and gentlemen, I ask you to raise your glasses for %s and %s.
May they live happily ever after.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """%(user_name,user_name,grooms_name,age,descriptive_word_1,age,brides_name,descriptive_word_2,
     animal,grooms_name,where,number,brides_name,brides_name,grooms_name)
# Then we print it.
    print(content)

# Now we call the function.
generate_the_speech()
