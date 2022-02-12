import argparse
import operator

from rich import print

from . import MyPermissions, FullPermissions


def main() -> None:
    arg_parser = argparse.ArgumentParser("Check your permissions")
    arg_parser.add_argument("path", help="Path to check")
    arg_parser.add_argument(
        "-v",
        "--invert",
        action="store_true",
        help="Show what you can't do",
    )
    arg_parser.add_argument(
        "-S",
        "--show",
        action="store_true",
        help="Show the full permission of the file and exit",
    )

    args = arg_parser.parse_args()

    if args.show:
        print(FullPermissions(args.path))
        return

    if args.invert:
        start_text = "[red]You can't"
        check = operator.not_
    else:
        start_text = "[green]You can"
        check = operator.truth

    my_permissions = MyPermissions(args.path)

    permissions = {
        "read": my_permissions.can_read(),
        "write": my_permissions.can_write(),
        "execute": my_permissions.can_execute(),
    }

    for key, value in permissions.items():
        if check(value):
            print(f"{start_text} [b]{key}[/b].")


if __name__ == "__main__":
    main()
