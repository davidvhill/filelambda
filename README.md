# filelambda &#955;
An obviously impure functional file library for Python.

## Install
```
pip install filelambda
```

## Usage

```python
from filelambda import files as f

filename = '/tmp/example.txt'
text     = 'Functions are good'

w = f.write(filename, text)
r = f.read(filename)
d = f.delete(filename)

assert w == 18
assert r == text
assert d == True
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


