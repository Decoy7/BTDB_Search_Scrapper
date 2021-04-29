# BTDB Search API
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Modules Used
  - BeautifulSoup4
  - Requests
  - Random

## Features
- Enter a search term and get the results in json format.
## Json Structure
   ```python:
{
       "title": string,
       "size": string,
       "seeds": string,
       "leeches": string,
       "magnet": string,
       "torrent": string,
       "desc_link": string,
       "added": string
}
   ```
## Examples
- Make the search and store the result.
   ```python:
   from btdb import btdb_eu
   movies=btdb_eu.search("matrix",order_by="popular")
   ```
- Go through all of the names one by one.
   ```python:
   for i in range(len(movies)):
      print(movies[i]["title"])
   ```
- Go through each size of each movie.
   ```python:
   for i in range(len(movies)):
      print(movies[i]["size"])
   ```
