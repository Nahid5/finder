# finder
Using public searchengines to find vulns and secrets

## googleScraper
Scrape google using google custom search engine to bypass rate limiting issues

* Go to https://console.developers.google.com/ and generate API key
* Go to https://cse.google.com/cse/all and generate the search engine ang get the id
Scope the search engine to no site and set the dropdown to search the entire web.

Copy the .example.env to .env and place your google api keys there with 3 pipes as the delimieter. You can enter multiple keys using new line as the delimieter.

API_KEY|SEARCH_ENGINE_ID

Ex.
* asdasdsadsdasdsdasdasdasd|||1234567890989764345345:23d23d223d3d2
* f34q34f334f3i3dj3odi3jdo2|||1234567890989764345345:23d23d223d3d2

Usage:
* ./googlescraper.py [TARGET] | tee output.txt