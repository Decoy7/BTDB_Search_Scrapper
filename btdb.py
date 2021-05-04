from requests import get
from random import choice
from bs4 import BeautifulSoup


class btdb_eu():
    url = 'https://btdb.eu/'
    name = 'Btdb.eu'

    def search(what,order_by):
        name = []
        desc_link = []
        size = []
        seeds = []
        leech = []
        magnet = []
        torrent = []
        added = []
        fnl = {}

        user_agent_list = [
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        ]

        user_agent = choice(user_agent_list)
        headers = {'User-Agent': user_agent}

        #Normalize search term
        what = what.replace(" ", "%20").strip("%20")

        #Get top torrents of the day
        if str(order_by.lower())=="top":
            url = "https://btdb.eu/top"
            result = get(url, headers=headers)
        
        #Order by size
        elif str(order_by.lower())=="length":
            url = "https://btdb.eu/search/"+what+"/0/?sort=length"
            result = get(url, headers=headers)
        
        #Order by popular
        elif str(order_by.lower())=="popular":
            url = "https://btdb.eu/search/"+what+"/0/?sort=popular"
            result = get(url, headers=headers)
        
        #Order by downloads
        elif str(order_by.lower())=="hits":
            url = "https://btdb.eu/search/"+what+"/0/?sort=hits"
            result = get(url, headers=headers)

        else:
            return ("No category given.")

        soup = BeautifulSoup(result.text, 'lxml')

        # Get Name And Description Link of the torrent
        for item in soup.find_all("h2", class_="item-title"):
            for child in item.children:
                name.append(child.get("title"))
                desc_link.append(child.get("href"))

        # Get Size,Seeders and Leechers
        alist = []
        for item in soup.findAll('strong'):
            alist.append(item.text)
        alist.pop(0)  # Delete the first header we don't need.
        for i in range(len(alist)):
            # if ("MB") in str(alist[i]) or ("GB") in str(alist[i]) or ("KB") in str(alist[i]): ### More explicit decided to use more broad expression to catch as many as I can ###
            if ("B") in str(alist[i]):
                size.append(str(alist[i]))
                seeds.append(str(alist[i+2]))
                leech.append(str(alist[i+3]))
                added.append(str(alist[i+4]))

        # Get Magnet
        for item in soup.find_all("a", class_="btn btn-square btn-outline btn-success"):
            magnet.append(str(item.get("href")))

        # Get Torrent File
        for item in soup.find_all("a", class_="btn btn-square btn-outline btn-danger"):
            if "https://btdb.eu/" == item.get("href"):
                torrent.append(
                    "Torrent Link Not Downloadable.Check for Magnet Link.")
            else:
                torrent.append(str(item.get("href")))

        lst = []
        for i in range(len(name)):
            temp = {
                "title": name[i],
                "size": size[i],
                "seeds": seeds[i],
                "leeches": leech[i],
                "magnet": magnet[i],
                "torrent": torrent[i],
                "desc_link": desc_link[i],
                "added": added[i]
            }
            lst.append(temp)

        fnl = lst

        return fnl