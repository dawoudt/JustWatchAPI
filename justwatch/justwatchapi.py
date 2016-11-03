"""
	-- json payload values --
	values can be null (None), or each or all items in corresponding list
		"content_types": -- null or ['movie', 'show']
		"presentation_types": -- null or ['hd', 'sd']
		"providers": -- null or ["mbi", "qfs", "tpl", "msf", "pls", "ply", "itu", "ddi", "crk", "qfx", "prs", "stn", "nfx"]
		"genres": -- null or ["act", "ani", "cmy", "crm", "drm", "msc", "hrr", "hst", "fnt", "trl", "war", "wsn", "rma", "scf","doc", "fml", "spt"]
		"languages": -- null
		"release_year_from": -- null or year > 1900
		"release_year_until": -- null or year < current year
		"monetization_types": -- null or ["flatrate", "ads", "rent", "buy", "free"]
		"min_price": -- null or integer value
		"max_price": -- null or integer value,
		"scoring_filter_types": -- null or
						{
						"imdb:score":
							{
							"min_scoring_value":0.0,"max_scoring_value":10.0
							},
						"tomato:meter":
							{
							"min_scoring_value":0,"max_scoring_value":100
							}
						},
		"cinema_release": -- null,
		"query": -- null or title as string 
		}
	shortened values 

	providers
	-- 
		mbi - mubi
		qfs - quickflix store
		tpl - tenplay
		msf - micrsoft
		pls - playstation
		ply - google play store
		itu - itunes
		ddi - dendy direct
		crk - crackle
		qfx - quickflix
		prs - presto
		stn - stan
		nfx - netflix

	genres
	--
		act - action
		ani - animation
		cmy - comedy
		crm - crime
		drm - drama
		msc - music and musical
		hrr - horror
		hst - historu
		fnt - fantasy
		trl - mystery and thriller 
		war - war
		wsn - western
		rma - romance
		scf - scifi
		doc - documentary
		fml - kids and family
		spt - sport
	
"""

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


