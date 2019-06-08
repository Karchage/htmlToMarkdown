TAG = "br"


def handle_starttag(parser, tag, attrs):
    parser.append_to_result(u"  \n")


def handle_endtag(parser, tag):
    pass
