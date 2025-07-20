def main():
    print(">> Setting 1 <<")
    print("--Your mother hands you a basket of warm soup, bread, and jam--\n")
    print("Mother says: “Go straight to Grandma’s house. Don’t talk to strangers. Stay on the safe path.”")
    print("You tie your red cloak and head on your way...\n")
    print(">> Moving to Setting 2 <<")

    
    choices = input("Choice 1: Which path will you take? \n" \
    "A. The safe path — A long, clear trail where you often walk \n" \
    "B. The secret shortcut — A narrow, winding trail you found once before.").lower().strip()
    
    if choices == 'a':
        print("You walk peacefully. Birds sing. You stop to pick some wildflowers for Grandma \n\
               Suddenly, a large gray wolf steps out from behind a tree \n \
               Wolf says: “Good day, little girl. Where are you off to with that basket?”")
        
    elif choices == 'b':
        print('The shortcut is tricky. You slip once, but you keep going. \n\
                Suddenly, a gray wolf jumps out from a bush. \n\
                Wolf says: “Hello, traveler. What’s in the basket?”')    
        
    print(">> Moving to Setting 3 <<")

    choice = input("Choice 2: What do you tell the wolf? \n\
            A. “I’m going to Grandma’s house in the woods.” \n\
            B. “It’s none of your business.”")

    if choice == "a":
        print("The wolf smiles slyly. \n\
            “How sweet. I hope your Grandma enjoys the visit.” \n\
            He turns and disappears into the trees.\n \
            He now rushes ahead to Grandma’s house!")

    elif choice == "b":
        print ("The wolf frowns but doesn’t stop you.\n\
            He walks away slowly, watching you.\n\
            (You may get ahead of him!)\n\
            When you reach Grandma’s house:\n\
            The door is slightly open. The fire is out. It’s very quiet.")
    
    print(">> Moving to Setting 4 <<")

    choicee= input("Choice 3: What do you do?\n\
                    A. Go inside quietly.\n\
                    B. Call out for Grandma from outside.").lower().strip()
    
    if choicee == "a": 
        print("You see “Grandma” in bed, but something looks odd...\n\
        “What big eyes you have…\n”\
        “The better to see you with.\n”\
        (You’re face to face with the wolf!)\n")
        choicee1= input ("1.fight the wolf\n \
                        2. Run away")
        if choicee1 == "1":
            print("LITTLE RED FOUND A GRENADE!!\n SHE THEN THREW IT AT THE WOLF AND EVERYTHING EXPLODED....\n the grandmother woke up and saw little red with the goods from her grandchild\n\n The End")
        elif choicee1 == "2":
            print("Little Red Ran Away, the grandmother woke up and saw little red with the goods from her grandchild\n\n The End")

    if choicee == "b":
        print("No answer. You peek in and notice muddy paw prints. You stay outside.\
                Suddenly, you see a woodcutter nearby!\n The woodcutter saves them\n\n The End")
        
main()
    
