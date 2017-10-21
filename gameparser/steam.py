import requests
try:
    import gameparser.__config__ as conf
except:
    import __config__ as conf

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

        print(dict(r.json()))

        data = dict(r.json())["playerstats"]["stats"]
        data = {arr['name'] : arr['value'] for arr in data}

        keys = ["total_kills", "total_deaths", "total_time_played", "total_wins",
                "total_kills_headshot", "total_shots_fired", "total_shots_hit", 'total_mvps', 'total_matches_played']
        [data.pop(k) for k in data.copy().keys() if k not in keys]

        return data

    def getUserMapsInCS(self, steamid):
        """
        Returns Statistics of rounds in maps in CS
        :param steamid: str Steam account id
        :return: dict map:rounds played
        """

        link = "http://api.steampowered.com/ISteamUserStats/" \
               "GetUserStatsForGame/v0002/?appid={appid}&key={key}&steamid={sid}"
        link = link.format(key=self.key, appid="730", sid=steamid)
        r = requests.get(link)

        data = dict(r.json())["playerstats"]["stats"]
        data = {arr['name'] : arr['value'] for arr in data}

        keys = ['total_wins_map_ar_baggage',
 'total_wins_map_ar_monastery',
 'total_wins_map_ar_shoots',
 'total_wins_map_cs_assault',
 'total_wins_map_cs_italy',
 'total_wins_map_cs_office',
 'total_wins_map_de_cbble',
 'total_wins_map_de_dust',
 'total_wins_map_de_dust2',
 'total_wins_map_de_inferno',
 'total_wins_map_de_lake',
 'total_wins_map_de_nuke',
 'total_wins_map_de_safehouse',
 'total_wins_map_de_stmarc',
 'total_wins_map_de_train']
        [data.pop(k) for k in data.copy().keys() if k not in keys]

        return data
    
    
    def getUserBestMapsInCS(self, steamid):
        """
        :param steamid: str Steam account id
        :return: dict map:rounds played. len(dict)=5
        """
        link = "http://api.steampowered.com/ISteamUserStats/" \
               "GetUserStatsForGame/v0002/?appid={appid}&key={key}&steamid={sid}"
        link = link.format(key=self.key, appid="730", sid=steamid)
        r = requests.get(link)

        data = dict(r.json())["playerstats"]["stats"]
        data = {arr['name'] : arr['value'] for arr in data}

        keys = ['total_wins_map_ar_baggage',
 'total_wins_map_ar_monastery',
 'total_wins_map_ar_shoots',
 'total_wins_map_cs_assault',
 'total_wins_map_cs_italy',
 'total_wins_map_cs_office',
 'total_wins_map_de_cbble',
 'total_wins_map_de_dust',
 'total_wins_map_de_dust2',
 'total_wins_map_de_inferno',
 'total_wins_map_de_lake',
 'total_wins_map_de_nuke',
 'total_wins_map_de_safehouse',
 'total_wins_map_de_stmarc',
 'total_wins_map_de_train']
        [data.pop(k) for k in data.copy().keys() if k not in keys]
        
        data={v:k for k, v in data.items()}
        return [(data[i], i) for i,j in zip(sorted(data, reverse=True), range(5))]
    
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


    def getPlayerName(self, steamid):
        link = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={sid}"
        link = link.format(key=self.key, sid=steamid)

        r = requests.get(link)

        return dict(r.json())["response"]["players"][0]["personaname"]



if __name__ == "__main__":
    p = Parser(conf.STEAMKEY)
    print(p.getPlayerName("76561198353376393"))

