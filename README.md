# JustWatchAPI

JustWatch.com Python 3 API

## How To 
####search for an item
```python
from justwatchapi import JustWatch

just_watch = JustWatch()

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

#### Read api_payload.txt for more information
