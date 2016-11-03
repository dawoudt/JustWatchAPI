import requests

class JustWatch:
	def __init__(self, **kwargs):
		self.kwargs = kwargs
	def search_for_item(self, **kwargs):
		if kwargs:
			self.kwargs = kwargs
		null = None
		payload = {
			"content_types":null,
			"presentation_types":null,
			"providers":null,
			"genres":null,
			"languages":null,
			"release_year_from":null,
			"release_year_until":null,
			"monetization_types":null,
			"min_price":null,
			"max_price":null,
			"scoring_filter_types":null,
			"cinema_release":null,
			"query":null
		}
		for key, value in self.kwargs.items():
			if key in payload.keys():
				payload[key] = value
			else:
				print('{} is not a valid keyword'.format(key))
		header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'}
		r = requests.post('https://api.justwatch.com/titles/en_AU/popular', json=payload, headers=header)
		return r.json()


