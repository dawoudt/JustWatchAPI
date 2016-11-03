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
#### Note: Default location is AU
##### Read api_payload.txt for more information
