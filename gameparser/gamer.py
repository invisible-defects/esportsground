from gameparser.steam import Parser
import gameparser.__config__ as conf

parser = Parser(conf.STEAMKEY)

class Gamer:
    def __init__(self, vk_id, steam_id, game_names):
        '''
        A class that keep a users inforamtion
        :param vk_id: vk id
        :param steam_id: suprisingly, steam id :)
        :param game_names: list of games (can find in __config__.py), example: ["csgo, "dota2"]
        '''

        self.vk_id = vk_id
        self.steam_id = steam_id

        self.stats = list()
        for game in game_names:
            stats = parser.getUserStatsForGame(steam_id, conf.STEAMGAMES[game])

            self.stats.append({game : stats})




if __name__ == "__main__":
    g = Gamer(123213, "76561198208367476", ["csgo"])
    print(g.stats)



