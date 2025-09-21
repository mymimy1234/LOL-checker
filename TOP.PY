import requests
from PIL import Image
API_KEY = "RGAPI-7e1ccdeb-ca17-4f2e-9104-2011be04e8b9"
ASIA_DOMAIN = "https://asia.api.riotgames.com"
QUERY = "?api_key="+API_KEY
def getPuuidByGameNameTagLine(gameName, tagLine):
    path = "/riot/account/v1/accounts/by-riot-id/"+gameName + "/" + tagLine
    url = ASIA_DOMAIN + path + QUERY
    response = requests.get(url=url)
    if response.status_code != 200:
        print("사용자 정보를 불러오지 못했습니다.")
        exit()
    response = response.json()
    puuid = response['puuid']
    return puuid

def league_v4_tier(tier):
    
    queue = 'RANKED_SOLO_5x5'
 
    if tier == 'challenger' :
        url = f"https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue}"
    elif tier == 'grandmaster':
        url = f"https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue}"
    else:
        url = f"https://kr.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue}"
        
    return tier