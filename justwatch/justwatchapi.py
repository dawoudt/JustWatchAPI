from datetime import datetime
from datetime import timedelta
import requests
from babel import Locale

HEADER = {'User-Agent':'JustWatch Python client (github.com/dawoudt/JustWatchAPI)'}

class JustWatch:
	def __init__(self, country='AU', use_sessions=True, **kwargs):
		self.kwargs = kwargs
		self.country = country
		self.language = Locale.parse('und_{}'.format(self.country)).language
		self.locale = self.language + '_' + self.country
		self.kwargs_cinema = []
		if use_sessions:
			self.requests = requests.Session()
		else:
			self.requests = requests
		
	def search_for_item(self, **kwargs):
		if kwargs:
			self.kwargs = kwargs
		null = None
		payload = {
			"age_certifications":null,
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
			"nationwide_cinema_releases_only":null,
			"scoring_filter_types":null,
			"cinema_release":null,
			"query":null,
			"page":null,
			"page_size":null,
			"timeline_type":null
		}
		for key, value in self.kwargs.items():
			if key in payload.keys():
				payload[key] = value
			else:
				print('{} is not a valid keyword'.format(key))
		header = HEADER
		api_url = 'https://api.justwatch.com/titles/{}/popular'.format(self.locale)
		r = self.requests.post(api_url, json=payload, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()

	def get_providers(self):

		header = HEADER
		api_url = 'https://apis.justwatch.com/content/providers/locale/{}'.format(self.locale)
		r = self.requests.get(api_url, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()
        
	def get_genres(self):

		header = HEADER
		api_url = 'https://apis.justwatch.com/content/genres/locale/{}'.format(self.locale)
		r = self.requests.get(api_url, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()

	def get_title(self, title_id, content_type='movie'):

		header = HEADER
		api_url = 'https://apis.justwatch.com/content/titles/{}/{}/locale/{}'.format(content_type, title_id, self.locale)
		r = self.requests.get(api_url, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()

        
	def get_season(self, season_id):

		header = HEADER
		api_url = 'https://apis.justwatch.com/content/titles/show_season/{}/locale/{}'.format(season_id, self.locale)
		r = self.requests.get(api_url, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()


	def get_cinema_times(self, title_id, content_type = 'movie', **kwargs):

		if kwargs:
			self.kwargs_cinema = kwargs

		null = None
		payload = {
			"date":null,
			"latitude":null,
			"longitude":null,
			"radius":20000
		}
		for key, value in self.kwargs_cinema.items():
			if key in payload.keys():
				payload[key] = value
			else:
				print('{} is not a valid keyword'.format(key))


		header = HEADER
		api_url = 'https://apis.justwatch.com/content/titles/{}/{}/showtimes'.format(content_type, title_id)
		r = self.requests.get(api_url, params=payload, headers=header)

		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()


	def get_cinema_details(self, **kwargs):

		if kwargs:
			self.kwargs_cinema = kwargs

		null = None
		payload = {
			"latitude":null,
			"longitude":null,
			"radius":20000
		}
		for key, value in self.kwargs_cinema.items():
			if key in payload.keys():
				payload[key] = value
			elif key == 'date':
                #ignore the date value if passed
				pass
			else:
				print('{} is not a valid keyword'.format(key))


		header = HEADER
		api_url = 'https://apis.justwatch.com/content/cinemas/{}'.format(self.locale)
		r = self.requests.get(api_url, params=payload, headers=header)

		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()



	def get_upcoming_cinema(self, weeks_offset, nationwide_cinema_releases_only=True):

		header = HEADER
		payload = { 'nationwide_cinema_releases_only': nationwide_cinema_releases_only, 
						'body': {} }
		now_date = datetime.now()
		td = timedelta(weeks=weeks_offset)
		year_month_day = (now_date + td).isocalendar()
		api_url = 'https://apis.justwatch.com/content/titles/movie/upcoming/{}/{}/locale/{}'
		api_url = api_url.format(year_month_day[0], year_month_day[1], self.locale)

		#this throws an error if you go too many weeks forward, so return a blank payload if we hit an error
		try:        
			r = self.requests.get(api_url, params=payload, headers=header)

			# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
			r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

			return r.json()
		except:
			return {'page': 0, 'page_size': 0, 'total_pages': 1, 'total_results': 0,  'items': []}

	def get_certifications(self, content_type = 'movie'):

		header = HEADER
		payload = { 'country': self.country, 'object_type': content_type }
		api_url = 'https://apis.justwatch.com/content/age_certifications'
		r = self.requests.get(api_url, params=payload, headers=header)

		# Client should deal with rate-limiting. JustWatch may send a 429 Too Many Requests response.
		r.raise_for_status()   # Raises requests.exceptions.HTTPError if r.status_code != 200

		return r.json()

