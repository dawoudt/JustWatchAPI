# Unofficial JustWatch API
[![Build Status](https://travis-ci.com/dawoudt/JustWatchAPI.svg?branch=master)](https://travis-ci.com/dawoudt/JustWatchAPI)

JustWatch.com Python 3 API

## Install
```bash
python3 -m pip install JustWatch
```

## Disclaimer

**This is not the official JustWatch API.**

The work of many developers went and is still going into the development and maintenance of the data and the API. The main business of JustWatch is to operate a streaming guide with apps for iOS, Android and TV that offers the data for business intelligence and marketing. Therefore it is prohibited to use the API for commercial purposes, meaning all purposes intended for, or directed towards, commercial advantage or monetization by an individual or organization (consumer service, data science, business intelligence etc.). The API may be used for non-commercial purposes such as private projects, but please be respectful with your API calls to prevent an overload on the API.

JustWatch does not warrant that the API is free of inaccuracies, errors, bugs, malicious code or interruptions or that it is reliable, flawless, complete or otherwise valid. JustWatch does not warrant that the API will meet your requirements, will be available without interruption, or that the results from its use will be accurate or reliable, the quality of the products, services, information or other materials received through the API meets your expectations, and errors regarding the API are corrected. Use of the API is at your sole discretion and risk. You are solely responsible for any damages resulting from your use of the API, including damage to its system or loss of data. JustWatch can disable and change the API at any time without notice and without giving any reason. JustWatch excludes any liability to the extent permitted for direct, indirect or incidental damages, consequential damages, lost profits, quantifiable pecuniary losses arising out of or in connection with the use of the API.
Incorrect or prohibited use of the API, for example for commercial use, may result in a claim for damages by JustWatch.

If you would like to work with JustWatch and use the official Data API take a look at JustWatch Media and contact us at data-partner@justwatch.com. Currently, JustWatch can only work with bigger partners and clients. JustWatch is also hiring: https://www.justwatch.com/us/talent and has some interesting open source projects on GitHub.

## How To
#### search for an item
```python
from justwatch import JustWatch

just_watch = JustWatch(country='US')

results = just_watch.search_for_item(query='the matrix')
```
#### or search for combination of genres
```python
just_watch = JustWatch(genres=['act', 'scf', 'hrr'])

results_by_genres = just_watch.search_for_item()
```
#### or maybe search by provider
```python
just_watch = JustWatch()

results_by_providers = just_watch.search_for_item(providers=['nfx', 'stn'])
```

#### or possibly a combination of the above 
```python
just_watch = JustWatch()

results_by_multiple = just_watch.search_for_item(
    providers=['nfx', 'stn'], 
    content_types=['movie'], 
    monetization_types=['free'])
```

#### search for a person
```python
just_watch = JustWatch()
results = just_watch.search_for_item(query="Keanu Reeves",
    content_types=['person'])
```

#### search for items of a person
```python
just_watch = JustWatch()
titles_person = just_watch.search_for_item(person_id=3036)
```

#### get list of genres and codes
```python
just_watch = JustWatch(country='GB')
genre_details = just_watch.get_genres()

```

#### get list of providers for a country
```python
just_watch = JustWatch(country='DE')
provider_details = just_watch.get_providers()

```

#### get further details on a movie or tv program

Based on title id found in previous search

```python
just_watch = JustWatch(country='GB')
megamind = just_watch.get_title(title_id=103561)
dark = just_watch.get_title(title_id=55668, content_type='show')

```

#### You can query for title IDs

```python
just_watch = JustWatch(country='GB')
the_matrix = just_watch.search_title_id(query='the matrix')

{'The Matrix': 10, 'The Matrix Revisited': 30701, ...}

```

#### get further defails on a specific season of a tv program

`season_id` can be found in the response from get_title of a tv program

```python
just_watch = JustWatch(country='GB')
hannibal_season2 = just_watch.get_season(season_id=20236)

```

#### get country specific certification details

```python
just_watch = JustWatch(country='GB')
certs = just_watch.get_certifications()

```

content_type can be specified but (for GB at least) setting to 'show' gives less detail than the default of 'movie'


#### get cinema details

Setting ```"monetization_types" to "cinema"``` and possibly setting ```nationwide_cinema_releases_only = True``` will return a list of potential showings.

```python
just_watch = JustWatch(country='GB')
cinema_showings = just_watch.search_for_item(monetization_types='cinema')

```

Then based on title_id obtained from that search

```python
cinema_times = just_watch.get_cinema_times(title_id=this_title_id,
                                           date='2018-03-24',
                                           latitude=51.5287718,
                                           longitude=-0.2416809,
                                           radius=20000)
```
This will return details of all the showings in the area.  Details of all the cinemas in the area can be obtained by a call to ```get_cinema_details()```.  This takes the same latitutde, longitude and radius parameters as ```get_cinema_times()```, and if a call has already been made they'll be reused.

```python
local_cinemas = just_watch.get_cinema_details()
```

You can then join the data from the two calls by joining ```'cinema_id'``` from ```get_cinema_times()``` with ```'id'``` from ```get_cinema_details()```

#### get upcoming cinema details

Call ```get_upcoming_cinema()``` with number of weeks forward or back and whether you only require national releases

```python
showings_last_week = just_watch.get_upcoming_cinema(weeks_offset=-1, nationwide_cinema_releases_only=True)
showings_three_weeks = just_watch.get_upcoming_cinema(weeks_offset=3, nationwide_cinema_releases_only=False)
```

#### get person details

```python
        just_watch = JustWatch()
        person_detail = just_watch.get_person_detail(3036)
```

##### Notes: 
* Default country is AU
* `person_id` is a justwatch specific id and does not work with imdb or tmdb ids. 
You can get the `person_id` for example from the credits of a title or from search.

#### Read api_payload.txt for more information

## Contributions
### Contributions are welcome!
Please write unit tests for any new functionality :)
