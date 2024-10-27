import requests, os, time
from colorama import Fore, Style
import fade

class color:
    WHITE = Fore.WHITE + Style.BRIGHT
    RED = Fore.RED + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

class IntelX:
    def __init__(self, key):
        self.url = "https://2.intelx.io/"
        self.key = key
        self.agent = 'IX-Python/0.5'

    def search(self, term, max=100):
        headers = {'x-key': self.key, 'User-Agent': self.agent}
        data = {"term": term, "maxresults": max, "lookuplevel": 0}
        
        res = requests.post(f"{self.url}/intelligent/search", headers=headers, json=data)
        sid = res.json().get('id')
        print(f"id : {sid}")
        return self.results(sid, max)

    def results(self, sid, max):
        headers = {'x-key': self.key, 'User-Agent': self.agent}
        
        while True:
            time.sleep(1)
            res = requests.get(f"{self.url}/intelligent/search/result?id={sid}&limit={max}", headers=headers)
            data = res.json()
            if data['status'] in [1, 2]:
                return data['records']

def main():
    os.system('cls' if os.name == "nt" else 'clear')
    ascii = f"""
  ██╗███╗   ██╗████████╗███████╗██╗     ██╗  ██╗
  ██║████╗  ██║╚══██╔══╝██╔════╝██║     ╚██╗██╔╝
  ██║██╔██╗ ██║   ██║   █████╗  ██║      ╚███╔╝ 
  ██║██║╚██╗██║   ██║   ██╔══╝  ██║      ██╔██╗ 
  ██║██║ ╚████║   ██║   ███████╗███████╗██╔╝ ██╗
  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
"""
    print(fade.fire(ascii))
    dem = input(f"{color.WHITE}  [*] Please enter the search query: ")
    print(color.WHITE + '\n')
    key = "0156bf6d-5caa-44e7-8392-4f79d353a30c"
    ix = IntelX(key)
    res = ix.search(dem)
    for r in res:
        print(r)

    choice = input(f"{color.WHITE}  \n[*] Press ENTER to return the menu: ")
    main()

if __name__ == "__main__":
    main()
