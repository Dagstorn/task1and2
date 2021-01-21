import random
import time 

# generating play card with random 5 numbers for each player
def create_play_card():
    player_card = []
    for i in range(0,5):
        n = random.randint(1,99)
        player_card.append(n)
    return player_card

# moddels
class Player:
    def __init__(self, name):
        self.name = name
        # creates game cards for players
        self.player_card = create_play_card()
    
    def check_player_card(self, game_numbers):
        # set to list
        numbers = list(game_numbers)
        player = self.player_card
        common_items = []

        for i in range(len(numbers)):
            if numbers[i] in player and numbers[i] not in common_items:
                common_items.append(numbers[i])        
            
            player.sort()
            common_items.sort()

            if player == common_items:
                print('%s BINGO!!!' % (self.name.upper()))
                global winner
                winner = True
                break

class Observer:
    def __init__(self):
        self.numbers = set()
        self.players = set()

    def add_player(self, player):
        self.players.add(player)

    def add_num(self, num):
        self.numbers.add(num)
        print('We got number: %s' % (num))
    
    def display_players(self):
        for player in self.players:
            print(player.name)
            print(player.player_card)

    def look_for_winner(self):
        for player in self.players:
            if len(self.numbers) > 4:
                player.check_player_card(self.numbers)

# game host
obs = Observer()

# initiating players
alex = Player('Alex')
john = Player('John')
anna = Player('Anna')
lisa = Player('Lisa')
karl = Player('Karl')
# adding players to game
obs.add_player(alex)
obs.add_player(john)
obs.add_player(anna)
obs.add_player(lisa)
obs.add_player(karl)

# printing players cards at start
obs.display_players()

# Start of the game
print('Welcome to bingo game')
# game flag
winner = False
# game loop
while winner is False:
    current_number = random.randint(1,99)
    obs.add_num(current_number)
    
    # checking players 
    obs.look_for_winner()

    # delay
    # time.sleep(1)
