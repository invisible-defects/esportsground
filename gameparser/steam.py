import requests
import gameparser.__config__ as conf

class Parser:
    def __init__(self, key):
        """
        A parser interface for Steam
        :param key: a key string for the Steam api
        """

        self.key = key

    def getGameAchivements(self, steamid, appid):
        """
        Returns achivements of a cartain game
        :param steamid: int64 Steam account id
        :param appid: game id
        :return: games
        """

        link = "http://api.steampowered.com/ISteamUserStats/" \
               "GetPlayerAchievements/v0001/?appid={appid}&key={key}&steamid={sid}"
        link = link.format(key=self.key, sid=steamid, appid=appid)

        print(link)

        r = requests.get(link)

        return dict(r.json())["playerstats"]


if __name__ == "__main__":
    p = Parser(conf.STEAMKEY)
    print(p.getGameAchivements("76561198208367476", conf.STEAMGAMES["csgo"]))
