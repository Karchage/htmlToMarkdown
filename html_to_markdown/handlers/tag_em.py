TAG = "em"


def handle_starttag(parser, tag, attrs):
    parser.append_to_result(u"_")


def handle_endtag(parser, tag):
    parser.append_to_result(u"_")