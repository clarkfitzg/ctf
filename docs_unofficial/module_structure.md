## Intro to importing
Import the ctf package, which runs /ctf/__init__.py.
```python
import ctf
```

Import the column module in the ctf package, which runs /ctf/__init__.py as well as ctf/column.py
```python
import ctf.column
```

Use the Column class within the ctf/column.py.
```python
import ctf.column
x = ctf.column.Column
```

If we have a directory structure like this:
```
column_text_format/
    __init__.py
    column.py
    reader.py
```
We can use imports to have reader.py use a class from column.py called Column. Within column_text_format/reader.py import using relative import using:
```python
from .column import Column
```
or by absolute import by using:
```python
from column_text_format.column import Column
```

## Compared to CSV
Because csv is imported as a module our import will be a little more completed.
Rathan than:
```python
import csv
```
We will need:
```python
from column_text_format import ctf
```

From here the following code should be interchangable between ctf and csv.
```python
rows = csv.reader(file_name)
for row in rows:
    print(row)
```

## CTF directory structure
To mimick how csv imports work with its reader() and writer() functions while still maintaining seperate files for classes we will need to use the structure below.
```
column_text_format/
    __init__.py
    ctf.py
    writer.py
    reader.py
```
Within ctf.py we can write functions like reader() and writer() that will return objects from reader.py and writer.py respectively. 
