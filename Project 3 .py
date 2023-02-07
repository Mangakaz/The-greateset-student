def check_time():
 global time 
 time = time - 1
 if time <= 0:
     def failed():
    
     

        print("You only have 20 Minutes to get to the castle", 20 - time, "minutes")



def start():
    print("It seem's as if there pieces of Princess Plum's dress on the ground, lets see if they lead anywhere!")
    Start()

def Start():
    check_time()
    print("You are in Start")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tQuestion Block\n\tGoomba\n")
    if move.lower() == "question block": 
        Question_Block()
    elif move.lower() == "goomba":
        Goomba()
    else:
        #TODO: what should happen if they type something else?
        print("Stop Using Cheats")

def Question_Block():
    check_time()
    print("It seems there is something right here, should we touch it?")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tMove on\n\tJump\n")
    if move.lower() == "move on":
        Pipe()
    elif move.lower() == "jump":
        Block_A()
    else:
        #TODO: what should happen if they type something else?
        print("Stop using cheats")

def Goomba():
    check_time()
    print("It looks as if there aren't to many of these goomba's which is lucky")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tStomp\n")
    if move.lower() == "stomp":
        Question_Block()
    else:
        #TODO: what should happen if they type something else?
        print("Stop using cheats")

def Pipe():
    check_time()
    print("This pipe look's as if it leads somehwere...")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tBlock\n\tDown\n")
    if move.lower() == "block":
        Block_A()
    elif move.lower() == "down":
        Down()
    else:
        #TODO: what should happen if they type something else?
        print("Stop using cheats")

def Down():
    check_time()
    print("Oh it seems as if there isn't anything here....Ima go back up")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tPipe\n")
    if move.lower() == "pipe":
        Pipe()

    else:
        #TODO: what should happen if they type something else?
        print("Stop using cheats")
    
def Block_B():
    check_time()
    print("There seem's like theres a flag at the top of these blocks.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tFlag \n")
    if move.lower() == "flag":
        Flag()
    else:
        print("Stop using cheats")

def Block_A():
    check_time()
    print("There seem's like theres a flag at the top of these blocks.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tgo up\n")
    if move.lower() == "go up":
        Flag()
    else:
        print("Stop using cheats")
    
    
    

def Flag ():
    print("Seem's like this is the end, would you want to restart?.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tRestart\n")
    if move.lower() == "restart":
        Start()
        
    else:
        print("Stop using cheats")


time = 15
start()