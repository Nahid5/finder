#!/usr/bin/env python3
# Bing dorks https://help.bing.microsoft.com/#apex/18/en-US/10001/-1
import requests
import sys
import time
import argparse

SUBSCRIPTION_KEY = ""
BASE_URL = ""
with open(".env", "r") as fil:
    for line in fil:
        row = line.strip()
        if("API_KEY=" in row):
            SUBSCRIPTION_KEY = row.replace("API_KEY=", "")
        if("URL=" in row):
            BASE_URL = row.replace("URL=", "")

def doDork(args):
    '''
    '''
    # target = args.input
    outputFile = open(args.output, 'w+')

    target_sites = []
    with open(args.input) as f:
        target_sites = f.read().splitlines()

    # Load dorks
    dorksList = []
    with open("dorks.txt", 'r') as res:
        for line in res:
            dorksList.append(line.strip())

    # Search
    headers = {"Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY}

    for site in target_sites:
        print("################################################## " + site + " ##################################################")
        outputFile.write("################################################## " + site + " ##################################################")
        outputFile.write("\n")
        for dork in dorksList:
            '''
            '''
            drk = "site:" + site + " " + dork
            params = {"q": drk, "textDecorations": True, "textFormat": "HTML"}
            search_results = requests.get(BASE_URL, headers=headers, params=params).json()

            print("------------------------------------------------" + drk + "------------------------------------------------")
            outputFile.write("------------------------------------------------" + drk + "------------------------------------------------")
            outputFile.write("\n")
            try:
                for res in search_results['webPages']['value']:
                    try:
                        print("Title: " + res['name'])
                        outputFile.write("Title: " + res['name'])
                        outputFile.write("\n")
                    except Exception as e:
                        pass
                    try:
                        print("URL: " + res['url'])
                        outputFile.write("URL: " + res['url'])
                        outputFile.write("\n")
                    except Exception as e:
                        pass
                    try:
                        print("Snippet: " + res['snippet'])
                        outputFile.write("Snippet: " + res['snippet'])
                        outputFile.write("\n")
                    except Exception as e:
                        pass
                    try:
                        print("Last Crawled: " + res['dateLastCrawled'])
                        outputFile.write("Last Crawled: " + res['dateLastCrawled'])
                        outputFile.write("\n")
                    except Exception as e:
                        pass 
                    print("\n\n")
                    outputFile.write("\n\n")
            except Exception as e:
                pass
            if(args.timeout):
                time.sleep(1)
            outputFile.flush()
        outputFile.write("\n\n")
    outputFile.close()


if (__name__ == '__main__'):
    parser = argparse.ArgumentParser(description='Use Bing API to get find vulns for a website')
    parser.add_argument('-i', '--input', help='Target sites', type=str, required=True)
    parser.add_argument('-o', '--output', help='Output file name', type=str, required=True)
    parser.add_argument('-t', '--timeout', help='1 Second timeout if using the free tier', action='store_true')
    args = parser.parse_args()

    doDork(args)