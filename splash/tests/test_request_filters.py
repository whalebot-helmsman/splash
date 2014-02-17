# -*- coding: utf-8 -*-
from __future__ import absolute_import
from splash.tests import ts
from splash.tests.test_render import BaseRenderTest


class FiltersTestHTML(BaseRenderTest):

    def test_filtering_work(self):
        r = self.request({'url': ts.mockserver.url('iframes')})
        self.assertIn('SAME_DOMAIN', r.text)
        self.assertIn('OTHER_DOMAIN', r.text)

        r = self.request({'url': ts.mockserver.url('iframes'), 'filters': 'noscript'})
        self.assertNotIn('SAME_DOMAIN', r.text)
        self.assertIn('OTHER_DOMAIN', r.text)

        r = self.request({'url': ts.mockserver.url('iframes'), 'filters': 'noscript2'})
        self.assertIn('SAME_DOMAIN', r.text)
        self.assertNotIn('OTHER_DOMAIN', r.text)

    def test_multiple_filters(self):
        r = self.request({'url': ts.mockserver.url('iframes'), 'filters': 'noscript,noscript2'})
        self.assertNotIn('SAME_DOMAIN', r.text)
        self.assertNotIn('OTHER_DOMAIN', r.text)

    def test_invalid_filters(self):
        r = self.request({'url': ts.mockserver.url('iframes'), 'filters': 'nozcript,noscript2'})
        self.assertEqual(r.status_code, 400)
        self.assertIn('nozcript', r.text)
