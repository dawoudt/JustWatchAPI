# JustWatchAPI

JustWatch.com Python 3 API

## Install
```bash
python3 -m pip install JustWatch
```
## How To 
####search for an item
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



##### Note: Default country is AU
#### Read api_payload.txt for more information
