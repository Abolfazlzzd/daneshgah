#jungle_game

animallist = ['moosh','fil','shir','sag','gorbeh'] #list heyvanat
print (animallist)

while True :
    player_1 = input(" player_1 yeki az heyvanat ra az jangal entekhab konid! ")
    player_2 = input(" player_2 yeki az heyvanat ra az jangal entekhab konid! ")
    player_3 = input(" player_3 yeki az heyvanat ra az jangal entekhab konid! ")
    if player_1 == player_2 == player_3 : #age mosavi entekhab konan
        print ("shoma mosavi hastid")
    if player_1 == player_2 :
        print ("shoma mosavi hastid player 1 va 2 ")
    if player_1 == player_3 :
        print ("shoma mosavi hastid player 1 va 3 ")
    if player_2 == player_3 :
        print ("shoma mosavi hastid player 2 va 3 ")
    if player_2 == player_1 :
        print ("shoma mosavi hastid player 2 va 1 ")
    if player_3 == player_1 :
        print ("shoma mosavi hastid player 3 va 1 ")
    if player_3 == player_2 :
        print ("shoma mosavi hastid player 3 va 2 ")        
    elif player_1 == 'moosh': #shoroe bazi
        print ("shoma barande shodid player_1 ")
    elif player_2 == 'moosh':
        print ("shoma barande shodid player_2 ")
    elif player_3 == 'moosh':
        print ("shoma barande shodid player_3 ")
    elif player_1 == 'fil':
        print ("shoma barande shodid player_1 ")
    elif player_2 == 'fil':
        print ("shoma barande shodid player_2 ")
    elif player_3 == 'fil':
        print ("shoma barande shodid player_3 ")
    elif player_1 == 'shir':
        print ("shoma barande shodid player_1 ")
    elif player_2 == 'shir':
        print ("shoma barande shodid player_2 ")
    elif player_3 == 'shir':
        print ("shoma barande shodid player_3 ")
    elif player_1 == 'sag':
        print ("shoma barande shodid player_1 ")
    elif player_2 == 'sag':
        print ("shoma barande shodid player_2 ")
    elif player_3 == 'sag':
        print ("shoma barande shodid player_3 ")
    elif player_1 == 'gorbeh':
        print ("shoma barande shodid player_1 ")
    elif player_2 == 'gorbeh':
        print ("shoma barande shodid player_2 ")
    elif player_3 == 'gorbeh':
        print ("shoma barande shodid player_3 ")
    else:
        print('shoma bazi ra bakhtid ya gozineh dorost ra entekhab nakarde eid')    

