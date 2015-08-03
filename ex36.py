from sys import exit

def living_room():
    print "This room has a very small dog in in."
    print "The dog blocking the door to the dining room."
    print "She has a ball in front of her."
    print "What do you do?"
    dog_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "pick up":
            dead("She hated that, and bit you!")
        elif choice == "hug and kiss" and not dog_moved:
            print "You're hugging & kissing the dog. She like that & allows you to enter."
            dog_moved = True
        elif choice == "throw ball" and dog_moved:
            dead("You have begun an endless game of fetch. You play for eternity.")
        elif choice == "enter room" and dog_moved:
            dining_room()
        else:
            print "I got no idea what that means."

def dining_room():
    print "You have entered a room of horrors!"
    print "There is Table, covered in mail!"
    print "You have to save Table! Do you sort his mail, or just leave it?"

    choice = raw_input("> ")

    if "sort" in choice:
        print "You spend 15 minutes sorting his mail."
        print "That's a lot of mail."
        print "......."
        print "Ok, all done. It's TV time!"
        tv()
    elif "leave" in choice:
        print "Bad choice."
        print "You leave the mail there."
        print "The mailman arries and brings more mail."
        print "Years pass, and the mail piles up forever."
        dead("Eventually, the mail buries you alive and you die.")
    else:
        dining_room()

def tv():
    print "You stretch and wander into the  TV room to have TV night."
    print "Just in time, you realize there is a big bad Mookers in here!"
    print "This Mookers is trying to swipe you! What do you do?"

    choice = raw_input("> ")

    if "boost" in choice:
        print "You give that Mooc a boost."
        print "He likes that fine."
        print "You watch TV together, 2 friends hanging out."
        print "Good job!"
        exit(0)
    else:
        dead("He doesn\'t like that!")

def dead(why):
    print why, "good job!"
    exit(0)

living_room()
