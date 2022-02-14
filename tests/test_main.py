import os
import sys
from unittest.mock import patch

import pytest

from my_permissions.__main__ import main


def patch_os_access_side_effect(modes):
    def inner(path, mode):
        return mode in modes

    return patch.object(os, "access", side_effect=inner)


def test_main_path_does_not_exit():
    with patch.object(sys, "argv", ["", "myfile"]):
        with pytest.raises(SystemExit):
            main()


def test_main_regular(capsys):
    with patch.object(sys, "argv", ["", "myfile.txt"]):
        with patch_os_access_side_effect([os.R_OK, os.W_OK]):
            main()

    assert """You can read.\nYou can write.""" == capsys.readouterr().out.strip()


def test_main_invert(capsys):
    with patch.object(sys, "argv", ["", "myfile.txt", "-v"]):
        with patch_os_access_side_effect([os.R_OK, os.W_OK]):
            main()

    assert """You can't execute.""" == capsys.readouterr().out.strip()


def test_main_show(capsys):
    with patch.object(sys, "argv", ["", "myfile.txt", "-S"]):
        with patch.object(os, "stat", return_value=type("", (), {"st_mode": 0o755})):
            main()

    assert "755 = rwxr-xr-x" == capsys.readouterr().out.strip()
