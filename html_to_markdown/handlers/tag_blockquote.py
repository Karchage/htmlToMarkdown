TAG = "blockquote"


def handle_starttag(parser, tag, attrs):
    parser.append_to_result(u"\n\n> ")


def handle_endtag(parser, tag):
    parser.append_to_result(u"\n\n")
