TAG = "h3"


def handle_starttag(parser, tag, attrs):
    parser.append_to_result(u"### ")


def handle_endtag(parser, tag):
    pass
