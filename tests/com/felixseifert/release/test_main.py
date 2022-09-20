import sys
from argparse import Namespace

from src.com.felixseifert.release.__main__ import say_hello, get_name, \
    parse_command_line, main


def test_main(monkeypatch, capsys):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['__main__'])
        main()
        captured_actual = capsys.readouterr().out
        captured_expected = 'Hello, World!\n'
        assert captured_actual == captured_expected


def test_parse_command_line(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['__main__', 'Karl'])
        namespace_actual: Namespace = parse_command_line()
        namespace_expected: Namespace = Namespace(name='Karl')

        assert namespace_actual == namespace_expected


def test_get_name_no_arg():
    args: Namespace = Namespace(name=None)
    name_actual = get_name(args)
    name_expected = 'World'

    assert name_actual == name_expected


def test_get_name_name():
    args: Namespace = Namespace(name='Carla')
    name_actual = get_name(args)
    name_expected = 'Carla'

    assert name_actual == name_expected


def test_say_hello():
    greeting_actual = say_hello('Karl')
    greeting_expected = 'Hello, Karl!'

    assert greeting_actual == greeting_expected
