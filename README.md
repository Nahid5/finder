# finder
Using public searchengines to find vulns and secrets

## googleScraper
Scrape google using google custom search engine to bypass rate limiting issues

* Go to https://console.developers.google.com/ and generate API key
* Go to https://cse.google.com/cse/all and generate the search engine ang get the id
Scope the search engine to no site and set the dropdown to search the entire web.

Copy the .example.env to .env and place your google api keys there with 3 pipes as the delimieter. You can enter multiple keys using new line as the delimieter.

API_KEY|||SEARCH_ENGINE_ID

Ex.
* asdasdsadsdasdsdasdasdasd|||1234567890989764345345:23d23d223d3d2
* f34q34f334f3i3dj3odi3jdo2|||1234567890989764345345:23d23d223d3d2

Usage:
* ./googlescraper.py [TARGET] | tee output.txt


## Bing Scraper
Scrape sites using bing.

Get a bing api key from the azure portal:

Cognative Services -> Add -> Bing Search

The free F1 tier should work but you need to add the  -t flag to add in a timeout to keep inline with the 3 searches per second.

Change the *search_url* to your url.

Your API keys and endpoint can be found by clicking Cognative Services -> <What you just created> -> Keys and Endpoint

* Note the ENDPOINT from azure doesnt have the /search after the api version. So if you receive an error, add /search to the end of your endpoint

Place your api key in a file called .env in the bing directory.

Usage:
* ./bingScraper.py -i SITE_LIST.txt -o OUTPUT.txt