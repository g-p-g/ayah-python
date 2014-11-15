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
        captcha = ayah.Ayah(
            publisher_key=publisher_key,
            scoring_key=scoring_key,
            ws_host=ws_host)
        # Verify
        self.assertEqual(captcha.config['publisher_key'], publisher_key)
        self.assertEqual(captcha.config['scoring_key'], scoring_key)
        self.assertEqual(captcha.config['ws_host'], ws_host)
        self.assertEqual(captcha.config['publisher_url'], publisher_url)
        self.assertEqual(captcha.config['publisher_html'], publisher_html)
        self.assertEqual(captcha.config['scoring_url'], scoring_url)


if __name__ == '__main__':
    unittest.main()
