#this game takes place in a garden. You are in a labyrinth of hedges that open
#into different outdoor rooms. The goal is to reach a pond in the garden that
#contains a talking koi who will grant you 3 wishes. There are many
#ways to die, but when you die you'll just be overtaken by foliage and become
#a part of the garden yourself. The game will involve a runner that runs the
#various scenes in the labyrinth.

#death - death by foliage
#clearing - this is the starting point and you must make a fire for a torch to
    #help you see before you can move on.
#catcolony - this is where the main character unlocks the ability to communicate
    #with animals, through winning over Mookers, leader of the cat colony
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

class Scene(object):
    def enter(self):
        pass

class Runner(object):
    def __init__(self, scene_labyrinth):
        self.scene_labyrinth = scene_labyrinth

    def play(self):
        current_scene = self.scene_labyrinth.opening_scene()
        last_scene = self.scene_labyrinth.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_labyrinth.next_scene(next_scene_name)

            current_scene.enter()

class Death(object):

    def enter(self):
        print "You are dead. Oh no, that's the opposite of what you wanted to happen."
        print "Sorry about that, goodbye."
        exit(1)

class Clearing(object):

    def enter(self):
        print "You wake up in a clearing on a soft, mossy forest floor. It's winter,"
        print "but you seem to be immune to the cold. You stand up, look around, and"
        print "see that you're deep in an ancient forest, with silvery trees. You"
        print "don't know how you got here, but you know that your mission is to find"
        print "a wise koi living deep underwater and he will grant you 3 wishes.\n\n"
        print "Everything is very still. It is dusk. Next to you, there is an unlit torch"
        print "and a path into the darkness. Quick! Light the torch and begin your journey."
        print "It isn't safe here. Do you 'make fire with sticks' or 'make fire with rocks'"
        print "or 'make fire with eyeglasses'?"

        choice = raw_input("? ")

        if choice == "make fire with rocks":
            print "You pick up two rocks and begin trying to make fire with them. Has"
            print "literally anyone ever been able to do this?\n\nMinutes pass.\n\n"
            print "An hour passes. Your hands are rubbed raw."
            print "\n\nYou hear a rustling above, and glance up just in time to see a gigantic"
            print "bird (not sure what kind) swoop down and grab you in her massive talons.\n\n"
            print "You soar above the ancient forest, screaming, until she finally drops you."
            print "You free-fall for a hundred feet or so before you're abruptly caught in the beak"
            print "of a hungry baby bird. You are torn apart by its sharp beak, eaten alive.\n\n"
            return 'death'

        elif choice == "make fire with sticks":
            print "You grab two sticks and start rubbing them together as fast as you can."
            print "Slowly, the sticks begin to smoke, and finally they catch on fire. You"
            print "spend a few minute blowing on the flame, until the torch ignites. You"
            print "safely snuff out the starter sticks, stand up, and head down the dark"
            print "path, torch illuminating the way.\n\n"
            return 'cat_colony'

        elif choice == "make fire with eyeglasses":
            print "You build a small pile of leaves, then take off your eyeglasses and try to"
            print "catch the last rays of the fading evening light. You tilt your glasses"
            print "this way and that. Minutes pass, but the sun has set."
            print "Your pile of leaves is unchanged. Try something else!\n\n"
            return 'clearing'

        else:
            print "I don't understand what you're trying to do."
            return 'clearing'


class CatColony(object):

    def enter(self):
        print "The torch lights the way as you walk down the dark path. Suddenly, something"
        print "brushes your leg. You jump and nearly drop your torch; you see a few dozen"
        print "yellow eyes peering at you from out of the darkness -- You've wandered into"
        print "a cat colony.\n\n A big bad Mookers steps out of the darkness. 'You won't"
        print "be able to talk to the Koi because you are a person and he is a fish. But if"
        print "you can guess what number I'm thinking of, between 1-3, I will teach you how"
        print "to speak Koi.'\n\nThis is a surprise to you, because you didn't know that Mookers could talk to other"
        print "animals, but you go ahead and guess a number anyway."

        number = "%d" % (randint(1,3))
        print number
        choice = raw_input("> ")

        guess = 1

        while choice != int(number) and guess <= 3:
            guess += 1
            print "Guess again"
            choice = raw_input("> ")

        if guess <= 3 and choice == number:
            print "Mookers glances at you with apprehension, then says, 'Well, that's right."
            print "I will tell you the secret. He goes behind a tree and comes back with a"
            print "stack of dusty workbooks titled 'Learn Koi The Hard Way.' 'This will take"
            print "about 90 days, Mookers says.\n\n\nMonths pass. You have been surviving on"
            print "grubs, and dagnabbit, you learned Koi.\n\n'Go on,' that big fat Mookybear says."
            print "The pond is a long way away but you won't have any trouble finding it. Good luck!"
            return 'pond'
        else:
            print "That big bad Mookers grows impatient, and begins to growl his low cat"
            print "growl. Suddenly, he pulls back his wide, heavy Mooc paw and swipes at"
            print "you, knocking you over and killing you."
            return 'death'

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
        of these wishes. But I can grant you eternal life. I hope that's ok.
        You can either choose to live forever or die. Hm, which should it be,
        %r?'""" % (wish1, wish2, wish3, name)
        raw_input("> ")

        if raw_input == "die":
            print "So you've decided to die."
            return('death')
        elif raw_input == "live forever":
            print """With a boom and a flash of light, the koi disappears and you
            are left all alone at the bottom of the pond, which has gone from
            crystal-clear to murky and thick-feeling on your skin.\n\n"""
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
    'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Labyrinth.scene.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_labyrinth = Labyrinth('clearing')
a_game = Runner(a_labyrinth)
a_game.play()
