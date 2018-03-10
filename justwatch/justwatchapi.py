import requests
from babel import Locale

HEADER = {'User-Agent':'JustWatch Python client (github.com/dawoudt/JustWatchAPI)'}

class JustWatch:
	def __init__(self, country='AU', **kwargs):
		self.kwargs = kwargs
		self.country = country
		self.language = Locale.parse('und_{}'.format(self.country)).language
		self.locale = self.language + '_' + self.country
        
		
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
			"query":null,
			"page":null,
			"page_size":null
		}
		for key, value in self.kwargs.items():
			if key in payload.keys():
				payload[key] = value
			else:
				print('{} is not a valid keyword'.format(key))
		header = HEADER
		api_url = 'https://api.justwatch.com/titles/{}/popular'.format(self.locale)
		r = requests.post(api_url, json=payload, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()

	def get_providers(self):

		header = HEADER
		api_url = 'https://apis.justwatch.com/content/providers/locale/{}'.format(self.locale)
		r = requests.get(api_url, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()
        
	def get_genres(self):

		header = HEADER
		api_url = 'https://apis.justwatch.com/content/genres/locale/{}'.format(self.locale)
		r = requests.get(api_url, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()

	def get_title(self, title_id, content_type='movie'):

		header = HEADER
		api_url = 'https://apis.justwatch.com/content/titles/{}/{}/locale/{}'.format(content_type, title_id, self.locale)
		r = requests.get(api_url, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()
        
