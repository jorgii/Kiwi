import http.client
from django.test import TestCase


class XMLRPCViewTest(TestCase):
    def test_xmlrpc_info_page_loads(self):
        # test for https://github.com/kiwitcms/Kiwi/issues/80
        response = self.client.get('/xmlrpc/')

        self.assertEqual(http.client.OK, response.status_code)
        self.assertContains(response, 'Kiwi TCMS XML-RPC Service')
        self.assertContains(response, '<li class="xmlrpc_method">')