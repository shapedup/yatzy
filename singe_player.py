"""Single player version of Yatzy"""
from dice import D6
from hands import YatzyHand
from scoresheets import YatzyScoresheet
from scoresheets import Scoring


INTRO = """\nHello and welcome to my coded version of Yatzy!

Not to be confued with the well known 'Yahtzee', Yatzy is an open source game that plays very\n similar to it's cousin with a few differences.

The overall aim of the game is to score the highest possible points by rolling 5 die each turn\n and deciding which box is best to place your scores.

There are a total of 15 boxes and each one is scored in a different way. Be careful though! Once\n you have chosen which box to score, it is no longer available and you roll again to aim for a\n different box.

[NOT CURRENTLY AVAILABLE, YOU ONLY GET ONE THROW] To make things a bit easier for you (scrub),\n each time you roll the dice you can choose to save any number of them and roll the remaining. You\n can do this a whole two times if you want! How generous! Once all three rolls are up, you\n need to choose a box.

As you fill up the boxes with your scores it will get more and more difficult to score for an\n empty box, I'm afraid if you can't score for any of the open boxes, you score 0. Sad.

So! Scheme your way through to making the best score you can with the dice you have each turn!

Helpful hints:
It takes an average of 3 of each dice in the Upper Section to get a minimum score of 63 to get the 50 point bonus.
Just because you scored a full house doesn't mean the next time you score another one it's\n useless, you can go for scoring three of a kind or two pair or a pair or chance! Just remember,\n once you've scored for one box it's locked away!
"""

HELP = """You need help? Gosh, you really are a scrub... Fine, here's a list of commands (case sensitive):
    Rolling dice:
        > roll

    [NOT CURRENTLY IMPLEMENTED] Saving dice:
        > save(<dice_value>) = say you roll [2,4,5,6,6] type save(2,4,5,6) to save the 2, 4, 5, 6 and pray for a 3 to get the high straight

    Scoring (After submitting any of these inputs it is added to the relevant box)
    Upper Section scoring:
        >  ones => adds all the 1's
        >  twos => adds all the 2's
        >  threes => adds all the 3's
        >  fours => adds all the 4's
        >  fives => adds all the 5's
        >  sixes => adds all the 6's
    Remember! If you managed to get over 62 points in this section, you get a bonus 50!

    Lower Section scoring:
        >  pair => eg [1,3,3,4,4] = 8
        >  two pair => eg [2,2,5,5,5] = 14
        >  three oak => eg [1,4,4,4,4] = 12
        >  four oak => eg [4,5,5,5,5] = 20
        >  Lstraight => eg [1,2,3,4,5] = 15
        >  Hstraight => eg [2,3,4,5,6] = 20
        >  full => eg [2,2,3,3,3] = 13
        >  chance => eg [1,2,3,3,5] = 14
        >  YATZY! => scores 50 when you get 5 of any kind
    
    I can't imagine why on earth you would want to quit, but if you must:
        >  QUIT
    """
CONTROLS = YatzyScoresheet().scores().keys()
check = True

def help_quit(input):
    if input == "HELP":
        print(HELP)
    if input == "QUIT":
        print("I guess this was too hard for ya. It's okay. I get it.")
        check = False

print("Hello and welcome to my coded version of Yatzy!")
info = input("Would you like to learn about the game? (Y/N)\n>  ")
if info.upper() == "Y":
    print(INTRO)

print("Type 'HELP' at any time for a list of commands.")
while(check):
    cmd = input(">  ")
    help_quit(cmd)
    if cmd == "roll":
        hand = YatzyHand()
        print("Dice: ", hand)
        while(check):
            score = input(">  ")
            help_quit(score)
            if score in CONTROLS:
                print(YatzyScoresheet().scores())
                break
            else:
                print("Make sure to enter a valid control")


