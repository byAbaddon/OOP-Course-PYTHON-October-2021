# from player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        if player_name not in [x.name for x in self.players]:
            return f'Player {player_name} is not in the guild.'
        user = [x for x in self.players if x.name == player_name][0]
        self.players.remove(user)
        user.guild = 'Unaffiliated'
        return f'Player {player_name} has been removed from the guild.'

    def guild_info(self,):
        return f'Guild: {self.name}\n{"".join([x.player_info() for x in self.players])}'


'''       
player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

--------------------------------
Skill Shield Break added to the collection of the player George
Name: George
Guild: Unaffiliated
HP: 50
MP: 100
===Shield Break - 20

Welcome player George to the guild UGT
Guild: UGT
Name: George
Guild: UGT
HP: 50
MP: 100
===Shield Break - 20



'''