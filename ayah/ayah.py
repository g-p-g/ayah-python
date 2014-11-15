import json
import urllib
import urllib2

class Ayah(object):

    def __init__(self, publisher_key, scoring_key, **kwargs):
        """
        publisher_key
            Identifies you and your application to areyouahuman.com.
        scoring_key
            Used to retrieve pass or fail results from areyouahuman.com.
        """
        self.config = configure(publisher_key, scoring_key, **kwargs)

    def get_publisher_html(self):
        """
        Gets the HTML markup that displays the PlayThru content to the
        alleged human. When the alleged human finishes the PlayThru challenge,
        pass the value of the hidden input field with id='session_secret'
        to score_result().
        """
        return self.config['publisher_html']

    def score_result(self, session_secret):
        """
        Returns True or False indicating whether the alleged human succeeded
        in satisfying the PlayThru challenge.

        session_secret
            Pass in the value of the hidden input field with id='session_secret'.
        """
        data = {
            'scoring_key': self.config['scoring_key'],
            'session_secret': session_secret
        }
        values = urllib.urlencode(data)
        response = urllib2.urlopen(self.config['scoring_url'], values)
        success = False
        if response.code == 200:
            content = response.readline()
            data = json.loads(content)
            success = (data['status_code'] == 1)
        return success

    def record_conversion(self, session_secret):
        """
        Returns the HTML needed to be embedded in the confirmation page
        after a form submission. Once the code loads on the page it will
        record a conversion with our system.

        session_secret
            Pass in the value of the hidden input field with id='session_secret'
        """
        conversion_url = (
            '<iframe style="border: none;" height="0" width="0"',
            ' src="https://%s/ws/recordConversion/%s"></iframe>'
        ) % (self.config['ws_host'], session_secret)
        return conversion_url


def configure(publisher_key, scoring_key, ws_host='ws.areyouahuman.com'):
    """
    Sets the publisher key and scoring key needed to make subsequent
    calls to the areyouahuman API.

    publisher_key
        Identifies you and your application to areyouahuman.com.
    scoring_key
        Used to retrieve pass or fail results from areyouahuman.com.
    ws_host
        Web service host for areyouahuman calls (no trailing slash).
        Defaults to 'ws.areyouahuman.com'.
    """
    publisher_url = 'https://%s/ws/script/%s' % (
        ws_host, urllib2.quote(publisher_key, safe=''))
    publisher_html = (
        '<div id="AYAH"></div>'
        '<script type="text/javascript" src="%s"></script>'
    ) % publisher_url
    scoring_url = 'https://%s/ws/scoreGame' % ws_host

    config = {
        'publisher_key': publisher_key,
        'scoring_key': scoring_key,
        'ws_host': ws_host,
        'publisher_url': publisher_url,
        'publisher_html': publisher_html,
        'scoring_url': scoring_url
    }
    return config
