#Nested If Statements

# print("Please enter two words: ")
# words = input(">")

# print("Before .split() ->",words)

# words = words.split(" ")

# print("After .split() ->",words)

# if(words[0] == "two"):
#     print(words[0])
#     if(words[1] == "words"):
#         print(words[1])


print("You wake up in a dark forest.")
print("There is barely any light shining through the trees.")
print("You stumble around until you find a random remote.")
print()
print("Do you:")
print("1. Press the red button on the remote?")
print("2. Stay and try to survive.")
choice = input(">")

if(choice == "1"):
    print("You press the button and BOOM! Youve been teleported to some odd place. Its another forest but well lit. You got jumped at by a random squirrel, but it bounces off a random invisible ball around you, and runs off.")
    print("Do you:")
    print("1. Keep walking?")
    print("2. You stay and try to survive.")
    choice = input(">")

    if(choice == "1"):
        print("You walk down through the forest and suddenly you hear a LOUD explosion!") 
        print("You closed your eyes, and opened them back, as now the forest isnt much of a forest anymore, and more of a obstacle course.")
        print("But, you see a button at the end, and you have to get to it to get out of the forest.")
        print("Do you:")
        print("1. Run through the obstacles?")
        print("2. Run through the side, and try to cheat your way through.")
        choice = input(">")
    
    if(choice == "1"):
        print("You jump through, and successfully make it.") 
        print("Youve survived. And are back, having a normal life again.")
    


    if choice == "2":
        print("You walk along the edges, trying to get to the end.")
        print("you start to stumble until...")
        print("You fall, and are back at where you started, now just lost in a forest.")
        quit
    


if(choice == "2"):
    print("you try and survive, but there is no one here, you have barely any resources.")
    print("Do you:")
    print("1. Try and find food?")
    print("2. Try and find water.")
    choice = input(">")

    if choice == "1":
        print("You search for food, but to no resources.")
        print("You die from lack of hydration, as you have no water.")
        print("youre DEAD.")
    if(choice == "2"):
        print("You search for water and to no luck.")
        print("You die from not having any resources.")
        print("youre DEAD.")


        print("This game is basically about a dude going insane and thinking he has special powers but in reality doesnt.")