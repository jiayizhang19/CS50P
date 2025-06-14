from watch import *


def test_valid():
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"


def test_out_of_iframe():
    assert parse('<src="https://www.youtube.com/embed/xvFZjo5PgG0">') == None


def test_non_src_value():
    assert parse('<iframe title="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == None


def test_non_url():
    assert parse('<iframe src="Youtube"></iframe>') == None


def test_non_valid_url():
    assert parse('<iframe src="htps://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == None
