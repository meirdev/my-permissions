from my_permissions import mode_to_string, __version__


def test_version():
    assert __version__ == "0.2.0"


def test_mode_to_string():
    assert mode_to_string(0o777) == "rwxrwxrwx"
    assert mode_to_string(0o555) == "r-xr-xr-x"
    assert mode_to_string(0o000) == "---------"
