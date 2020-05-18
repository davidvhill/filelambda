# filelambda
An (impure) functional Python file library.

## Install
```
pip install filelambda
```

## Examples

```python
>>> from filelambda import files as f
>>> f.write('/tmp/example.txt', 'Functions are good')
18
>>> f.read('/tmp/example.txt')
'Functions are good'
>>> f.delete('/tmp/example.txt')
True
```

## Reference

| Function         | Description                          |
| ---------------- | ------------------------------------ |
| files.read       | read a text file                     |
| files.readb      | read a binary file                   |
| files.readlines  | read lines of a text file            |
| files.readlinesb | read lines of a binary file          |
| files.write      | write a text file                    |
| files.writeb     | write a binary file                  |
| files.append     | append to a text file                |
| files.appendb    | append to a binary file              |
| files.delete     | delete a file                        |
| files.exists     | check if a file exists               |
| files.mkdirs     | create parent directories for a file |

## Contributing
Rebase off latest master, send a pull request.


