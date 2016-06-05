Error-Correcting/Detecting Codes
=======================

`errcode` is a package for error-correcting codes and error-detecting codes.

### Install

```
pip install --upgrade errcode
```

### API

```python
max_size(arity:int|list[int]=2, repeat:int=1, direction:int|list[int]=1, correct:int=0, detect:Optional[int]=None) -> int|range
```

### Usage Examples

```python
from errcode import max_size
print(max_size(arity=2, repeat=6, correct=4))
print(max_size(arity=[5, -3, 4], detect=1))
```

### GitHub

```
https://github.com/zhiqingxiao/errcode
```
