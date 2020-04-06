import textwrap
import sys
import os
import time
import random


screen_width = 300

##### Title Screen #####
def game_logo():
    print("####################################################################")
    print("#       /\         /\               /\         /\ __         /\    #")
    print("#      /  \      ~~~~~~TEXT RPG~~~~~~ \       /  | ||       /  \   #")
    print("#     /   _\____/______\__________/____\_____/___| ||_ _ _ /__ _\  #")
    print("# ---/-- /_____________________________________||\  \I \ /\ /\ /|\-#")    
    print("#   /    \_____________________________________||/  /I_/_\/_\/_\|  #")
    print("#  /            \           \                    | ||    \         #")
    print("#    ---------------------------------------     |_|| ---------    #")
    print("#                                                                  #")
    print("#______________________© 2020, Albert Salomo. All rights reserved. #")
    print('#___________________________Play___________________________________#')
    print('#___________________________Help___________________________________#')
    print('#___________________________Quit___________________________________#')
    print('####################################################################')

def tittle_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        os.system('cls')
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        print("===========================================")
        print("          Thanks For Playing :)            ")
        print("Type tittle_screen() to play the game again")
        print("===========================================")
        sys.exit()
    while option.lower() not in ['play' , 'help' , 'quit']:
        print("Please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            os.system('cls')
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            print("===========================================")
            print("         Thanks For Playing :)             ")
            print("Type tittle_screen() to play the game again")
            print("===========================================")
            sys.exit()

def tittle_screen():
    os.system('cls')
    game_logo()
    tittle_screen_selection()

def help_menu():
    print('=============== HELP ===================')
    print('= Type the command to execute them     =')
    print('= Use "move" command to move           =')
    print('= Use "look" to search something       =')
    print('= Use "battle" to fight with a monster =')
    print('========================================')
    tittle_screen_selection()
    
##### Player Setup #####
class player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mana = 0
        self.atk = 0
        self.exp = 0
        self.level = 1
        self.gold = 0
        self.skill = ''
        self.location = 'Starting Point'
        self.game_over = False
        self.item = ''
myPlayer = player()


    

##### LEVEL SYSTEM #####

def desc_level_up():
    if myPlayer.exp >=1 and myPlayer.exp < 2:
        level_up_2()
        myPlayer.level = 2
    elif myPlayer.exp >=20 and myPlayer.exp < 21:
        level_up_3()
        myPlayer.level = 3
    elif myPlayer.exp >=100 and myPlayer.exp < 101:
        level_up_4()
        myPlayer.level = 4
    elif myPlayer.exp >=200 and myPlayer.exp < 201:
        level_up_5()
        myPlayer.level = 5
    elif myPlayer.exp >=450 and myPlayer.exp < 451:
        level_up_6()
        myPlayer.level = 6
    elif myPlayer.exp >=1000 and myPlayer.exp < 1001:
        level_up_7()
        myPlayer.level = 7
    elif myPlayer.exp >=3000 and myPlayer.exp < 3001:
        level_up_8()
        myPlayer.level = 8
    elif myPlayer.exp >=5000 and myPlayer.exp < 5001:
        level_up_9()
        myPlayer.level = 9
     
def level_up_2():
    print("You are now level 2 !")
    myPlayer.hp = myPlayer.hp + 10
def level_up_3():
    print("You are now level 3 !")
    myPlayer.hp = myPlayer.hp + 10
def level_up_4():
    print("You are now level 4 !")
    myPlayer.hp = myPlayer.hp + 10
def level_up_5():
    print("You are now level 5 !")
    myPlayer.hp = myPlayer.hp + 10
def level_up_6():
    print("You are now level 6 !")
    myPlayer.hp = myPlayer.hp + 10
def level_up_7():
    print("You are now level 7 !")
    myPlayer.hp = myPlayer.hp + 10
def level_up_8():
    print("You are now level 8 !")
    myPlayer.hp = myPlayer.hp + 10
def level_up_9():
    print("You are now level 9 !")
    myPlayer.hp = myPlayer.hp + 10


        
ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = 'up' 
DOWN = 'down'
LEFT = 'left' 
RIGHT = 'right'

solved_places = {'a1' : False, 'a2' : False, 'a3':False, 'a4': False,
                 'b1' : False, 'b2' : False, 'b3':False, 'b4': False,
                 'c1' : False, 'c2' : False, 'c3':False, 'c4': False,
                 'd1' : False, 'd2' : False, 'd3':False, 'd4': False,
                 }

zonemap = {
    'Nothing' : {
        },
    'Starting Point' : {
        ZONENAME : "Starting Point",
        DESCRIPTION : "Wellcome to this world !",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'd1',
        DOWN : 'b1',
        LEFT : 'a4',
        RIGHT : 'Telesia',
        },
    'Telesia' : {
        ZONENAME : "This is your home",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'd2',
        DOWN : 'b2',
        LEFT : 'Starting Point',
        RIGHT : 'Spider Forest',
        },
    'Spider Forest' : {
        ZONENAME : "",
        DESCRIPTION :"description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'd3',
        DOWN : 'b3',
        LEFT : 'Telesia',
        RIGHT : 'a4',
        },
    'a4' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'd4',
        DOWN : 'b4',
        LEFT : 'Spider Forest',
        RIGHT : 'Starting Point',
        },
    'b1' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'Starting Point',
        DOWN : 'c1',
        LEFT : 'b4',
        RIGHT : 'b2',
        },
    'b2' : {
        ZONENAME : "Home",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'a2',
        DOWN : 'c2',
        LEFT : 'b1',
        RIGHT : 'b3',
        },
    'b3' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'a3',
        DOWN : 'c3',
        LEFT : 'b2',
        RIGHT : 'b4',
        },
    'b4' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'a4',
        DOWN : 'c4',
        LEFT : 'b3',
        RIGHT : 'b1',
        },
    'c1' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'b1',
        DOWN : 'd1',
        LEFT : 'c4',
        RIGHT : 'c2',
        },
    'c2' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'b2',
        DOWN : 'd2',
        LEFT : 'c1',
        RIGHT : 'c3',
        },
    'c3' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'b3',
        DOWN : 'd3',
        LEFT : 'c2',
        RIGHT : 'c4',
        },
    'c4' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'b4',
        DOWN : 'd4',
        LEFT : 'c3',
        RIGHT : 'c1',
        },
    'd1' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'c1',
        DOWN : 'Starting Point',
        LEFT : 'd4',
        RIGHT : 'd2',
        },
    'd2' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'c2',
        DOWN : 'a2',
        LEFT : 'd1',
        RIGHT : 'd3',
        },
    'd3' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'c3',
        DOWN : 'Spider Forest',
        LEFT : 'd2',
        RIGHT : 'd4',
        },
    'd4' : {
        ZONENAME : "",
        DESCRIPTION : "description",
        EXAMINATION : "examine",
        SOLVED : False,
        UP : 'c4',
        DOWN : 'a4',
        LEFT : 'd3',
        RIGHT : 'd1',
        },
}
###### GAME START #######
#def print_location():
 #   print('\n' + ('#' + (4 + len(myPlayer.location))))
  #  print('#' + myplayer.location + ' #')
   # print('#' + zonemap[myPlayer.location.upper][DESCRIPTION] + ' #')
    #print('\n' + ('#' + (4 + len(myPlayer.location))))

def map_overview():
    os.system('cls')
    print("         =============THE MAP============     ")
    print("         d1         d2        d3        d4    ")
    print("         ^           ^        ^         ^     ")
    print("     #########################################")
    print("     #         #         #         #         #")
    print("     #         #         #         #         #")
    print("     # Starting# Telesia # Spider  #    a4   #")
    print("     #   Point #         # Forest  #         #")
    print("     #         #         #         #         #")
    print("     #########################################")
    print("     #########################################")
    print("     #         #         #         #         #")
    print("     #         #         #         #         #")
    print("     #   b1    #    b2   #    b3   #    b4   #")
    print("     #         #         #         #         #")
    print("     #         #         #         #         #")
    print("     #########################################")
    print("     #########################################")
    print("     #         #         #         #         #")
    print("     #         #         #         #         #")
    print("     #   c1    #    c2   #    c3   #    c4   #")
    print("     #         #         #         #         #")
    print("     #         #         #         #         #")
    print("     #########################################")
    print("     #########################################")
    print("     #         #         #         #         #")
    print("     #         #         #         #         #")
    print("     #   d1    #    d2   #    d3   #    d4   #")
    print("     #         #         #         #         #")
    print("     #         #         #         #         #")
    print("     #########################################")
    print("          v         v         v         v     ")
    print("      Starting     a2         a3        a4    ")
    print("        Point                               \n")
    print("You are on the " + myPlayer.location + "....\n")



            
######## COMMAND IN MAP (SAFRZONE) ##########
def safezone():
    print("================"+myPlayer.location+"=================")
    print("What would you like to do?")
    print("Type 'help' to show the action list")
    action = input("> ")
    acceptable_actions = ['move', 'quit', 'look' , 'map', 'battle' , 'help']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
        print("===========================================")
        print("         Thanks For Playing :)             ")
        print("Type tittle_screen() to play the game again")
        print("===========================================")
    elif action.lower() == 'move':
        os.system('cls')
        player_move(action.lower())
    elif action.lower() == 'look':
        player_look(action.lower())
    elif action.lower() == 'map':
        map_overview()
        input("Type anything to continue......\n> ")
        os.system('cls')
    elif action.lower() == 'help':
        help_action()
    elif action.lower() == 'battle':
        safezone_text = "You can't battle here... , this is a safezone"
        for character in safezone_text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        input("\nType anything to continue......\n> ")
        os.system('cls')

        
######### COMMAND IN BATTLE MAP ###########       
def prompt():
    acceptable_actions = ['move', 'quit', 'look' , 'battle', 'map', 'help']
    print("================"+myPlayer.location+"=================")
    print("What would you like to do?")
    print("Type 'help' to show the action list")
    action = input("> ")
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
        print("===========================================")
        print("         Thanks For Playing :)             ")
        print("Type tittle_screen() to play the game again")
        print("===========================================")
    elif action.lower() == 'move':
        player_move(action.lower())
        os.system('cls')
        if zonemap == 'Starting Point':
            safezone()
        else :
            prompt()
            monster_1_spawn_chance()
    elif action.lower() == 'look':
        player_look(action.lower())
        monster_1_spawn_chance()
    elif action.lower() == 'map':
        map_overview()
        input("Type anything to continue......\n> ")
        os.system('cls')
    elif action.lower() == 'help':
        help_action()
    elif action.lower() == 'battle':
        random.seed(random.randint(1,100))
        a = random.randint(1,100)
        #### SPIDER FOREST ####
        if myPlayer.location == 'Spider Forest':
            random.seed(random.randint(1,100))
            a = random.randint(67,100)
            if a > 0 and a <=33 :
                os.system('cls')
                player_battle_monster1(action.lower())
                os.system('cls')
            elif a > 33 and a <=66 :
                os.system('cls')
                player_battle_monster2(action.lower())
                os.system('cls')
            elif a>66: 
                os.system('cls')
                player_battle_monster3(action.lower())
                os.system('cls')
            else :
                print("There is no monster ")
        else :
            random.seed(random.randint(1,100))
            a = random.randint(1,100)
            if a > 0 and a <=33 :
                os.system('cls')
                player_battle_monster1(action.lower())
                os.system('cls')
            elif a > 33 and a <=66 :
                os.system('cls')
                player_battle_monster2(action.lower())
                os.system('cls')
            elif a>66: 
                os.system('cls')
                player_battle_monster3(action.lower())
                os.system('cls')
            else :
                print("There is no monster ")            


####### HELP ACTION ########            
def help_action():
    print("============-------HELP-------==============")
    print("= MOVE = To move to the another area       =")
    print("= LOOK = To examine the area               =")
    print("= MAP = To show you the map                =")
    print("= QUIT = To exit the game                  =")
    print("= BATTLE = To battle with a monster        =")
    print("============================================")
    input("\nType anything to continue.......\n> ")
    os.system('cls')


###### MOVE OPTION ########    
def player_move(action):
    a = True
    while a == True:
        ask = "You are in ~" + myPlayer.location  + "~ now....\n"
        upper_text = "Where you like to move to\n=============================\n"
        up_text = "=      UP = " + zonemap[myPlayer.location][UP] 
        left_text = "\n=      LEFT = " + zonemap[myPlayer.location][LEFT] 
        right_text = "\n=      RIGHT = " + zonemap[myPlayer.location][RIGHT] 
        down_text = "\n=      DOWN = " + zonemap[myPlayer.location][DOWN]
        closed_text = "\n=============================\n"
        back_text = "<- BACK\n\n> " 
        dest = input(ask + upper_text + up_text + left_text + right_text + down_text + closed_text + back_text )
        if dest.lower() == 'up':
            destination = zonemap[myPlayer.location][UP]
            movement_handler(destination)
            if destination == 'Starting Point' :
                a = False
                safezone()
            else :
                a = False
                prompt()
        elif dest.lower() == 'left':
            destination = zonemap[myPlayer.location][LEFT]
            movement_handler(destination)
            if destination == 'Starting Point' :
                a = False
                safezone()
            else :
                a = False
                prompt()
        elif dest.lower() == 'right':
            destination = zonemap[myPlayer.location][RIGHT]
            movement_handler(destination)
            if destination == 'Starting Point' :
                a = False
                safezone()
            else :
                a = False
                prompt()                        
        elif dest.lower() == 'down':
            destination = zonemap[myPlayer.location][DOWN]
            movement_handler(destination)
            if destination == 'Starting Point' :
                a = False
                safezone()
            else :
                a = False
                prompt()
        elif dest.lower() == 'back':
            os.system('cls')
            a = False

        else :
            print("Invalid Command !,\nType up,left,down,right to move\n")
            os.system('cls')
            a = True
###### INVENTORY #####
  
        
###### MOVE EXECUTION #####

def movement_handler(destination):
    os.system('cls')
    print("\n" + "You have move to the " + destination + ".")
    myPlayer.location = destination

##### LOOK ACTION #####

def player_look(action):
    if myPlayer.location == 'Starting Point':
        a = "There is nothing to look in this place.....\n"
        for character in a :
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)   
        input("Type anything to continue.......\n> ") 
        os.system('cls')
    elif myPlayer.location == 'Telesia':
        b = "I think i smell something....., oh i'm forgot i can't smell ._.\n"
        for character in b :
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        os.system('cls')
    elif myPlayer.location == 'Spider Forest':
        c ="I think i heard something......... ?"
        for character in c :
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        os.system('cls')


#### SPAWN CHANCE ####
            
def monster_1_spawn_chance():
    random.seed(random.randint(1,100))
    monster_spawn = random.randint(1,100) 
    action = 'battle'
    if action.lower() == 'battle' :
        if monster_spawn >= 80 and monster_spawn<=100:
            print("A monster suddenly approach....!")
            player_battle_monster1(action)


#### NPC ####



#### MONSTER ####
            
class slime:
    def __init__(self):
        random.seed(random.randint(1,10))
        self.name = "Slime"
        self.hp = 20
        self.atk = 2
        self.exp = random.randint(1,10)
        self.mana = 1
        self.gold = random.randint(1,10)
monster1 = slime()

class skeleton:
    def __init__(self):
        random.seed(random.randint(1,10))
        self.name = "Skeleton"
        self.hp = 30
        self.atk = 4
        self.exp = random.randint(1,10)
        self.mana = 1
        self.gold = random.randint(1,10)
monster2 = skeleton()

class spider:
    def __init__(self):
        random.seed(random.randint(1,10))
        self.name = "Spider"
        self.hp = 22
        self.atk = 5
        self.exp =  random.randint(1,10)
        self.mana = 2
        self.gold = random.randint(1,10)
monster3 = spider()

#### BATTLE EXECUTION ####


######SLIME###### 
def player_battle_monster1(action):
    slimeimage()
    monster_speech1 = "You have met a slime.......\n"
    for character in monster_speech1 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    battle_arguments = True
    while battle_arguments == True: 
        print("-------------------------------")
        print(" FIGHT | RUN | ITEM | EXAMINE |")
        print("-------------------------------")
        battle_option = {'fight', 'run', 'item', 'examine'}
        battle_action = input("What would you like to do ? >")
        while battle_action.lower() not in battle_option:
            print("Unknown action, try again. \n")
            battle_action = input("What would you like to do ? >")
        if battle_action.lower() == 'run':
            print('You have successfully escaped from the monster')
            battle_arguments = False
        if battle_action.lower() == 'item':
            print("You don't have any item yet")
            battle_arguments = True
        if battle_action.lower() == 'examine':
            print(" Monster name : Slime")
            print(" Difficulty : Easy")
            print(" Hp = " + str(monster1.hp))
            print(" Mana = 1")
            battle_arguments = True
        elif battle_action.lower() == 'fight':
            monster1.hp = monster1.hp - myPlayer.atk
            myPlayer.hp = myPlayer.hp - monster1.atk
            if myPlayer.hp <=0:
                myPlayer.hp = 0
            print("Your hp now " + str(myPlayer.hp))
            if monster1.hp < 0:
                monster1.hp = 0
            print(str(monster1.name) + " hp now " + str(monster1.hp))
            if monster1.hp <= 0:
                slimeimage_dead()
                print("You've won the battle......")
                print("You gain " + str(monster1.exp) + " exp")
                print("You gain " + str(monster1.gold) + " gold")
                myPlayer.exp = myPlayer.exp + monster1.exp
                myPlayer.gold = myPlayer.gold + monster1.gold
                input("Type anything to continue......\n> ")
                os.system('cls')
                battle_arguments = False
            elif myPlayer.hp <= 0:
                battle_arguments = False
                gameover_text()
            else : 
                battle_arguments = True
    monster1.hp = 20
    desc_level_up()

def slimeimage():
    print("   UuUuUuUuUu")
    print('  U          U ')
    print(" U  o       o U")
    print(' U      ---    U ')
    print(" UuUuUuUuUuUuUuU")
    
def slimeimage_dead():
    print("   UuUuUuUuUu")
    print('  U          U ')
    print(" U  X       X U")
    print(' U      ---    U ')
    print(" UuUuUuUuUuUuUuU")
    
                ###### SKELETON ######
def player_battle_monster2(action):
    skeletonimage()
    monster_speech1 = "You have met a skeleton.......\n"
    for character in monster_speech1 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    battle_arguments = True
    while battle_arguments == True: 
        print("-------------------------------")
        print(" FIGHT | RUN | ITEM | EXAMINE |")
        print("-------------------------------")
        battle_option = {'fight', 'run', 'item', 'examine'}
        battle_action = input("What would you like to do ? >")
        while battle_action.lower() not in battle_option:
            print("Unknown action, try again. \n")
            battle_action = input("What would you like to do ? >")
        if battle_action.lower() == 'run':
            print('You have successfully escaped from the monster')
            battle_arguments = False
        if battle_action.lower() == 'examine':
            print(" Monster name : Skeleton")
            print(" Difficulty : Easy")
            print(" Hp = " + str(monster2.hp))
            print(" Mana = 1")
            battle_arguments = True
        elif battle_action.lower() == 'fight':
            monster2.hp = monster2.hp - myPlayer.atk
            myPlayer.hp = myPlayer.hp - monster2.atk
            if myPlayer.hp <=0:
                myPlayer.hp = 0
            print("Your hp now " + str(myPlayer.hp))
            if monster2.hp < 0:
                monster2.hp = 0
            print(str(monster2.name)+ " hp now " + str(monster2.hp))
            if monster2.hp <= 0:
                skeletonimage_dead()
                print("You've won the battle......")
                print("You gain " + str(monster2.exp) + " exp")
                print("You gain " + str(monster2.gold) + " gold")
                myPlayer.exp = myPlayer.exp + monster2.exp
                myPlayer.gold = myPlayer.gold + monster2.gold
                input("Type anything to continue......\n> ")
                os.system('cls')
                battle_arguments = False
            elif myPlayer.hp <= 0:
                battle_arguments = False
                gameover_text()
            else : 
                battle_arguments = True
    monster2.hp = 25
    desc_level_up()
  

def skeletonimage():
    print("    __________")
    print("  /            \ ")
    print(" /              \ ")
    print("/                \ ")
    print("|   _      _     |")
    print("|  |_|    |_|    | ")
    print(" \             _/ ")
    print("  |___________|")
    print("   |_|_|_|_|_|")
    print("   |_|_|_|_|_|")
    print("   \_________/")  
           
def skeletonimage_dead():
    print("    __________ ")
    print("  /            \ ")
    print(" /              \ ")
    print("/                \ ")
    print("|                |")
    print("|   \/    \/     | ")
    print(" \  /\    /\   _/ ")
    print("  |___________|")
    print("   |_|_|_|_|_|")
    print("   |_|_|_|_|_|")
    print("   \_________/")



            ####### SPIDER #######
def player_battle_monster3(action):
    spiderimage()
    monster_speech1 = "You have met a spider.......\n"
    for character in monster_speech1 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    battle_arguments = True
    while battle_arguments == True: 
        print("-------------------------------")
        print(" FIGHT | RUN | ITEM | EXAMINE |")
        print("-------------------------------")
        battle_option = {'fight', 'run', 'item', 'examine'}
        battle_action = input("What would you like to do ? >")
        while battle_action.lower() not in battle_option:
            print("Unknown action, try again. \n")
            battle_action = input("What would you like to do ? >")
        if battle_action.lower() == 'run':
            print('You have successfully escaped from the monster')
            battle_arguments = False
        if battle_action.lower() == 'examine':
            print(" Monster name : Spider")
            print(" Difficulty : Easy")
            print(" Hp = " + str(monster3.hp))
            print(" Mana = 1")
            battle_arguments = True
        elif battle_action.lower() == 'fight':
            monster3.hp = monster3.hp - myPlayer.atk
            myPlayer.hp = myPlayer.hp - monster3.atk
            if myPlayer.hp <=0:
                myPlayer.hp = 0
            print("Your hp now " + str(myPlayer.hp))
            if monster3.hp < 0:
                monster3.hp = 0
            print(str(monster3.name)+ " hp now " + str(monster3.hp))
            if monster3.hp <= 0:
                spiderimage_dead()
                print("You've won the battle......")
                print("You gain " + str(monster3.exp) + " exp")
                print("You gain " + str(monster3.gold) + " gold")
                myPlayer.exp = myPlayer.exp + monster3.exp
                myPlayer.gold = myPlayer.gold + monster3.gold
                input("Type anything to continue......\n> ")
                os.system('cls')
                battle_arguments = False
            elif myPlayer.hp <= 0:
                battle_arguments = False
                gameover_text()
            else :  
                battle_arguments = True
    monster3.hp = 11
    desc_level_up()

def spiderimage():
    print("            ______________                   ")
    print("       __  /--------------\                  ")
    print("      /  \/                \  ___            ")
    print("     /_/\/-----------------|/ __ \           ")
    print("    // \|              /\  | /\ \ \          ")
    print("   |/ /\|-------------/  \ |/  \ \ \         ")
    print("   / /  |   _____    / /\ \ \/\ \ \ \        ")
    print("  / / /\ \ /       \/ /__\ \/  \ \ \ \       ")
    print(" | / |  \_|        |_/    \ \   \ \ \ |      ")
    print(" |_| |    |o O O o |       \ \   | ||_|      ")
    print("   | |_   \________/       _\ \  |_|         ")
    print("   |__|   |_     _|        |__|              ")

def spiderimage_dead():
    print("            ______________                   ")
    print("       __  /--------------\                  ")
    print("      /  \/                \  ___            ")
    print("     /_/\/-----------------|/ __ \           ")
    print("    // \|              /\  | /\ \ \          ")
    print("   |/ /\|-------------/  \ |/  \ \ \         ")
    print("   / /  |   _____    / /\ \ \/\ \ \ \        ")
    print("  / / /\ \ /       \/ /__\ \/  \ \ \ \       ")
    print(" | / |  \_|        |_/    \ \   \ \ \ |      ")
    print(" |_| |    |x X X x |       \ \   | ||_|      ")
    print("   | |_   \________/       _\ \  |_|         ")
    print("   |__|   |_     _|        |__|              ")


    
###GAME OVER###
def gameover_text():
    a = '###############################\n#' 
    b = "         You are dead        #\n"
    c = '###############################\n\n\n'
    for character in a :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.001)
    for character in b :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in c :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.001)
    os.system('cls')
    tittle_screen()
                                           
            
###### GAME FUNCTIONALITY ######

   
def main_game_loop():
    while myPlayer.game_over is False:
        if myPlayer.location == 'Starting Point':
            safezone()
        else:    
            prompt()
def setup_game():
    question1 = "Hello, what's your name?\n"
    for character in question1 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "Choose a job\n"
    question2_added = "Warrior,\nRogue,\nMage,\nArcher\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in question2_added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    valid_jobs = ['warrior', 'rogue', 'mage', 'archer']
    class_change = True
    while class_change == True :
        player_job = input("> ")
        myPlayer.job = player_job
        if player_job.lower() in valid_jobs:
            ### PLAYER STATS
            if player_job.lower() == "warrior":
                choose_1 = True
                while choose_1 == True :
                    warrior_image()
                    yes_or_no_warrior = input("Do you want to pick this class \n(YES OR NO) \n>  ")
                    if yes_or_no_warrior.lower() == "yes" :
                        os.system('cls')
                        choose_1 = False
                        class_change = False
                        myPlayer.hp = 100
                        myPlayer.mana = 40
                        myPlayer.atk = 15
                    elif yes_or_no_warrior.lower() == 'no' :
                        choose_1 = False
                        os.system('cls')
                        class_change = True
                        for character in question2:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        for character in question2_added:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                    else :
                        print("Invalid Input ! \n")
                        input("Type anything to continue.....")
                        os.system('cls')
                        choose_1 = True
            elif player_job.lower() == "mage":
                choose_2 = True
                while choose_2 == True :
                    mage_image()
                    yes_or_no_warrior = input("Do you want to pick this class \n(YES OR NO) \n> ")
                    if yes_or_no_warrior.lower() == "yes" :
                        os.system('cls')
                        choose_2 = False
                        class_change = False
                        myPlayer.hp = 70
                        myPlayer.mana = 70
                        myPlayer.atk = 12
                    elif yes_or_no_warrior.lower() == 'no' :
                        choose_2 = False
                        os.system('cls')
                        class_change = True
                        for character in question2:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        for character in question2_added:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                    else :
                        print("Invalid Input ! \n")
                        input("Type anything to continue.....")
                        os.system('cls')
                        choose_2 = True
            elif player_job.lower() == "rogue":
                choose_3 = True
                while choose_3 == True :
                    rogue_image()
                    yes_or_no_warrior = input("Do you want to pick this class \n(YES OR NO) \n> ")
                    if yes_or_no_warrior.lower() == "yes" :
                        os.system('cls')
                        choose_3 = False
                        class_change = False
                        myPlayer.hp = 70
                        myPlayer.mana = 50
                        myPlayer.atk = 20
                    elif yes_or_no_warrior.lower() == 'no' :
                        choose_3 = False
                        os.system('cls')
                        class_change = True
                        for character in question2:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        for character in question2_added:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                    else :
                        print("Invalid Input ! \n")
                        input("Type anything to continue.....")
                        os.system('cls')
                        choose_3 = True
            elif player_job.lower() == "archer":
                choose_4 = True
                while choose_4 == True :
                    archer_image()
                    yes_or_no_warrior = input("Do you want to pick this class \n(YES OR NO)\n> ")
                    if yes_or_no_warrior.lower() == "yes" :
                        os.system('cls')
                        choose_4 = False
                        class_change = False
                        myPlayer.hp = 80
                        myPlayer.mana = 65
                        myPlayer.atk = 12
                    elif yes_or_no_warrior.lower() == 'no' :
                        choose_4 = False
                        os.system('cls')
                        class_change = True
                        for character in question2:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                        for character in question2_added:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.03)
                    else :
                        print("Invalid Input ! \n")
                        input("Type anything to continue.....")
                        os.system('cls')
                        choose_4 = True
        else : 
            player_job = print("Invalid job !, type the right job..")
            class_change = True
    print("You are now a " + player_job + "!\n")
                                    
    ### INTRODUCTION
    question3 = "Welcome, " + player_name + " the " + player_job + "..... !  \n"
    for character in question3 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("(Type Anything To Continue....)\n> ")
    myPlayer.name = player_name
    speech1 = "Welcome to this fantasy python world XD\n"
    speech2 = "This is just my first RPG test program and not complete yet btw hehe...\n"
    speech3 = "Hope you guys enjoy my test program.....\n"
    for character in speech1 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech2 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    for character in speech3 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)    

    os.system('cls')
    print("                                                     ")
    print("                                                     ")
    print("                                                     ")
    print("                                                     ")
    startsign =  "                   Well Then..................\n"
    startsign1 = "                   Let's start the adventure !\n"
    for character in startsign :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in startsign1 :
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    os.system('cls')
#### ADVENTURE START HERE ####
    main_game_loop()

def warrior_image():
    print("#######################################")
    print("#                                     #")
    print("#   ===========                       #")
    print("#   = WARRIOR =                       #")
    print("#   ===========     /\                #")
    print("#    =  HP  =      ||||               #")
    print("#    ========      ||||               #")
    print("#    = 100  =      ||||               #")
    print("#    ========      ||||               #")
    print("#    = ATK  =      ||||               #")
    print("#    ========      ||||               #")
    print("#    =  15  =    __||||__             #")
    print("#    ========   |__ 00___|            #")
    print("#    = MANA =      |\/|               #")
    print("#    ========      |__|               #")
    print("#    =  40  =                         #")
    print("#    ========                         #")
    print("#######################################")
    
def mage_image():
    print("#######################################")
    print("#                 ____                #")
    print("#   ===========  / __ \               #")
    print("#   =  MAGE   = | |  \ \              #")
    print("#   =========== |/ /\ \ \             #")
    print("#    =  HP  =      \/ / /             #")
    print("#    ========        / /              #")
    print("#    =  70  =       | /               #")
    print("#    ========       | |               #")
    print("#    = ATK  =       |_|               #")
    print("#    ========       |_|               #")
    print("#    =  12  =       |_|               #")
    print("#    ========       |_|               #")
    print("#    = MANA =       |_|               #")
    print("#    ========       |_|               #")
    print("#    =  70  =                         #")
    print("#    ========                         #")
    print("#######################################")

def rogue_image():
    print("#######################################")
    print("#                                     #")
    print("#   ===========                       #")
    print("#   =  ROGUE  =        _    __        #")
    print("#   ===========  _____|_|  /_/        #")
    print("#    =  HP  =    >____|_| /_/         #")
    print("#    ========        /|_|/_/\         #")
    print("#    =  70  =       / |_/_/\ \        #")
    print("#    ========      / /|/ / / \        #")
    print("#    = ATK  =     /^/ / /  |_\        #")
    print("#    ========        / /|             #")
    print("#    =  10  =       / / |             #")
    print("#    ========      / /| |             #")
    print("#    = MANA =     / / | |             #")
    print("#    ========    /_/  | |             #")
    print("#    =  70  =         |/              #")
    print("#    ========                         #")
    print("#######################################")

def archer_image():
    print("#######################################")
    print("#                _____                #")
    print("#                \   _\               #")
    print("#   ===========   \|| \\              #")
    print("#   =  ARCHER =    || |\\             #")
    print("#   ===========    || | \\            #")
    print("#    =  HP  =      || |  \\           #")
    print("#    ========      || |    \\         #")
    print("#    =  70  =      || |     \\        #")
    print("#    ======== ooooooooooooooooooooo|> #")
    print("#    = ATK  =      || |    //         #")
    print("#    ========      || |   //          #")
    print("#    =  10  =      || |  //           #")
    print("#    ========      || | //            #")
    print("#    = MANA =      || |//             #")
    print("#    ========      || //              #")
    print("#    =  70  =     / |//               #")
    print("#    ========    /___/                #")
    print("#######################################")
    

    
####START#####
tittle_screen()
