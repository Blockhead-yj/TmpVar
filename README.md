# TmpVar

TmpVar is used to change the variables environement temprorarily to run some codes and restore the previous environment.

## Example

```python
    import TmpVar
    
    a = 3
    b = 6
    c = 9
    class TestClass:
        def __init__(self, a, b, c) -> None:
            self.a = a
            self.b = b
            self.c = c
    d = TestClass(a, b ,c)
    print(a, b, c, 
          d.a, d.b, d.c)
    with TmpVar({'d.a':3354}, a=453):
        print('—————— temporal environment：——————')
        print(a, b, c, 
            d.a, d.b, d.c)
    print('—————— raw environment：——————')
    print(a, b, c, 
          d.a, d.b, d.c)

    # 3 6 9 3 6 9
    # —————— temporal environment：——————
    # 453 6 9 3354 6 9
    # —————— raw environment：——————
    # 3 6 9 3 6 9
```

## Usage

For single variable, you can simpily run it with:

``` python
with TempEnv(varname1=value1, varname2=value2,...):
    run some code
    ...
```
For attribute of variables, you can use:

``` python
with TempEnv('varname1.attribute1=value1', 'varname2.attribute2=value2',...):
    run some code
    ...
```

For some items in list or dict, I didn't figure out how to access them in proper way.
