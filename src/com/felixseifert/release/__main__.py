import argparse


def main() -> None:
    args = parse_command_line()
    name = get_name(args)
    print("Hello, {name}!".format(name=name))


def parse_command_line():
    app_description = 'Say \'Hello\' to a specific person or to the whole world'
    parser = argparse.ArgumentParser(description=app_description)
    parser.add_argument('name', type=str, nargs='?',
                        help='Specify name if you want to greet a specific person')
    return parser.parse_args()


def get_name(args):
    if args.name is None:
        return 'World'
    return args.name


if __name__ == '__main__':
    main()
