from webapp.models import User
from gameparser import Gamer

def getByVkId(vkid, games=["csgo"]):
    user = User.query.filter_by(vkid=vkid).first()
    steamid = user.steamid

    print(steamid)

    gamer = Gamer(steamid, game_names=games)

    return gamer

