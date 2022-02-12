# my-permissions

Check your permissions to read, write or execute.

## Show what you can do

```bash
my_permissions /path/to/file

You can read.
You can write.
You can execute.
```

## Show what you can't do

```bash
my_permissions /path/to/file -v

You can't write.
```

## Show the full permissions

```bash
my_permissions /path/to/file -S

rwxr-xr-x
```
