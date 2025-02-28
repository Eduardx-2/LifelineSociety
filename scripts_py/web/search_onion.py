import requests
from bs4 import BeautifulSoup
import argparse
from tabulate import tabulate


class ValidCrawler:
    def __init__(self) -> None:
        self.HD = ['URL-SITE', 'ESTADO', 'TIPO']
    
    def send_rq_data(self,urls_on):
        estado_data = list()
        try:
            headers_env ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0"}
            with requests.Session() as rqs_r:
                rqs_r.proxies = {}
                rqs_r.proxies['http'] = 'socks5h://127.0.0.1:9050'
                rqs_r.proxies['https'] = 'socks5h://127.0.0.1:9050'
                validate_rq = rqs_r.get(url=urls_on, headers=headers_env)
                if validate_rq.status_code == 200:
                    estado = "VALIDO"
                else:
                    estado = "INVALIDO"
                    
                estado_data.append([urls_on, validate_rq.status_code, estado])
            return estado_data
        except:
            return [[urls_on, 'NULL', 'INVALIDO']]
            
class MessageErros:
    DEF_MESSAGE_TROCH  = "Your search returned 0 results"
    

class SearchWebOnion:
    def __init__(self) -> None:
        self.URLS = {"excavator":"http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion/search/find_eye",
                     "torch": "http://torch4st4l57l2u2vr5wqwvwyueucvnrao4xajqr2klmcmicrv7ccaad.onion/",
                     "tor66": "http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/"}
        self.RQ = requests.session()
        self.EXTENDS = list()

    def index_link_bs4(self, html_parser:str):
        return BeautifulSoup(html_parser, "html.parser")

    def search_link(self, find_deep):
        data = list()
        try:
           # print(f"\n--------------------------------------------\n[SITE] => {find_deep}\n[INDEX] => EXCAVATOR-\n--------------------------------------------\n")
            print(f"[!] Esto puede tomar entre 60-80 segundos.....\n")
            self.RQ.proxies = {}
            self.RQ.proxies['http'] = 'socks5h://127.0.0.1:9050'
            self.RQ.proxies['https'] = 'socks5h://127.0.0.1:9050'
            self.RQ.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0"}
            send_r = self.RQ.get(url=self.URLS['excavator'].replace('find_eye', find_deep))
            search_url_onion = self.index_link_bs4(send_r.content)
            for url in search_url_onion.find_all("div", {'class': 'mx-auto'})[14:]: #/html/body/div/div[14]
                if url.a:
                    self.EXTENDS.append(url.a['href'])
                    #print(f"[URL-ONION]: {url.a['href']}") //*[@id="page"]
                    valid = ValidCrawler().send_rq_data(url.a['href'])
                    data.extend(valid)
                else:pass
            print(f"[!] Se realizaron {len(data)} peticiones\n")       
            print(tabulate(data, stralign="center",headers=ValidCrawler().HD, tablefmt="fancy_grid"))

        except Exception as e:
            print(str(e))

    def search_torch_link(self, find_dork):
        data_urls = list()
        try:
           #print(f"\n--------------------------------------------\n[SITE] => {find_dork}\n[INDEX] => TORCH\n--------------------------------------------\n")
           print(f"[!] Esto puede tomar entre 60-80 segundos.....\n")
           with requests.Session() as session_r:
               session_r.proxies = {}
               session_r.proxies['http'] = 'socks5h://127.0.0.1:9050'
               session_r.proxies['https'] = 'socks5h://127.0.0.1:9050'
               session_r.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0"}
               rq_r = session_r.get(url=self.URLS['torch'] + f'search?query={find_dork}&action=search')
               send_scrap = self.index_link_bs4(rq_r.content)
               error = send_scrap.find('div', {'class': 'col-lg-8'}).text
               if MessageErros().DEF_MESSAGE_TROCH in error:
                   print(f"La busqueda {find_dork} genero 0 resultados")
               else:
                    for links in send_scrap.find_all('div', {'class':'result mb-3'}):
                        #print(f"[URL-ONION]: {links.a['href']}") #result mb-3
                        valid = ValidCrawler().send_rq_data(links.a['href'])
                        data_urls.extend(valid)
                    print(f"[!] Se realizaron {len(data_urls)} peticiones\n")
                    print(tabulate(data_urls, stralign="center",headers=ValidCrawler().HD, tablefmt="fancy_grid"))
                    
        except Exception as e:
            print(e)

    def search_tor66(self, find_dork):
        find_url = list()
        try:
            print(f"[!] Esto puede tomar entre 60-80 segundos.....\n")
            with requests.Session() as session_s:

                session_s.proxies = {}
                session_s.proxies['http'] = 'socks5h://127.0.0.1:9050'
                session_s.proxies['https'] = 'socks5h://127.0.0.1:9050'
                session_s.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0"}
                req = session_s.get(url=self.URLS['tor66'] + f"search.php?term={find_dork}")
                parser_links = self.index_link_bs4(req.content)
               # links_a = parser_links.findAll("li")[4:23]
                for links in parser_links.findAll("li")[4:23]:
                    valid = ValidCrawler().send_rq_data(links.a['href'])
                    find_url.extend(valid)#/html/body/div[3]/div/div[1]/ul[1]/li/a
                print(f"[!] Se realizaron {len(find_url)} peticiones")
                print(tabulate(find_url, stralign="center",headers=ValidCrawler().HD, tablefmt="fancy_grid"))
        except Exception as e:
            print(str(e))


class CompileCommands:
    def args_inicie():
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--index", help="Indica atraves de que motor quieres realizar la busqueda", required=True, type=str)
        parser.add_argument("-s", "--site", help="Ingresa el sitio a buscar", required=True, type=str)

        args = parser.parse_args()

        if args.index.lower() in ("exv", "excavator"): SearchWebOnion().search_link(args.site)
        elif args.index.lower() in ("trch", "torch"): SearchWebOnion().search_torch_link(args.site) 
        elif args.index.lower() in ("trs", "tors"): SearchWebOnion().search_tor66(args.site)
        else: print("Error")

CompileCommands.args_inicie()