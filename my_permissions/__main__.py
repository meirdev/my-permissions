import argparse
import operator
import os
import sys

from rich import print

from . import MyPermissions, mode_to_string, mode


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
        help="Show the permission and exit",
    )

    args = arg_parser.parse_args()

    if not os.path.exists(args.path):
        print(f"[red]Path does not exist", file=sys.stderr)
        sys.exit(1)

    if args.show:
        path_mode = mode(args.path)
        print(f"{path_mode:o} = {mode_to_string(path_mode)}")
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


if __name__ == "__main__":  # pragma: no cover
    main()
