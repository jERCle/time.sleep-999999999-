import random
import time
import shutil

health = 20
knightHealth = 10
knightAttack = 2
count = 1  # While loop within startRoom()
columns = shutil.get_terminal_size().columns  # Centered headers.


def attack():
    # Global variables, values can be used anywhere in the program.
    global health
    global knightHealth
    global knightAttack
    health = health - knightAttack


def startRoom():
    time.sleep(2)
    print("You've just slain the King, your sword shatterns inside of his limp corpse and his knights attack!")
    time.sleep(2)
    attack()
    print("You have", health, "points left")
    time.sleep(2)
    print("The knight attacks you!")
    time.sleep(2)
    attack()
    print("You have", health, "points left")


def secondRoom():
    print("Suddenly while holding your swords hilt a second knight appears!")
    time.sleep(2)
    attack()
    time.sleep(2)
    print("You can feel your life slipping away")
    time.sleep(2)
    print("You have", health, "points left")
    time.sleep(2)
    print("The knight attacks again! while the second laughs and watches amused")
    time.sleep(3)
    attack()
    print("You have", health, "points left")
    time.sleep(2)
    print("HEEEEEYAAAAA-H! A knight weilding a shovel comes in swinging!")
    time.sleep(3.5)
    print("FUCK THESE CUUUUUUUUUUUUUUUUNTS!!!!! -shovels out the throat of the first-")
    time.sleep(3.5)
    print("-laughs as he decapitates the second leaving you emotionless-")
    time.sleep(3.5)
    print("Get up you useless cunt -he begrudgingly insists- ")
    time.sleep(2)
    MAIN = input('-While groveling on the floor- Uhh, My names ')
    time.sleep(2)
    print("I don't give a fucking shit, get the fuck up you useless fuck head")
    time.sleep(2.5)
    print("...")
    time.sleep(1.5)
    print("Ugh " + MAIN + " listen here mate.")
    time.sleep(2)
    print("I only saved you because I thought you were someone else, but I uhhh, I know")
    time.sleep(3)
    print("that you're not him, so i'm just going to be on my way mate.")
    time.sleep(3)


def displayIntro():  # The Define Functions do nothing, until called upon below.
    print("-1455 AD-".center(columns))
    time.sleep(2.5)
    print("____Here we go!____".center(columns))
    time.sleep(2.5)


displayIntro()
startRoom()
secondRoom()
