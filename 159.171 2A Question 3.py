stories = [['With bloody hands, I say good-bye.','Frank Miller'],
['TIME MACHINE REACHES FUTURE!!! ... nobody there ...','Harry Harrison'],
['The baby\'s blood type? Human, mostly.','Orson Scott Card'],
['For sale: baby shoes, never worn.','Ernest Hemingway'],
['Corpse parts missing. Doctor buys yacht.','Margaret Atwood'],
['We kissed. She melted. Mop please!','James Patrick Kelly'],
['Starlet sex scandal. Giant squid involved.','Margaret Atwood'],
['Will this do (lazy writer asked)?','Ken McLeod'],
["I'm sorry, but there's not enough air in here for everyone. I’ll tell them you were a hero.",'J. Matthew Zoss'],
['Waking Up To Silence: Deafening silence. I strain my ears, praying there might be someone else still alive. The only noise I hear are the voices in my head','Mike Jackson'],
["Not In My Job Description: Make sure it's done by the end of the day Jones.\nBut, sir, it's not in my ....\nJust do it, and remember, no blood.",'Mike Jackson'],
['Empty Baggage: The trunk arrived two days later. He lifted the lid and froze, it was empty. No arms, no legs, no head, nothing. Where was she?','Mike Jackson'],
['Forgot My Own Name: The hospital said it was concussion.\nMight be permanent memory loss.\nCan\'t even remember my own name - which is handy considering who I am.','Mike Jackson']
]

#This function finds the stories which contain a certain pattern.
def stories_certain_pattern():
    pattern = input("The pattern you want: ")
    for i in stories:
        if pattern in i[0]:
            print(i[0])

#This function finds the stories written by a certain author.
def stories_certain_author():
    author = input("The author you want: ")
    for i in stories:
        if author in i[1]:
            print(i[0])

#This function finds the stories which were written by a certain author and contain a certain word.
def stories_certain_author_certain_word():
    author = input("The author you want: ")
    key_word = input("The word: ")
    for i in stories:
        if key_word in i[0] and author in i[1]:
            print(i[0])

#Find the stories under a word limit.
def stories_less_than():
    fixed_number = int(input("The limit number you want: "))
    result = []    #To see if there is no story that meets our demand.
    for i in stories:
        list = i[0].split()
        if len(list) < fixed_number:
            print(i[0])
            result.append(i[0])
    if result == []:
        print("There is no story less than %d words." % (fixed_number))

#This function below displays all the stories.
def all_stories():
    for i in stories:
        author = i[1]
        print('"%s"'%(i[0]),"\n     -- %s"%(author))

#This function which uses all the functions defined above is the main function of this program.
def story_explorer():
    print("""*** Story Explorer ***
       p - find stories that contain a certain pattern
       a - find all stories by a certain author
       aw - find stories that a by a certain author and a contain a certain word
       n - find stories less than a certain number of words
       d - display all the stories
       q - quit""")
    command=input("command: ")
    if command == "p":
        stories_certain_pattern()
        story_explorer()
    elif command == "a":
        stories_certain_author()
        story_explorer()
    elif command == "aw":
        stories_certain_author_certain_word()
        story_explorer()
    elif command == "n":
        stories_less_than()
        story_explorer()
    elif command == "d":
        all_stories()
        story_explorer()
    elif command == "q":
        print()

#Now,we call the function.
story_explorer()
