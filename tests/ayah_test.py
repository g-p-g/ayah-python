import ayah
import unittest

class AyahTestCase(unittest.TestCase):

    def test_configure(self):
        # Set up
        publisher_key = 'PUBLISHER_KEY'
        scoring_key = 'SCORING_KEY'
        ws_host = 'WS_HOST'
        publisher_url = 'https://' + ws_host + '/ws/script/' + publisher_key
        publisher_html = '<div id="AYAH"></div><script type="text/javascript" src="' + publisher_url + '"></script>'
        scoring_url = 'https://' + ws_host + '/ws/scoreGame'
        # Exercise
        ayah.configure(
            publisher_key=publisher_key,
            scoring_key=scoring_key,
            ws_host=ws_host)
        # Verify
        self.assertEqual(ayah.ayah.config['publisher_key'], publisher_key)
        self.assertEqual(ayah.ayah.config['scoring_key'], scoring_key)
        self.assertEqual(ayah.ayah.config['ws_host'], ws_host)
        self.assertEqual(ayah.ayah.config['publisher_url'], publisher_url)
        self.assertEqual(ayah.ayah.config['publisher_html'], publisher_html)
        self.assertEqual(ayah.ayah.config['scoring_url'], scoring_url)
        # Clean up

    def test_get_publisher_html_no_configure(self):
        # Set up
        ayah.ayah.config = None
        # Exercise
        # Verify
        self.assertRaises(Exception, ayah.get_publisher_html)
        # Clean up

    def test_score_result_no_configure(self):
        # Set up
        ayah.ayah.config = None
        # Exercise
        # Verify
        self.assertRaises(Exception, ayah.get_publisher_html)
        # Clean up

if __name__ == '__main__':
    unittest.main()
