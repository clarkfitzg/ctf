## Importing
We need to be able to import the package and use all the underlying functions out of the box.
```python
import column_text_format
reader_obj = column_text_format.reader(dir_name)
writer_obj = column_text_format.writer(dir_name)
converter_obj = column_text_format.converter(csv_file_name)
```
We need to be able to import each main function using dot notation from the main package, these need to be functions not modules.
```python
import column_text_format.reader as ctf_reader
```
```python
import column_text_format.writer as writer
```
```python
import column_text_format.converter as converter
```
TODO: Compare contrast to CSV

## Reading
For reading we have three ways to access columns.
1. Accessing all columns by using the whole reader as an iterable.
```python
reader_obj = ctf.reader(dir_name)
for row in reader_obj:
    print(row)
```
2. Access a single column by passing in the key or index.
```python
reader_obj = ctf.reader(dir_name)
for row in reader_obj['Name']:
    print(row)
for row in reader_obj[3]:
    print(row)
```
3. Access multiple columns by passing in a dict of either keys or indexes.
```python
reader_obj = ctf.reader(dir_name)
for row in reader_obj[['Name', 'BirthDate', 'Height']]:
    print(row)
for row in reader_obj[[3,5,7]]:
    print(row)
```


## Writing
For writing we will need a writer object with a write function that will perform data validation. Additionally there needs to be two ways to write to a file, one that used the relative indexes of the passed array, and another where you use a dictionary with keys to specify which file each item must be written to.
```python
writer_obj = ctf.writer(dir_name)
writer_obj.write("Julian", "1/1/1999", 6.0)
```
```python
writer_obj = ctf.writer(dir_name)
writer_obj.write(name="Julian", birthdate="1/1/1999", height=6.0)
# OR
writer_obj.write(name=["Julian", "Bill"], birthdate=["1/1/1999", "2/3/1994"], height=[6.0,5.7])
```
Because CTF will perform  conversion when reading, writing values need to be validated. With ```write()``` an exception will be thrown if the data doesn't conform to the standards set in the metadata. However, a user can also call ```validate(data)``` to get a boolean value of whether this data will write correctly.
```python
writer_obj = ctf.writer(dir_name)
writer_obj.validate("Julian", "1/1/1999", 6.0)
> True
```

## Conversion
For conversion we need two function to convert to and from csv. The naming scheme here is taken from pandas' ```df.to_csv()``` function.
```python
ctf.to_ctf(csv_file_name)
ctf.to_csv(ctf_dir_name)
```

## Row types
We will need a way to determine what types reader will return.
```python
reader_obj = ctf.reader(dir_name)
types = reader_obj.types
> [str, int, str, float, bool]
```
The same will be needed for writing by using.
```python
writer_obj = ctf.writer(dir_name)
types = writer_obj.types
> [str, int, str, float, bool]
```
TODO: Make to_ctf() a function below the main package.