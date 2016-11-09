from sys import exit


print "PIERWSZA ZMIANA"


def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    print "'1' = take honey"
    print "'2' = taunt bear"
    print "'3' = open door"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "1":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "2" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"
            print "'1' = take honey"
            print "'2' = taunt bear"
            print "'3' = open door"
            bear_moved = True
        elif choice == "2" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "3" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    print "'1' = left"
    print "'2' = right"

    choice = raw_input("> ")
    if choice == "1":
        bear_room()
    elif choice == "2":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve")


start()
