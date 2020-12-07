import random 

hp = 5
# intro
def intro():
    print("Welcome to The Witcher Adventure Game!")
    print("Geralt of Rivia, also known as The Witcher, travels alone hunting monsters.")
    print("Geralt's goal is to make it across the contient to a young princess named Ciri.")
    print("Help Geralt fullfil his destiny!" )
    print('You start the game with 5 hp, and a sword')
    
    
def choosenPath():
    forward = print(input("Would you like to step forward? (y or n): "))
    if forward == "y":
        print('You take a step forward')
    elif forward != "n":
        print('Geralt sits wondering when you are going to deicde to provide a correct command')
        

def Torque():
    print('You have been run over by a Torque, a horned devil')           
    print('You get up and ask Torque what he is doing')
    print('Torque throws a rock')
    print('Torque is a rare creature with 5 hp')
    usersinput = (input('DO you wish to run or attack? (run or attack): '))
    if usersinput == 'run':
        print('You try and swiftly get away but your head is spinning and you have no idea which direction you are headed')
        print('You manage to get away')
        hp - 2
        print('You\'re hp is now', hp - 2)
    elif usersinput == 'attack':
        print('You draw your sword and realize you do not see Torque')
        print('Torque throws another rock')
        print('You lift your arm and cast a spell towrds some bushes') 
        print('You hear Torque beg for mercy')
        print('You have defeated the horned devil')
        hp - 2
        print('You\'re hp is now', hp - 2)


def Yennefer():
    print('you begin to feel light headed')
    print('You have been attacked by Yennefer a powerful sorceress.')
    print('Yennefer has 50 hp, she is half elf with bright purple eyes. To your knowledge Yennefer has no weaknesses')
    decision = (input('DO you wish to run or attack? (run or attack): '))
    if decision == "run":
        print('You try and swiftly get away but your head is spinning and you have no idea which direction you are headed')
        print('You manage to get away from Yennefer')
        hp - 1
        print('You\'re hp is now', hp - 1)
    if decision == "attack":
        print('You lift your hand and cast a spell disabeling Yennefer')
        print('Yennefer hp falls by 1')
        print('Your spell was not super affective against the powerful sorceress') 
        print('You try and shake the light headedness away')
        hp - 3
        print('You\'re hp is now', hp - 3)
        
def Djinn():
    print('You have been attacked by a Djinn')
    print('Fighting a djinn is extraordinarily difficult. They can fling off spells in an instant that the most accomplished human mages could never cast with years of preparation.')
    print('The Djinn has hp above 20')
    print('Luckily, as magic beings, they are vulnerable to silver.')
    djinnD = (input('DO you wish to run or attack? (run or attack): '))
    if djinnD =='attack':
        print('You realize you have no silver, you have been killed by the Djinn')
        hp - 5
        print('You\'ve gathered', trinkets)
    elif djinnD =='run':
        print('You sprint in the opposite direction praying the Djinn did not notice you')
        print('You\'re hp is now', hp)
          
#def hp():
 #   if hp == 0 or hp < 0 :
  #      print('You have died')
   #     print (hp, trinkets, 'acquired')
   # elif hp > 0 :

intro()
trinkets =""
for steps in range (5):
    forward = (input("Would you like to step forward? (y or n): "))
    if forward != "n":
        print('You take a step forward')
    else:
        #forward != "n":
        print('Geralt sits wondering when you are going to deicde to provide a correct command')
        break
        #Trinket or Monster
    TM = random.randrange(0,2)
    if TM == 0:
    #Monsters 1-3
        randommonster = random.randrange(0,3)
        if randommonster == 0:
           Yennefer()
        if randommonster == 1:
           Torque()
        if randommonster == 2:
           Djinn()            
    if TM == 1:
            #TRINKETS 1-3
        trinket = random.randrange(0,3)
        if trinket == 0:
            Roach = print('You have come across your horse Roach')
            trinkets = trinkets + " Roach"
        if trinket == 1:
            gold = print('You have colleced 10 gold pieces!')
            trinkets = trinkets + " gold"

        if trinket == 2:
            bard = print('You have been joined by an extremely annoying bard')
            trinkets = trinkets + " Bard"
                
    while hp < 0 or hp == 0:
         print('You\'ve died!! However you\ve acquired', trinkets)
if hp > 0:
    print('Congratulations You Have Completed The Game!')
    print("Your HP is ", hp, "and you've gathered", trinkets)
  
     
            

