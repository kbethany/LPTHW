#this game takes place in a garden. You are in a labyrinth of hedges that open
#into different outdoor rooms. The goal is to reach a pond in the garden that
#contains a talking koi who will grant you with eternal life. There are many
#ways to die, but when you die you'll just be overtaken by foliage and become
#a part of the garden yourself. The game will involve a runner that runs the
#various scenes in the labyrinth.

#death - death by foliage
#clearing - this is the starting point and you must make a fire for a torch to
    #help you see before you can move on.
#catcolony - this is where the main character unlocks the ability to communicate
    #with animals, through winning over the queen of the cat colony
#pond - this is where the character has to break the ice on the koi pond to
    #descend below, and pick up a scuba suit
#koimaster - this is where the character guesses a set of numbers to receive
    #eternal life from the koi
#surface - this is where the hero floats peacefully to the surface

#Labyrinth
#-next scene, opening scene
#Scene - contains the scenes
#Runner - Just contains 'play'

from sys import exit
from random import randint
from sys import argv

class Death(object):

    def death(self):
        print """You are dead. Oh no, that's the opposite of what you wanted to
        happen. Sorry about that, goodbye."""

class Clearing(object):

    def enter(self):
        print """You wake up in a clearing on a soft, mossy forest floor. It's
        winter, but you seem to be immune to the cold. You stand up, look around,
        and see that you're deep in an ancient forest, with silvery trees.
        You don't know how you got here, but you know that your mission is to find
        a wise koi living deep underwater and he will grant you eternal life.

        Everything is very still. It is dusk. Next to you, there is an unlit torch
        and a path into the darkness. Quick! Light the torch and begin your journey.
        It isn't safe here. Do you 'make fire with sticks' or 'make fire with rocks'
        or 'make fire with your eyeglasses'?"""

        fire = False

        raw_input = "? "
        choice = raw_input

        if choice == 'make fire with sticks':
            print """You grab two sticks and start rubbing them together as fast as
            you can. Slowly, the sticks begin to smoke, and finally they catch on
            fire. You spend a few minute blowing on the flame, until the torch
            ignites. You safely snuff out the starter sticks, stand up, and head
            down the dark path, torch illuminating the way."""
            fire = True
            return next.scene('catcolony')

        elif choice == 'make fire with rocks':
            print """You pick up two rocks and begin trying to make fire with them.
            Has literally anyone ever been able to do this?
            Minutes pass.
            An hour passes. Your hands are rubbed raw.
            You hear a rustling above, and glance up just in time to see a gigantic
            bird (not sure what kind) swoop down and grab you in her massive talons.

            You soar above the ancient forest, screaming, until she finally drops
            you. You free-fall for a hundred feet or so before you're abruptly
            caught in the beak of her hungry baby birds. You are torn apart by their
            sharp beaks, eaten alive."""
            return('death')

        elif choice == 'make fire with your eyeglasses':
            print """You build a small pile of leaves, then take off your
            eyeglasses and try to catch the last rays of the fading evening
            light. You tilt your glasses this way and that. Minutes pass, but
            the sun has set, your pile of leaves is unchanged. Try something
            else!"""
            return('clearing')

        else:
            print "I don't understand what you're trying to do."
            return('clearing')


class CatColony(object):

    def enter(self):
        print """The torch lights the way as you walk down the dark path. Suddenly,
        something soft brushes your leg. You jump and nearly drop your torch; you
        see a few dozen yellow eyes peering at you from out of the darkness --
        You've wandered into a cat colony.

        A big bad Mookers steps out of the darkness. "You won't be able to talk
        to the Koi because you are a person and he is a fish. But if you can
        guess what number I'm thinking of, between 1-3, I will teach you how
        to speak Koi.

        This is a surprise to you, because you didn't know that Mookers could
        talk to other animals, but you go ahead and guess a number anyway."""

        number = randint(1,3)
        raw_input("> ")
        choice = raw_input

        guess = 1

        if guess <= 2 and choice == int(number):
            print """Mookers glances at you with apprehension, then says, 'Well,
            that's right. I will tell you the secret. He goes behind a tree and
            comes back with a stack of dusty workbooks titled 'Learn Koi The
            Hard Way.' 'This will take about 90 days, Mookers says.\n\n\nMonths
            pass. You have been surviving on grubs, you dagnabbit, you learned
            Koi.\n\n'Go on,' that big fat Mookybear says. The pond is a long way
            away but you won't have any trouble finding it. Godspeed!"""
            return('pond')
        elif guess <= 2 and choice != int(number):
            guess += 1
            print "Guess again"
        else:
            print """That big bad Mookers grows impatient, and begins to growl
            his low cat growl. Suddenly, he pulls back his wide, thick Mooc paw
            and swipes at you, knocking you over and killing you."""
            return('death')

class Pond(object):

    def enter(self):
        print """You walk for miles, following the path ever deeper in the forest,
        until you come upon a pond, but the pond is frozen. There is some scuba
        gear nearby."""

        raw_input("> ")

        if "scuba" in raw_input:
            print """You pick up the scuba gear. Yay, now you won't drown.'\n\n
            The Koi lives underwater, so you'll have to break the ice to dive in.
            Do you 'jump up and down' on it, 'smash it with a rock', or 'wait
            for it to melt'?"""
            raw_input("> ")
            choice = raw_input
            if choice == "jump up and down":
                print """You carefully walk out to the middle of the pond. You're
                standing on transluscent ice, and you can see fish swimming
                beneath. You jump up and down. You hear a crack and suddenly,
                the ice splits beneath you, and with a scream you drop into the
                dark, icy water.\n\nRefreshing!!"""
                return('koi_master')
            elif choice == "smash it with a rock":
                print """You look for a big rock and start trying to smash the ice.
                You are barely making a dent in the ice. \n\nThis does not appear
                to be working."""
                return('pond')
            elif choice == "wait for it to melt":
                print """You decide to wait for the pond to thaw. You sit down
                on a log and wait patiently. Wow, you feel like you've been here
                for a long time! Your eyes droop. You may have fallen asleep.
                You wake with a start and realize you're constricted: You've
                become overgrown with trees and other foliage. This ancient,
                spooky forest is reclaiming you."""
                return('death')
            else:
                print "I don't understand what you're trying to do."
                return('pond')
        else:
            print "I don't understand what you want to do."


class KoiMaster(object):

    def enter(self):
        print """Unlike normal ponds, in this pond the water is completely clear,
        and you can see for miles in any direction. You're surrounded by koi
        lazily gliding around. In the distance you see a koi far bigger than the
        rest, bigger than you, bigger than a house. You swim over to him,
        thinking about what to say."""
        print """You come face-to-face with the big house-sized koi. Surprisingly,
        he has a soft voice. 'What is your name?', he asks."""
        raw_input("> ")
        name = raw_input
        print """Hello, %r. I am proud of you for making it to the bottom of
        my ice pond. I would like to grant you three wishes.""" % (name)
        print """What is your first wish?"""
        raw_input("> ")
        wish1 = raw_input
        print """The big koi grows very serious. 'Why, that's a heck of a wish to
        start with. %r, my gosh. You are really aiming high. Well, go ahead and
        tell me what your second wish is, %r.''""" % (wish1, name)
        raw_input("> ")
        wish2 = raw_input
        print """Whoa, wow wow wow. First that and now this.' He strokes his big
        koi whiskers and his bright orange and black scales shimmer in the water.
        'What is your third wish, then?'"""
        raw_input("> ")
        wish3 = raw_input
        print """'So if I understand you correctly,' the koi says patiently,
        'Your first wish is %r. \nYour second wish is %r.\nAnd your third wish
        is %r.\n. Unfortunately, even though I'd like to because tbh I'm pretty
        impressed with how you learned koi, I can't actually grant you any
        of these wishes. But I can grant you eternal life. Uh, I hope that's ok.
        You can either choose to live forever or die. Hm, which should it be,
        %r?'""" % (wish1, wish2, wish3, name)
        raw_input("> ")

        if raw_input == "die":
            return('death')
        elif raw_input == "live forever":
            return('surface')
        else:
            print "I don't understand what you're saying."
            raw_input("> ")

class Surface(object):

    def enter(self):
        print """Lungs burning and disoriented, you tilt your face toward the
        faint light, which you imagine must be the surface. You kick wildly,
        now knowing your error -- while you can live forever, you can also
        suffer forever, and if you don't make it to the surface soon you'll feel
        as if you're dying but never actually get the relief dying would bring!
        You kick and kick and with a splash, you break through to the surface."""
        return('finished')

class Finished(object):

    def finished(self):
        print "\nCongratulations!"

class Labyrinth(object):

    scene = {
    'clearing': Clearing(),
    'cat_colony': CatColony(),
    'pond': Pond(),
    'koi_master': KoiMaster(),
    'death': Death(),
    'finished': Finished(),
    }

Labyrinth('clearing')
