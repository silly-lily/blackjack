import game_module as gm



def main():

    games = 0
    games_user_won = 0
    
    while should_play():
        game = gm.Game()
        games+=1
        if game.calc_game() == 'user won':
            games_user_won+=1

    print('You won '+str(games_user_won)+' out of '+str(games))

def should_play():

    print('play hand? (y/n)')
    ans = input()
    
    if ans == 'y':
        return True
    elif ans == 'n':
        return False
    else:
        return should_play()

main()