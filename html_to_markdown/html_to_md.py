# -*- coding: utf-8 -*-
"""
Module for converting HTML to Markdown
"""

import glob
import os
import importlib
import HTMLParser
import argparse


class HtmlToMarkdownParser(HTMLParser.HTMLParser):
    """
    The class to parse HTML and convert it to Markdown
    """

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.result = []

        self.tag_handlers = {}
        script_dir = os.path.dirname(__file__)
        handlers_dir_name = "handlers"
        handlers_dir = os.path.join(script_dir, handlers_dir_name)
        for tag_handler in glob.glob(handlers_dir + "/tag*.py"):
            handler_module_name = os.path.splitext(os.path.basename(tag_handler))[0]
            handler_module = importlib.import_module("{}.{}".format(handlers_dir_name,
                                                                    handler_module_name),
                                                     handlers_dir_name)
            self.tag_handlers[handler_module.TAG] = handler_module

    def handle_data(self, data):
        self.result.append(data)

    def handle_starttag(self, tag, attrs):
        if tag in self.tag_handlers:
            self.tag_handlers[tag].handle_starttag(self, tag, attrs)

    def handle_endtag(self, tag):
        if tag in self.tag_handlers:
            self.tag_handlers[tag].handle_endtag(self, tag)

    def feed(self, data):
        HTMLParser.HTMLParser.feed(self, data)

    def append_to_result(self, text):
        self.result.append(text)

    def parse(self, data):
        self.feed(data)
        self.close()
        return u''.join(self.result)


def html_to_md(text):
    parser = HtmlToMarkdownParser()
    return parser.parse(text)


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("filename", help="Input HTML file")
    argument_parser.add_argument("-e", "--encoding",
                                 help="Encoding of the input file (default is 'utf-8')",
                                 default="utf-8")
    arguments = argument_parser.parse_args()

    with open(arguments.filename) as input_file:
        input_text = input_file.read().decode(arguments.encoding)
        print html_to_md(input_text)


if __name__ == "__main__":
    main()
