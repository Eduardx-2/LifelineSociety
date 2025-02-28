import requests 
import json
import argparse
from set_uri.find_regex_all_acept import C0untVerified
from set_uri.setter_uri_session import Sett_Verify_uri_
from set_uri.find_sites_web import Session_Inf0x_
from colors.colors import *

sett_uri = r"osint_name/set_uri/uri_sett.json"

TK_URL_F = ('instagram', 'youtube', 'facebook')

class Session_Scraping0x:
    def __init__(self, sett_find_=False) -> None:
        self.SETT_SESSION = sett_find_

    def validate_(self, file_site, us_):
        if self.SETT_SESSION == True:
            for site in file_site:
                if site in TK_URL_F:
                    if site == TK_URL_F[0]:
                        Session_Inf0x_().session_ig_user(us_)
                    elif site == TK_URL_F[1]:
                        Session_Inf0x_().session_user_yt(us_)
                    elif site == TK_URL_F[2]:
                        Session_Inf0x_().session_username_facebook(us_)
        else: print(f"{YELLOW}[!] {YELLOW}-{YELLOW} {ROJO}[USE -f PARA OBTENER MÁS INFORMACIÓN]")

class Napoleon_Sett:
    def __init__(self) -> None:
        self.R_SESSI0N = requests.session()

    def rb_set_uri(self):
        with open(sett_uri, 'r') as f_json:
            set_json = json.load(f_json)
            return set_json
        
    def set_user_session_find(self, _json, user_find_):
        print(f"{VERDEL}[+] {MG}->{MG} {ROJO}{user_find_}\n")
        for json in _json:
            c_verify = Sett_Verify_uri_().setter_uri_verify(json['uri'])    
            if c_verify[0] == True:
                if c_verify[1] == 'royaleapi.com':
                    print(C0untVerified().set_royale_verified(json['uri'].replace('rename', user_find_), json['agents']))
                elif c_verify[1] == 'www.instagram.com':
                    print(C0untVerified().set_instagram_verified(user_find_))       
            else:
                try:
                    session = self.R_SESSI0N.get(url=json['uri'].replace("rename", user_find_), headers=json['agents'])
                    if session.status_code == 200:
                        print(f"{VERDE}[FOUND] - {ROJO}{session.url}{ROJO}")
                    else: print(f"{YELLOW}[{ROJO}NOT FOUND{ROJO}{YELLOW}] {AZUL}-{AZUL} {YELLOW}{session.url}")
                except Exception as e:
                    print(f"{ROJO}[ERROR] -> {e}")


    def set_args_inicie(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--user', type=str, required=True, help="Especifica el nombre a buscar")
        parser.add_argument('-s', '--site', required=False, help="Opción para buscar en sitios especificos")
        parser.add_argument('-f', '--find', required=False, help="Obtener Información avanzada en un sitio")

        args = parser.parse_args()

        try:
            if args.site is not None:
                set_args = [site.strip() for site in args.site.split(",")]
                self.set_user_session_find(self.rb_set_uri(), find_=True)
            else:
                if args.user is not None:
                    self.set_user_session_find(self.rb_set_uri(), args.user)
                    if args.find is not None:
                        find_site_ = [site.strip() for site in args.find.split(",")]
                        Session_Scraping0x(sett_find_=True).validate_(find_site_, args.user)
                    else: print(f"\n{YELLOW}[!]{YELLOW} -> {ROJO}[PARA OBTENER MÁS INFORMACIÓN USE {VERDEL}(-f){ROJO}]")
                
        except Exception as e:
            print(f"[ERROR] ->{e}")


Napoleon_Sett().set_args_inicie()
                    