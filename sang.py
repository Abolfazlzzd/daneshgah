#sang_kaghaz_gheychi

gamelist = ['r', 'p', 's']     #game option
print(gamelist)
while True :
    player_1 = input("player_1 choose the gamelist: ")  #players
    player_2 = input("player_2 choose the gamelist: ")  #players
    if player_1 == player_2:
        print("mosavi shodid")
    elif player_1 == 'r' and player_2 == 'p':
        print("shoma bakhtid player_1")
    elif player_1 == 'r' and player_2 == 's':
        print("shoma bakhtid player_2")   
    elif player_1 == 'p' and player_2 == 's':
        print("shoma bakhtid player_1")
    elif player_1 == 'p' and player_2 == 'r':
        print("shoma bakhtid player_2") 
    elif player_1 == 's' and player_2 == 'r':
        print("shoma bakhtid player_1")
    elif player_1 == 's' and player_2 == 'p':
        print("shoma bakhtid player_2")
    else:
        print('gozineh dorost ra entekhab konid')
