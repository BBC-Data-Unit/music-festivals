# Festivals dominated by male acts, study shows, as Glastonbury begins

![](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/festivalfemalesgif.gif)

In June 2017 we [published an analysis of music festival data](http://www.bbc.co.uk/news/uk-england-40273193) which highlighted the scarcity of female headliners, the dominance of 20 acts which make up a quarter of all headline slots, how Glastonbury headliners are getting older, and the rise of pop and hip hop and decline of electronic and rock.

BBC England's data unit analysed more than 600 separate headline performances across 14 UK festivals. They were: Download, Reading/Leeds, T in the Park, V Festival, Isle of Wight, Bestival, Latitude, Wireless, Rewind, End of the Road, Cornbury, Boardmasters and Lovebox.
Festivals that were not defined around headline acts were excluded. These include Creamfields, Boomtown Fair and Womad. Fairport's Cropredy Convention was also excluded as it is traditionally headlined by its organisers.

## Get the data

* [CSV: Genre frequency count](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/genrecount.csv)
* Spotify IDs for festival headliners

## Visualisation

![](https://ichef.bbci.co.uk/news/624/cpsprodpb/849C/production/_96484933_chart_mostpopular_glasto.png)

* Line chart: Percentage of headline acts by gender each year
* Bar chart: Acts with the most festival headline appearances
* Multiple bar chart: Is rock music in decline? Genre tags associated with headline acts (%)
* Bar chart: How Glastonbury headliners have been getting older

## Multimedia 

* Video: UK festival line-ups dominated by male headliners

## Analysis and code

* [Python scraper which uses the Spotify API to fetch details on a list of headline acts](https://github.com/BBC-Data-Unit/music-festivals/blob/master/spotifyscraper.py)
* [How to do the same thing using a scraper in R](https://github.com/BBC-Data-Unit/music-festivals/blob/master/using_spotify_api.Rmd)
* [Analysing genre using R](https://github.com/BBC-Data-Unit/music-festivals/blob/master/analysingSpotifyGenre.Rmd)
* [Creating data on related artists for a network analysis in R](https://github.com/BBC-Data-Unit/music-festivals/blob/master/SpotifyNetworkAnalysis.Rmd)
* All these scripts can be used as part of the [R project](https://github.com/BBC-Data-Unit/music-festivals/blob/master/spotify.Rproj)
