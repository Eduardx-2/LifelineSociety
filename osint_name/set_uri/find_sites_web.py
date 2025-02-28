import requests
from colors.colors import *

class Ag3nts0x_session:
    @staticmethod
    def _s0xfinst4():
        headers_u = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
            "X-CSRFToken": "o9GHPZokHeaNtSBJ31j3uqiU29c6iyZj",
            "x-asbd-id": "129477",
            "x-ig-app-id": "936619743392459",
            "X-Requested-With": "XMLHttpRequest"
        }
        return headers_u

class Session_Inf0x_:
    def __init__(self) -> None:
        self.RQ_S = requests.session()

    def session_ig_user(self, regex_user_):
        print(f"\n{YELLOW}[{MG}SEARCH{MG}{YELLOW}] {MG}-> {YELLOW}[{ROJO}{regex_user_}{ROJO}{YELLOW}] {MG}-> {YELLOW}[{MG}INSTAGRAM{MG}{YELLOW}]\n")
        try:
            uri = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={regex_user_}"
            rq_set_uri = self.RQ_S.get(url=uri,headers=Ag3nts0x_session()._s0xfinst4())
            if rq_set_uri.status_code == 200:
                user_find = rq_set_uri.json()['data']['user']
                bio = user_find["biography"]
                follow_usr = user_find["edge_followed_by"]["count"]
                edge_follow = user_find["edge_follow"]["count"]
                full_name = user_find["full_name"]
                for links_profile in user_find["bio_links"]:
                    url_ = links_profile['url']
                    type_l = links_profile['link_type']
                
                text_ask = f"\n{VERDE}NOMBRE: {WHITE}{full_name}\n{VERDE}BIOGRAFIA: {WHITE}{bio}\n{VERDE}URL: {WHITE}{url_}\n{VERDE}TYPE_LINK: {WHITE}{type_l}\n{VERDE}SEGUIDORES: {WHITE}{follow_usr}\n{VERDE}SEGUIDOS: {WHITE}{edge_follow}"
                print(text_ask)
            else:
                print(f"[FAILED] -> [ERROR SCRAPING]")
        except Exception as e:
            print(f"[SCRAPING]- {e}")
    
    def session_user_yt(self, rgx_user_):
        try:
            _list_link_ = []
            print(f"\n{YELLOW}[{MG}SEARCH{MG}{YELLOW}] {MG}-> {YELLOW}[{ROJO}{rgx_user_}{ROJO}{YELLOW}] {MG}-> {YELLOW}[{MG}YT{MG}{YELLOW}]\n")
            r_Q = self.RQ_S.get(f"http://127.0.0.1:9094/find/user/yt/{rgx_user_}")
            if r_Q.status_code == 200:
                sub = r_Q.json()["suscriptores"]
                vid = r_Q.json()["videos"]
                ubi = r_Q.json()["ubicacion"]
                fecha = r_Q.json()["fecha"]
                estats = r_Q.json()["subs"]
                for linkS_profil3 in r_Q.json()["links"]:
                    _list_link_.append(linkS_profil3.split("=")[3])
                text_yt = f"{VERDE}SUSCRIPTORES: {WHITE}{sub}\n{VERDE}VIDEOS: {WHITE}{vid}\n{VERDE}UBICACIÓN: {WHITE}{ubi}\n{VERDE}FECHA: {WHITE}{fecha}\n{VERDE}ESTADISTICAS: {WHITE}{estats}\n{VERDE}LINKS: {WHITE}{len(_list_link_)}"

                print(text_yt)
        except Exception as e:
            print(str(e))

    def session_username_facebook(self, rgx_usr):
        try:
            print(f"\n{YELLOW}[{MG}SEARCH{MG}{YELLOW}] {MG}-> {YELLOW}[{ROJO}{rgx_usr}{ROJO}{YELLOW}] {MG}-> {YELLOW}[{MG}FACEBOOK{MG}{YELLOW}]\n")
            rq_session = self.RQ_S.get(f"http://127.0.0.1:9094/find/user/facebook/{rgx_usr}")
            if rq_session.status_code == 200:
                link = rq_session.json()["link"]
                seguidos = rq_session.json()["seguidos"]
                sg = rq_session.json()["seguidores"]
                id = rq_session.json()["id"]
                fecha  = rq_session.json()["fecha_creacion"]
                text_find_fb = f"{VERDE}SEGUIDORES: {WHITE}{sg}\n{VERDE}SEGUIDOS: {WHITE}{seguidos}\n{VERDE}ID: {WHITE}{id}\n{VERDE}FECHA CREACION: {WHITE}{fecha}\n{VERDE}LINK: {WHITE}{link}"
                print(text_find_fb)
        except Exception as e:
            print(e)
    
    