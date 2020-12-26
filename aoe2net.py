import requests
from steam.steamid import SteamID

#DE APP ID: 813780
#STEAMKEY: 1AE7FC208EB1094123CA30D9AE7F5339
def steam64(steam_id):
	steamids = SteamID(steam_id)
	return steamids.as_64

alias = 94590787

print(steam64(alias))

"""
http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=813780&key=1AE7FC208EB1094123CA30D9AE7F5339&steamid=76561198054856515
"""

def getstrings():
	pass

def issteam_id():
	pass

def playersearch(alias, ):
	if alias == steam_id:
		pass
	elif alias == profile_id:
		pass
	else:
"""
