import requests
from set_uri.setter_uri_session import Session_Scraper
from colors.colors import *

class C0untVerified:
    

    def set_royale_verified(self, url:str, header):
        session_ = requests.get(url=url, headers=header)
        if session_.status_code == 200:
            html_find = Session_Scraper().session_html(session_.content)
            sent = html_find.find_all('h4', {'class': 'ui attached header'})
            for _f in sent:
                if 'Found 0 possible match from database.' in _f.text:
                    return f'{VERDE}[FOUND] - {ROJO}{session_.url}{ROJO}'
                else:
                    return f"{YELLOW}[{ROJO}NOT FOUND{ROJO}{YELLOW}] {AZUL}-{AZUL} {YELLOW}{session_.url}"
    
    def set_instagram_verified(self, user_:str):
        try:
            uri = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={user_}"
            r_find = requests.get(uri, headers=self.sett_agents_0xfinst4())
              
            if r_find.status_code == 200:
                return f"{VERDE}[FOUND]{VERDE}- {ROJO}https://www.instagram.com/{user_}"
            else:
                return f"{YELLOW}[{ROJO}NOT FOUND{ROJO}{YELLOW}] {AZUL}-{AZUL} {YELLOW}https://www.instagram.com/{user_}"
        except Exception as e:
            print(str(e))

    @staticmethod
    def sett_agents_0xfinst4():
        headers_u = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
            "X-CSRFToken": "o9GHPZokHeaNtSBJ31j3uqiU29c6iyZj",
            "x-asbd-id": "129477",
            "x-ig-app-id": "936619743392459",
            "X-Requested-With": "XMLHttpRequest"
        }
        return headers_u