from .base_test import BaseTest, MockSendGridAPIClientRequest
import os
try:
    import unittest2 as unittest
except ImportError:
    import unittest
try:
    from StringIO import StringIO
except ImportError:  # Python 3
    from io import StringIO

import sendgrid
from sendgrid.client import SendGridAPIClient
from sendgrid.version import __version__

SG_KEY  = os.getenv('SG_KEY') or 'SENDGRID_APIKEY'

class TestASMGroups(unittest.TestCase):
    def setUp(self):
        SendGridAPIClient = MockSendGridAPIClientRequest
        self.client = SendGridAPIClient(SG_KEY)
        
    def test_apikeys_init(self):
        self.asm_groups = self.client.asm_groups
        self.assertEqual(self.asm_groups.base_endpoint, "/v3/asm/groups")
        self.assertEqual(self.asm_groups.endpoint, "/v3/asm/groups")
        self.assertEqual(self.asm_groups.client, self.client)

    def test_asm_groups_get(self):
        status, msg = self.client.apikeys.get()
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()