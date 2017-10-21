from webapp.models import User
import sys
sys.path.insert(0, "./../")
from gameparser import Gamer

def getByVkId(vkid, games=["csgo"]):
    user = User.query.filter_by(vkid=vkid).first()
    steamid = user.steamid

    print(steamid)

    gamer = Gamer(steamid, game_names=games)

    return gamer