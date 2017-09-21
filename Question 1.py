# My Name : Tianchi Zhang Massey ID Number : 17139797
import random


def load():
    global Adjectives,Adverbs,Conjunctions,IntransitiveVerbs,Leadin,NounMarkers,Nouns,TransitiveVerbs
    global Adjectives_list,Adverbs_list,Conjunctions_list,IntransitiveVerbs_list,Leadin_list,NounMarkers_list,Nouns_list,TransitiveVerbs_list
    Adjectives = open("Adjectives.txt","r")
    Adverbs = open("Adverbs.txt","r")
    Conjunctions = open("Conjunctions.txt","r")
    IntransitiveVerbs = open("IntransitiveVerbs.txt","r")
    Leadin = open("Leadin.txt","r")
    NounMarkers = open("NounMarkers.txt","r")
    Nouns = open("Nouns.txt","r")
    TransitiveVerbs = open("TransitiveVerbs.txt","r")
    #Then,we create lists whose elements are lines in the file (without the \n).
    Adjectives_list = Adjectives.readlines()
    Adjectives_list = [i.strip() for i in Adjectives_list]
    Adverbs_list = Adverbs.readlines()
    Adverbs_list = [i.strip() for i in Adverbs_list]
    Conjunctions_list = Conjunctions.readlines()
    Conjunctions_list = [i.strip() for i in Conjunctions_list]
    IntransitiveVerbs_list = IntransitiveVerbs.readlines()
    IntransitiveVerbs_list = [i.strip() for i in IntransitiveVerbs_list]
    Leadin_list = Leadin.readlines()
    Leadin_list = [i.strip() for i in Leadin_list]
    NounMarkers_list = NounMarkers.readlines()
    NounMarkers_list = [i.strip() for i in NounMarkers_list]
    Nouns_list = Nouns.readlines()
    Nouns_list = [i.strip() for i in Nouns_list]
    TransitiveVerbs_list = TransitiveVerbs.readlines()
    TransitiveVerbs_list = [i.strip() for i in TransitiveVerbs_list]
    Adjectives = open("Adjectives.txt", "r")
    Adverbs = open("Adverbs.txt", "r")
    Conjunctions = open("Conjunctions.txt", "r")
    IntransitiveVerbs = open("IntransitiveVerbs.txt", "r")
    Leadin = open("Leadin.txt", "r")
    NounMarkers = open("NounMarkers.txt", "r")
    Nouns = open("Nouns.txt", "r")
    TransitiveVerbs = open("TransitiveVerbs.txt", "r")


def exam():
    adj_line = Adjectives.readline()
    adv_line = Adverbs.readline()
    conj_line = Conjunctions.readline()
    IntransitiveVerbs_line = IntransitiveVerbs.readline()
    Leadin_line = Leadin.readline()
    NounMarkers_line =  NounMarkers.readline()
    Nouns_line = Nouns.readline()
    TransitiveVerbs_line = TransitiveVerbs.readline()
    print(adj_line,end="")
    print(adv_line,end="")
    print(conj_line,end="")
    print(IntransitiveVerbs_line,end="")
    print(Leadin_line,end="")
    print(NounMarkers_line,end="")
    print(Nouns_line,end="")
    print(TransitiveVerbs_line,end="")


def easy_sentence():
    random_Noun = random.choice(Nouns_list)       # The Nouns_list is defined in the first function.
    random_IntransitiveVerb = random.choice(IntransitiveVerbs_list)
    string = random_Noun + " " + random_IntransitiveVerb + "."
    string = string.capitalize()
    print(string)


def noun_phrase():
    noun_marker = random.choice(NounMarkers_list)
    string = noun_marker + " "
    index = random.choice(["0", "1"])     #To make things happen 50% of the time.
    if index == "0":
        adj = random.choice(Adjectives_list)
        string = string + adj + " "
    noun = random.choice(Nouns_list)
    string = string + noun
    return string


def verb_phrase():
    index = random.choice(["0","1"])
    if index == "0":
        intransitive_verb = random.choice(IntransitiveVerbs_list)
        string = intransitive_verb + " "
    else:
        transitive_verb = random.choice(TransitiveVerbs_list)
        string = transitive_verb + " "
    Noun_phrase = noun_phrase()       #To call the noun_phrase function.
    string = string + Noun_phrase + " "
    return string


def sentence():
    string = ""
    index1 = random.choice(["0","1"])
    if index1 == "0":
        lead_in = random.choice(Leadin_list)
        string = string + lead_in + " "
    Noun_phrase = noun_phrase()        #Call the noun_phrase function.
    string = string + Noun_phrase + " "
    index2 = random.choice(["0","1"])
    if index2 == "0":
        adv = random.choice(Adverbs_list)
        string = string + adv + " "
    Verb_phrase = verb_phrase()        #Call the verb_phrase function.
    string = string + Verb_phrase + "."
    string = string.capitalize()
    return string


def main():
    print("""          ***Random Sentence Generator***
    L(l) - Load all the files of words from disk.
    T(t) - display the first word from each list to make sure they've been loaded.
    E(e) - display a two word sentence.
    S(s) - generate & display a sentence
    Q(q) - Quit the program.""")
    command = input("Your command is: ")
    if command == 'L' or command == 'l':
        load()
        main()
    elif command == "T" or command == "t":
        exam()
        main()
    elif command == "E" or command == "e":
        easy_sentence()
        main()
    elif command == "S" or command == "s":
        #Statements below are to remind user when files were not loaded.
        try:
            Sentence = sentence()    #Call the sentence function.
            print(Sentence)
        except:
            print("Sorry,wordlists haven't been loaded.")
            main()
        main()
    elif command == "Q" or command == "q":
        # Close files and exit the program.
        Adjectives.close()
        Adverbs.close()
        Conjunctions.close()
        IntransitiveVerbs.close()
        Leadin.close()
        NounMarkers.close()
        Nouns.close()
        TransitiveVerbs.close()
        exit()


# Now , we call the main function.
main()