import unittest
from justwatch import justwatchapi, JustWatch
from requests.exceptions import HTTPError


class TestJustWatchAPI(unittest.TestCase):
    def test_header(self):
        ''' Assert header has not changed'''

        expected_header = {'User-Agent': 'JustWatch Python client (github.com/dawoudt/JustWatchAPI)'}
        header = justwatchapi.HEADER
        self.assertEqual(header, expected_header)

    def test_get(self):
        '''Test that we at least don't fail to get a response'''

        just_watch = JustWatch(country='US')
        try:
            just_watch.search_for_item(query='the matrix', page_size=1)
        except Exception as e:
            self.fail(f"test_get() failed with Exception: {e}")  # noqa

    def test_results_contains_query_item(self):
        '''Test that searching for something correctly returns correct results'''

        search_item = 'the matrix'

        just_watch = JustWatch(country='US')
        results = just_watch.search_for_item(query=search_item, page_size=1)
        first_result_title = results['items'][0]['title'].lower()

        self.assertEqual(search_item, first_result_title)


if __name__ == '__main__':
    unittest.main()
