### Challenges
1. Convention.
In the csv package in python they use functions like writeheader() should we keep this same convention or follow the larger python convention of seperating function words with a underscore. Should it be writeheader() or write_header()?

### Writer object setup
```python
import column_text_format
writer = column_text_format.writer

writer.writerow()
```

### Add a new row
```python
writer.writerow({'column_name_one': 'Some string value', 'taxable': 123.4})
```

### Add multiple rows
```python
writer.writerow([
    {'column_name_one': 'Some string value', 'taxable': 123.4},
    {'column_name_two': 'Some other value', 'A bool value': True}
])
```
### Add a new column
For setting up a new document it may be needed to pull together columns from seperate files. Having writecolumn would allow you to add a new column to the CTF file, as long as it has enough values to fill the spaces according to the other columns. if there are no rows yet then simply passing a string will work.
Column with rows:
```python
writer.writecolumn({'new_column_name': ['a', 'list', 'of', 'values', 'to', 'add'])
```
Column with no rows:
```python
writer.writecolumn('new_column_name')
```
Column with no rows, that has a specified type:
```python
writer.writecolumn('new_column_name', 'string')
```

### Delete column
```python
writer.removecolumn('new_column_name')
```

### Change column names
```python
writer.renamecolumn('old_column_name', 'new_column_name')
```