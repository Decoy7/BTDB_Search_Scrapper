# NO LONGER WORKS CAUSE OF CLOUDFLARE PROTECTION
# BTDB Search Scrapper
<!---
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
-->

## Modules Used
  - BeautifulSoup4
  - Requests
  - Random

## Features
- Enter a search term and get the results in json format.
## Json Structure
   ```json
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
- Categories you can pass.
   * "top" to get the top torrents of the day
   * "length" to get by size (bigger in size first)
   * "popular" to get by popularity (most seeders and leechers first)
   * "hits" to get by times downloaded (most downloaded torrents first)

- Make the search and store the result.
   ```python
   from btdb import btdb_eu
   movies=btdb_eu.search("matrix",order_by="popular")
   ```
- Go through all of the names one by one.
   ```python
   for movie in range(len(movies)):
      print(movies[movie]["title"])
   ```
- Go through each size of each movie.
   ```python
   for movie in range(len(movies)):
      print(movies[movie]["size"])
   ```
