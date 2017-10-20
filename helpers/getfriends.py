import vk
from gameparser.__config__ import VKAPP

session = vk.InteractiveSession(VKAPP)
vk_api = vk.API(session)

def getFriends(uid):
    """
    Return vk friends
    :param uid: string, vk id, exaple: 1, 128819
    :return: dict, user name : profile pic link
    """
    response = vk_api.freinds.get(user_id=str(uid))
    return response

if __name__ == "__main__":
    print(getFriends(17))