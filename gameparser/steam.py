import requests
import gameparser.__config__ as conf

class Parser:
    def __init__(self, key):
        """
        A parser interface for Steam
        :param key: a key string for the Steam api
        """

        self.key = key

    def getGameAchievements(self, steamid, appid):
        """
        Returns achievements of a certain game
        :param steamid: int64 Steam account id
        :param appid: game id
        :return: games
        """

        link = "http://api.steampowered.com/ISteamUserStats/" \
               "GetPlayerAchievements/v0001/?appid={appid}&key={key}&steamid={sid}"
        link = link.format(key=self.key, sid=steamid, appid=appid)
        r = requests.get(link)

        return dict(r.json())["playerstats"]

    def getUserStatsForGame(self, steamid, appid):
        """
        Returns Statistics of a certain game
        :param steamid: int64 Steam account id
        :param appid: Steam game id (listed in __config__.STEAMGAMES)
        :return: games
        """

        link = "http://api.steampowered.com/ISteamUserStats/" \
               "GetUserStatsForGame/v0002/?appid={appid}&key={key}&steamid={sid}"
        link = link.format(key=self.key, appid=appid, sid=steamid)
        r = requests.get(link)

        data = dict(r.json())["playerstats"]["stats"]
        data = {arr['name'] : arr['value'] for arr in data}

        keys = ["total_kills", "total_deaths", "total_time_played", "total_wins",
                "total_kills_headshot", "total_shots_fired", "total_shots_hit", 'total_mvps', 'total_matches_played']
        [data.pop(k) for k in data.copy().keys() if k not in keys]

        return data

    def isVACBanned(self, steamid):
        """
        Tells if players is VACBanned
        :param steamid: id64 Steam account id
        :return: bool
        """

        link = "http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key={key}&steamids={sid}"
        link = link.format(key=self.key, sid=steamid)

        r = requests.get(link)

        return dict(r.json())['players'][0]["VACBanned"]




if __name__ == "__main__":
    p = Parser(conf.STEAMKEY)
    print(p.getBans("76561197960435530"))

