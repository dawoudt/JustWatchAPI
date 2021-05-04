import unittest
from justwatch import justwatchapi, JustWatch
from requests.exceptions import HTTPError


class TestJustWatchAPI(unittest.TestCase):
    def test_header(self):
        ''' Assert header has not changed'''

        expected_header = {'User-Agent': 'JustWatch client (github.com/dawoudt/JustWatchAPI)'}
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

    def test_locale_defaults_correctly(self):
        ''' Test that locale defaults to en_AU '''

        just_watch = JustWatch(country='NotRealCountry')
        self.assertEqual(just_watch.locale, 'en_AU')
        res = just_watch.search_for_item(query='the matrix', page_size=1)
        self.assertIsNotNone(res)

    def test_locale_works_with_full_country_name(self):
        '''Test that full country name can be used to get locale '''

        just_watch = JustWatch(country='Australia')
        self.assertEqual(just_watch.locale, 'en_AU')
        res = just_watch.search_for_item(query='the matrix', page_size=1)
        self.assertIsNotNone(res)

    def test_get_providers(self):
        just_watch = JustWatch(country='US')
        prov = just_watch.get_providers()
        self.assertIsNotNone(prov)

    def test_get_genres(self):
        just_watch = JustWatch(country='US')
        genres = just_watch.get_genres()
        self.assertIsNotNone(genres)
        self.assertGreater(len(genres), 2)

    def test_get_title(self):
        the_matrix_title_id = '10'
        just_watch = JustWatch()
        titles = just_watch.get_title(the_matrix_title_id)
        self.assertIsNotNone(titles)
        self.assertGreater(len(titles), 0)

    def test_search_title_id(self):
        just_watch = JustWatch()
        title_ids = just_watch.search_title_id(query='the matrix')
        self.assertIn('The Matrix', title_ids.values())

    def test_person_detail(self):
        just_watch = JustWatch()
        person_detail = just_watch.get_person_detail(3036)
        self.assertIn('Keanu Reeves', person_detail.values())

            

if __name__ == '__main__':
    unittest.main()
