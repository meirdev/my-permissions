import os
import stat

__version__ = "0.1.0"


READ = "r"
WRITE = "w"
EXECUTE = "x"
NONE = "-"


PERMISSIONS = {
    stat.S_IRUSR: READ,
    stat.S_IWUSR: WRITE,
    stat.S_IXUSR: EXECUTE,
    stat.S_IRGRP: READ,
    stat.S_IWGRP: WRITE,
    stat.S_IXGRP: EXECUTE,
    stat.S_IROTH: READ,
    stat.S_IWOTH: WRITE,
    stat.S_IXOTH: EXECUTE,
}


class MyPermissions:
    def __init__(self, path: str) -> None:
        self._path = path

    def can_read(self) -> bool:
        return os.access(self._path, os.R_OK)

    def can_write(self) -> bool:
        return os.access(self._path, os.W_OK)

    def can_execute(self) -> bool:
        return os.access(self._path, os.X_OK)


class FullPermissions:
    def __init__(self, path: str) -> None:
        self._path = path

    def __str__(self) -> str:
        permissions = os.stat(self._path).st_mode & 0o777

        result = ""
        for key, value in PERMISSIONS.items():
            result += value if permissions & key else NONE
        return result
