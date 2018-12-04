import unittest
from justwatch import justwatchapi, JustWatch
from requests import Session
from requests.exceptions import HTTPError
import sys


class TestJustWatchAPI(unittest.TestCase):
    def setUp(self):
        self.just_watch = JustWatch(country='US')

    def tearDown(self):
        self.just_watch.requests.close()

    def test_using_session(self):
        self.assertIsInstance(self.just_watch.requests, Session)

    def test_header(self):
        ''' Assert header has not changed'''

        expected_header = {'User-Agent': 'JustWatch Python client (github.com/dawoudt/JustWatchAPI)'}
        header = justwatchapi.HEADER
        self.assertEqual(header, expected_header)

    def test_get(self):
        '''Test that we at least don't fail to get a response'''

        try:
            self.just_watch.search_for_item(query='the matrix', page_size=1)
        except Exception as e:
            self.fail(f"test_get() failed with Exception: {e}")  # noqa

    def test_results_contains_query_item(self):
        '''Test that searching for something correctly returns correct results'''

        search_item = 'the matrix'

        just_watch = JustWatch(country='US')
        results = self.just_watch.search_for_item(query=search_item, page_size=1)
        first_result_title = results['items'][0]['title'].lower()

        self.assertEqual(search_item, first_result_title)

    def test_get_providers(self):
        ''' Test we actually get providers '''

        try:
            self.just_watch.get_providers()
        except Exception as e:
            self.fail(f"test_get_providers() failed with Exception: {e}")  # noqa

    def test_providers_has_netflix(self):
        ''' Test we get netflix as a provider '''

        res = self.just_watch.get_providers()
        has_netlix = any('netflix' == prov['technical_name'] for prov in res)
        self.assertTrue(has_netlix)

    def test_get_genres(self):
        ''' Test we get some genres back'''

        try:
            self.just_watch.get_genres()
        except Exception as e:
            self.fail(f"test_get_genres() failed with Exception: {e}")  # noqa

    def test_get_title(self):
        ''' Test we get some genres back'''
        the_matrix_title_id = 10

        try:
            self.just_watch.get_title(the_matrix_title_id)
        except Exception as e:
            self.fail(f"test_get_title() failed with Exception: {e}")  # noqa


if __name__ == '__main__':
    unittest.main()
