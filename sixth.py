import sys
import requests
from html.parser import HTMLParser


class HrefParser(HTMLParser):
    """
    Třída pro parsování HTML a extrakci odkazů z tagů <a>
    """
    def __init__(self):
        super().__init__()
        self.hrefs = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href' and value:
                    self.hrefs.append(value)


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    try:
        # Stažení obsahu stránky
        response = requests.get(url)
        
        # Kontrola status kódu
        if response.status_code != 200:
            print(f"Chyba: Server vrátil status kód {response.status_code}")
            return []
        
        # Parsování HTML a extrakce odkazů
        parser = HrefParser()
        parser.feed(response.text)
        
        # Výpis výsledků
        print(f"Na stránce {url} bylo nalezeno {len(parser.hrefs)} odkazů:")
        for i, href in enumerate(parser.hrefs, 1):
            print(f"{i:3d}. {href}")
        
        return parser.hrefs
        
    except requests.exceptions.RequestException as e:
        print(f"Chyba při stahování URL: {e}")
        return []
    except Exception as e:
        print(f"Neočekávaná chyba: {e}")
        return []


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Použití: python sixth.py <URL>")
            print("Příklad: python sixth.py https://www.jcu.cz")
            sys.exit(1)
            
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        
    except Exception as e:
        print(f"Program skoncil chybou: {e}")