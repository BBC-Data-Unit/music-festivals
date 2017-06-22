# Festivals dominated by male acts, study shows, as Glastonbury begins

![](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/festivalfemalesgif.gif)

In June 2017 we [published an analysis of music festival data](http://www.bbc.co.uk/news/uk-england-40273193) which highlighted the scarcity of female headliners, the dominance of 20 acts which make up a quarter of all headline slots, how Glastonbury headliners are getting older, and the rise of pop and hip hop and decline of electronic and rock.

BBC England's data unit analysed more than 600 separate headline performances across 14 UK festivals. They were: Download, Reading/Leeds, T in the Park, V Festival, Isle of Wight, Bestival, Latitude, Wireless, Rewind, End of the Road, Cornbury, Boardmasters and Lovebox.
Festivals that were not defined around headline acts were excluded. These include Creamfields, Boomtown Fair and Womad. Fairport's Cropredy Convention was also excluded as it is traditionally headlined by its organisers.

## Get the data

* [CSV: Headliners for each festival, including demographic data](https://github.com/BBC-Data-Unit/music-festivals/blob/master/festival_headliners.csv)
* [Excel spreadsheet: headliner demographics summary tables](https://github.com/BBC-Data-Unit/music-festivals/blob/master/festivaldata-withcalcs.xlsx)
* [CSV: Headliner IDs, names, related artists, top tracks, popularity, from Spotify API](https://github.com/BBC-Data-Unit/music-festivals/blob/master/spotifydata.csv)
* [CSV: Headliners by festival with Spotify genres](https://github.com/BBC-Data-Unit/music-festivals/blob/master/appearance_plus_genres.csv)
* [CSV: Genre frequency count](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/genrecount.csv)
* [CSV: Genre count times appearances](https://github.com/BBC-Data-Unit/music-festivals/blob/master/genrecount_x_appearances.csv)
* [CSV: Relationships between artists](https://raw.githubusercontent.com/BBC-Data-Unit/music-festivals/master/relationships_between_artists.csv) - includes non-headliners
* [CSV: Relationships between artists - headliners only](https://github.com/BBC-Data-Unit/music-festivals/blob/master/relationships_headlinersonly.csv)
* [Spotify IDs and names for festival headliners and related artists](https://github.com/BBC-Data-Unit/music-festivals/blob/master/artistidlookup.csv) - related artists include non-headliners
* [CSV: MusicBrainz IDs and Spotify IDs for headliners](https://github.com/BBC-Data-Unit/music-festivals/blob/master/headliners_musicbrainzids.csv)

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
* [R script for converting list column into popularity lookup table](https://github.com/BBC-Data-Unit/music-festivals/blob/master/createlookup.R)
* [R script for converting table into data that can be used for network analysis](https://github.com/BBC-Data-Unit/music-festivals/blob/master/createnetworktable.R)
* All these scripts can be used as part of the [R project](https://github.com/BBC-Data-Unit/music-festivals/blob/master/spotify.Rproj)
