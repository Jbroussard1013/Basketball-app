import copy
from constants import PLAYERS
from constants import TEAMS


def clean_data(data):
    players_copy = copy.deepcopy(data)
    for item in players_copy:
        item['height'] = (int(item['height'].split(' ')[0]))
        item['guardians'] = item['guardians'].split('and')
        if item['experience'] == 'YES':
            item['experience'] = True 
        else:
            item['experience'] = False
    return players_copy
    
# The exp used in this case is shorthand for experienced
def balance_teams():
    num_players_teams = int(len(PLAYERS) / len(TEAMS))
    All_players = clean_data(PLAYERS)
    exp_players = []
    non_exp_players = []
    for player in All_players:
        if player['experience'] == True:
            exp_players.append(player)
        else: 
            non_exp_players.append(player)
    panthers = [exp_players[i]['name'] for i in range(0,3)]
    bandits = [exp_players[i]['name'] for i in range(3,6)]
    warriors =[exp_players[i]['name'] for i in range(6,9)] 
    for player in non_exp_players:
        if len(panthers) < num_players_teams:
            panthers.append(player['name'])
        elif len(warriors) < num_players_teams:
            warriors.append(player['name'])  
        else:
            bandits.append(player['name'])
    return panthers, bandits, warriors

teams = balance_teams()

def create_menu():
    print('\nTHE BASKETBALL STATS TOOL. \n')
    print('----- MENU -------\n\n')
    print ('Your options are:\n A) Display Team Stats\n B) Quit\n')
    choice = (input('Please select an option:  '))
    

    if choice.lower() == 'a':
        print('A) Panthers \nB) Bandits\nC) Warriors\n\n')
        team_choice()
        create_menu()
        
    elif choice.lower() == 'b':
        return False
    else:
        print('\nPlease select either A or B.\n')
        create_menu()

def show_team_stats(team):
    teams = ', '.join(team)
    print(f'Total players: {len(team)}')
    print(f'\nTeam members: {teams} \n------------------')



def team_choice():
    choosen_team = input('Select a team: ')
    if choosen_team.lower() == 'a':
            print('\nTeam: Panthers stats\n-------------------')
            show_team_stats(teams[0])
    elif choosen_team.lower() == 'b':
            print('\nTeam: Bandits stats\n--------------------') 
            show_team_stats(teams[1])   
    elif choosen_team.lower() == 'c':
            print('\nTeam: Warriors stats\n-------------------')
            show_team_stats(teams[2])
    else:
            print("\nPlease select one of the teams from above.\n")
            team_choice()


if __name__ =='__main__':
    player_exit = 'True'
    while player_exit:
        player_exit = create_menu()