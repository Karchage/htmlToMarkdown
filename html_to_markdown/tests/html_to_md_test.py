# -*- coding: utf-8 -*-
"""
Tests for html_to_md module
"""

import unittest
import os
import sys

root_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(root_path)

import html_to_md

class Test(unittest.TestCase):
    def test_parse_empty_string(self):
        html_text = u''
        result = html_to_md.html_to_md(html_text)
        expected = u''
        self.assertEqual(result, expected)

    def test_ignored_tags(self):
        html_text = u'<html>Some text</html>'
        result = html_to_md.html_to_md(html_text)
        expected = u'Some text'
        self.assertEqual(result, expected)

    def test_tag_tt(self):
        html_text = u'<tt class="class1" id="1">Some text</tt>'
        result = html_to_md.html_to_md(html_text)
        expected = u'`Some text`'
        self.assertEqual(result, expected)
		
    def test_tag_i(self):
        html_text = u'<i>Italic font</i>'
        result = html_to_md.html_to_md(html_text)
        expected = u'*Italic font*'
        self.assertEqual(result, expected)
		
    def test_tag_b(self):
        html_text = u'<b>Bold font</b>'
        result = html_to_md.html_to_md(html_text)
        expected = u'**Bold font**'
        self.assertEqual(result, expected)

    def test_tag_code(self):
        html_text = u'<code>char arr[] = "abcd";</code>'
        result = html_to_md.html_to_md(html_text)
        expected = u'```char arr[] = "abcd";```'
        self.assertEqual(result, expected)

    def test_tag_h(self):
        html_text = \
            u'''
            <h1>header1;</h1>
            <h2>header2;</h2>
            <h3>header3;</h3>
            <h4>header4;</h4>
            <h5>header5;</h5>
            <h6>header6;</h6>'''
        result = html_to_md.html_to_md(html_text)
        expected = \
            u'''
            # header1;
            ## header2;
            ### header3;
            #### header4;
            ##### header5;
            ###### header6;'''
        self.assertEqual(result, expected)

    def test_tag_u(self):
        html_text = u'<u>Hello</u>'
        result = html_to_md.html_to_md(html_text)
        expected = u'_Hello_'
        self.assertEqual(result, expected)

    def test_tag_small(self):
        html_text = u'<small>This is small text</small>'
        result = html_to_md.html_to_md(html_text)
        expected = u'--This is small text--'
        self.assertEqual(result, expected)

    def test_tag_q(self):
        html_text = u'<q>Hello world</q>'
        result = html_to_md.html_to_md(html_text)
        expected = u'"Hello world"'
        self.assertEqual(result, expected)
        
    def test_tag_em(self):
        html_text = u'<em>Emphasis</em>'
        result = html_to_md.html_to_md(html_text)
        expected = u'_Emphasis_'
        self.assertEqual(result, expected)

    def test_tag_br(self):
        html_text = u'Hello<br />Bye'
        result = html_to_md.html_to_md(html_text)
        expected = u'''Hello  
Bye'''
        self.assertEqual(result, expected)

    def test_tag_blockquote(self):
        html_text = \
            u'''text1 <blockquote>text2</blockquote> author'''
        result = html_to_md.html_to_md(html_text)
        expected = \
            u'''text1 

> text2

 author'''
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
