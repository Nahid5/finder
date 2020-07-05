#!/usr/bin/env python3
import requests
import sys
import argparse

class ApiInfo:
    '''
    '''
    def __init__(self):
        self.API_KEYS = []
        self.API_KEY = ""
        self.SEARCH_ENGINE_ID = ""
        self.loadApiKeys()

    def loadApiKeys(self):
        with open('.env', 'r') as fil:
            for line in fil:
                self.API_KEYS.append({'API_KEY': line.strip().split('|||')[0], 'SEARCH_ENGINE_ID': line.strip().split('|||')[1]})

    def getNextApiKey(self):
        '''
        '''
        try:
            self.API_KEY =self. API_KEYS[0]['API_KEY']
            self.SEARCH_ENGINE_ID = self.API_KEYS[0]['SEARCH_ENGINE_ID']
            del self.API_KEYS[0]
            if(i > 0):
                i -= 1
        except Exception as e:
            pass


def writeResultsToFile(outputFile, res):
    '''
    '''
    for itm in res:
        try:
            print("Title: " + itm['title'])
            outputFile.write("Title: " + itm['title'])
            outputFile.write("\n")
        except Exception as e:
            pass
        try:
            print("Link: " + itm['link'])
            outputFile.write("Link: " + itm['link'])
            outputFile.write("\n")
        except Exception as e:
            pass
        try:
            print("Snippet: " + itm['snippet'])
            outputFile.write("Snippet: " + itm['snippet'])
            print("\n")
        except Exception as e:
            pass
        outputFile.flush()


def doSearch(args):
    '''
    '''
    site = args.input
    outputFile = open(args.output, 'w+')
    query = 'site:' + site

    api = ApiInfo()

    # Load dorks
    DORKS = []
    with open('genericDorks.txt', 'r') as fil:
        for line in fil:
            DORKS.append(line.strip())

    # Target the specific site for stuff
    for i in range(len(DORKS)):
        newQuery = query + " " + DORKS[i]
        url = "https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}".format(API_KEY = api.API_KEY, SEARCH_ENGINE_ID = api.SEARCH_ENGINE_ID, query = newQuery)
        params = {'num': 10, 'start': 0}
        res = requests.get(url, params=params).json()
        try:
            if(res['error']):
                if(len(api.API_KEYS) == 0):
                    print('LOL, no more keys bra. Going into sleep mode')
                    exit(0)
                else:
                    api.getNextApiKey()
        except Exception as e:
            pass

        print("-------------------------------------------------------------------------" + newQuery + "-------------------------------------------------------------------------")
        outputFile.write("-------------------------------------------------------------------------" + newQuery + "-------------------------------------------------------------------------")
        outputFile.write("\n")
        try:
            writeResultsToFile(outputFile, res['items'])
        except Exception as e:
            pass
        

    # Target sites used by devs for secrets
    specificDorks = []
    specificDorks.append('inurl:https://trello.com AND intext:' + site)
    specificDorks.append('site:documenter.getpostman.com ' + site)
    specificDorks.append('site:gist.github.com "password" ' + site.replace('http://', '').replace('http://', '').replace('.com', '').replace('.org', '').replace('.net', ''))
    specificDorks.append('site:stackoverflow.com AND intext:' + site.replace('http://', '').replace('http://', '').replace('.com', '').replace('.org', '').replace('.net', ''))
    for i in range(len(specificDorks)):
        dork = site + " " + specificDorks[i]
        url = "https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}".format(API_KEY = api.API_KEY, SEARCH_ENGINE_ID = api.SEARCH_ENGINE_ID, query = dork)
        params = {'num': 10, 'start': 0}
        res = requests.get(url, params=params).json()

        try:
            if(res['error']):
                if(len(api.API_KEYS) == 0):
                    print('LOL, no more keys bra. Going into sleep mode')
                    exit(0)
                else:
                    api.getNextApiKey()
        except Exception as e:
            pass

        print("-------------------------------------------------------------------------" + dork + "-------------------------------------------------------------------------")
        outputFile.write("-------------------------------------------------------------------------" + dork + "-------------------------------------------------------------------------")
        outputFile.write("\n")
        try:
            writeResultsToFile(outputFile, res['items'])
        except Exception as e:
            pass

if (__name__ == '__main__'):
    parser = argparse.ArgumentParser(description='Use Google Custom Search Engine find vulns for a website')
    parser.add_argument('-i', '--input', help='Target', type=str, required=True)
    parser.add_argument('-o', '--output', help='Output file name', type=str, required=True)
    args = parser.parse_args()

    doSearch(args)