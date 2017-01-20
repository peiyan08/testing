import unittest

import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get("/")
        self.assertIn("Please RSVP", result.data)

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        self.assertIn("Party Details", result.data)
        # FIXME: check that once we log in we see party details--but not the form!

    def test_rsvp_mel(self):
        result = self.client.post("/rsvp",
                                  data={'name': 'Jane Doe', 'email': 'mel@ubermelon.com'},
                                  follow_redirects=True)
        self.assertIn("Sorry, Mel. This is kind of awkward.", result.data)
        
        # FIXME: write a test that mel can't invite himself


if __name__ == "__main__":
    unittest.main()