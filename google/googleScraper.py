#!/usr/bin/env python3
import requests
import sys

# Load API Keys
API_KEYS = []
with open('.env', 'r') as fil:
    for line in fil:
        API_KEYS.append({'API_KEY': line.strip().split('|||')[0], 'SEARCH_ENGINE_ID': line.strip().split('|||')[1]})
API_KEY = API_KEYS[0]['API_KEY']
SEARCH_ENGINE_ID = API_KEYS[0]['SEARCH_ENGINE_ID']
del API_KEYS[0]

# Load dorks
DORKS = []
with open('genericDorks.txt', 'r') as fil:
    for line in fil:
        DORKS.append(line.strip())

site = str(sys.argv[1])
query = 'site:' + site

# Target the specific site for stuff
for i in range(len(DORKS)):
    newQuery = query + " " + DORKS[i]
    url = "https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}".format(API_KEY = API_KEY, SEARCH_ENGINE_ID = SEARCH_ENGINE_ID, query = newQuery)
    params = {'num': 10, 'start': 0}
    res = requests.get(url, params=params).json()

    try:
        if(res['error']):
            if(len(API_KEYS) == 0):
                print('LOL, no more keys bra. Going into sleep mode')
                exit(0)
            else:
                API_KEY = API_KEYS[0]['API_KEY']
                SEARCH_ENGINE_ID = API_KEYS[0]['SEARCH_ENGINE_ID']
                del API_KEYS[0]
                if(i > 0):
                    i -= 1
    except Exception as e:
        pass

    print("-------------------------------------------------------------------------" + newQuery + "-------------------------------------------------------------------------")
    try:
        for itm in res['items']:
            print("Title: " + itm['title'])
            print("Link: " + itm['link'])
            print("Snippet: " + itm['snippet'])
            print("\n")
    except Exception as e:
        #print(e)
        print("\n")


# Target sites used by devs for secrets
specificDorks = []
specificDorks.append('inurl:https://trello.com AND intext:' + site)
specificDorks.append('site:documenter.getpostman.com ' + site)
specificDorks.append('site:gist.github.com "password" ' + site.replace('http://', '').replace('http://', '').replace('.com', '').replace('.org', '').replace('.net', ''))
specificDorks.append('site:stackoverflow.com AND intext:' + site.replace('http://', '').replace('http://', '').replace('.com', '').replace('.org', '').replace('.net', ''))
for i in range(len(specificDorks)):
    url = "https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}".format(API_KEY = API_KEY, SEARCH_ENGINE_ID = SEARCH_ENGINE_ID, query = specificDorks[i])
    params = {'num': 10, 'start': 0}
    res = requests.get(url, params=params).json()

    try:
        if(res['error']):
            if(len(API_KEYS) == 0):
                print('LOL, no more keys bra. Going into sleep mode')
                exit(0)
            else:
                API_KEY = API_KEYS[0]['API_KEY']
                SEARCH_ENGINE_ID = API_KEYS[0]['SEARCH_ENGINE_ID']
                del API_KEYS[0]
                if(i > 0):
                    i -= 1
    except Exception as e:
        pass

    print("-------------------------------------------------------------------------" + dork + "-------------------------------------------------------------------------")
    try:
        for itm in res['items']:
            print("Title: " + itm['title'])
            print("Link: " + itm['link'])
            print("Snippet: " + itm['snippet'])
            print("\n")
    except Exception as e:
        #print(e)
        print("\n")
