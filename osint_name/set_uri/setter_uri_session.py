from bs4 import BeautifulSoup

VERIFY_URI = ('steamcommunity.com', 'royaleapi.com', 'www.instagram.com')

class Session_Scraper:
    def session_html(self, html_):
        return BeautifulSoup(html_, "html.parser")

class Sett_Verify_uri_:

    def setter_uri_verify(self, _uri):
        set_http = _uri.split("://")[0]
        if set_http == "https":
            find_dmn = _uri.split("://")[1].split("/")[0]
            if find_dmn in VERIFY_URI:
                return [True, find_dmn]
            else:
                return [False]
        else:
            return False