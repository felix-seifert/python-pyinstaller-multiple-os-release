from argparse import Namespace, ArgumentParser


def main() -> None:
    args = parse_command_line()
    name = get_name(args)
    print(say_hello(name))


def parse_command_line() -> Namespace:
    parser = create_parser()
    return parser.parse_args()


def create_parser() -> ArgumentParser:
    app_description = 'Say \'Hello\' to a specific person or to the whole world'
    parser = ArgumentParser(description=app_description)
    parser.add_argument('name', type=str, nargs='?',
                        help='Specify name if you want to greet a specific person')
    return parser


def get_name(args: Namespace) -> str:
    if args.name is None:
        return 'World'
    return args.name


def say_hello(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == '__main__':
    main()
