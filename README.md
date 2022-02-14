# my-permissions

Check your permissions to read, write or execute.

## Show what you can do

```bash
mypermissions /path/to/file

You can read.
You can write.
You can execute.
```

## Show what you can't do

```bash
mypermissions /path/to/file -v

You can't write.
```

## Show the permissions

```bash
mypermissions /path/to/file -S

rwxr-xr-x
```
