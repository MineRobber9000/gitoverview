# gitoverview
A Python module for generating commit logs.

Requires [GitPython](https://www.github.com/gitpython-developers/GitPython).

## How to use
```Python
import gitoverview as go;

# generate commit log
go.generate("~minerobber/qdb")

# get a list of commits
go.getLogs("~minerobber/qdb")
```
