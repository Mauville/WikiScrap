import requests
import bs4
#TODO import json
import win_unicode_console

win_unicode_console.enable()

url = "http://www.james-camerons-avatar.wikia.com/api/v1/Articles/List?limit=921"
bigdata = requests.get(url)
jbigdata = bigdata.json()
# this is a triple nested dict {'items': [{'id': 24739, 'title': "'Awvea Tsamsiyu Armor", 'url': '/wiki/%27Awvea_Tsamsiyu_Armor', 'ns': 0},
entries = 920

while entries != -1:

    title = jbigdata["items"][entries]["title"]
    baseurl = jbigdata["items"][entries]["url"]
    fullurl = "http://www.james-camerons-avatar.wikia.com/" + baseurl
    finallinks = ""

    page = requests.get(fullurl) # Get page to obtain URLS
    soup = bs4.BeautifulSoup(page.text, "lxml")

    for link in soup.find_all('a'):
        rawlinks = link.get('href')
        try:
            if "//" not in rawlinks and "#" not in rawlinks and "/wiki/Special:" not in rawlinks: # Removes special links, tags and // links
                finallinks += (rawlinks + "\n")
        except TypeError: # unknown error, must be passed to continue
            pass
    #rate of 2.5 results per second
    print("#" + str(entries))
    print("Title: " +  title)
    print("Article URL:" + fullurl)
    print("Links: \n" + finallinks)
    print("#" + str(entries))
    print("*****")
    entries -= 1


# OBEJCTIVE:
    #  get all hyperlinks in all articles from a wikia

# USEFUL RESOURCES :
    # bs4
    # https://github.com/Timidger/Wikia
    # https://github.com/WikiTeam/wikiteam
    # http://marvel.wikia.com/api/v1#!/Articles
    # https://web.archive.org/web/20150906003340/http://api.wikia.com/wiki/Wikia_Content_API
    # https://realpython.com/python-json/

# PLANNING:
    # get an index for all the pages on the wikia
        # using WIKIAPI/api/v1/Articles/Details to list all 971 articles
        # This thing returns a json with article title and URL to it && UID
    # make a request to each page
        # Use requests
    # get all hyperlinks from page
        # Beautifulsoup.findall("a")
    # Write it to a new json
    # {
    #       "title": "Bad Brains",
    #       "url": "/wiki/%22Bad_Brains%22_Brent_Bennigan",
    #       "refs": "href="/wiki/Quick_Start",
    #       "categories":
    #    },
    # get media from page
        #using https://github.com/WikiTeam/wikiteam download images per page
# PC
#
#data = call WIKIAPI/api/v1/Articles/Details
#for each_entry_in (data)
    #request = data.url
    #refs = beautifulsoup.get("a")
    #json.add(data.url, data.title, refs)
    #getimages(request)
#
#def getimages(domain)
    #makedir
    #call "dumpgenerator.py + domain + --images"
#
#def json.add(data2add)
    #open data.json
    #write data2add
    #close data.json
