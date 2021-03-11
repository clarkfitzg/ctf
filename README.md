# CTF - column text format

CTF stores the columns of tabular data in plain text, combining the simplicity of text with the performance of a column store.

## Simple Example

Suppose you want to compute the maximum value in one column of a table with 10 columns.
CTF only reads in this column, so it's around 10 times faster than CSV, which must read in the entire data set.

TODO: show code, make sure it's 10 times faster. 😁




# Search times

- Searched 1 columns with 431644 rows in 0.26 seconds
- Searched 2 columns with 431644 rows in 0.39 seconds
- Searched 3 columns with 431644 rows in 0.51 seconds
- Searched 4 columns with 431644 rows in 0.61 seconds
- Searched 5 columns with 431644 rows in 0.69 seconds
- Searched 6 columns with 431644 rows in 0.92 seconds
- Searched 7 columns with 431644 rows in 1.04 seconds
- Searched 8 columns with 431644 rows in 1.34 seconds
- Searched 9 columns with 431644 rows in 1.66 seconds
- Searched 10 columns with 431644 rows in 1.83 seconds
- Searched 11 columns with 431644 rows in 1.96 seconds
- Searched 12 columns with 431644 rows in 2.11 seconds
- Searched 13 columns with 431644 rows in 2.29 seconds
- Searched 14 columns with 431644 rows in 2.39 seconds
- Searched 15 columns with 431644 rows in 2.47 seconds
 
# Conversion times
- name								start size	time
- ignore_country_classification.csv	4257    	0.02
- ignore_goods_classification.csv 	239619  	0.07
- ignore_gsquarterlySeptember20.csv	73824486	20.65
- ignore_services_classification.csv	2828		0.02
- ignore_test.csv						82533516	47.74

# End User Manual

How would I like use this code?

Suppose I have a table called `people` stored in CTF.

TODO: Define and describe `people` table.

```bash
$ cat people.csv
names       age
Shawheen    21
Julian      20
Clark       34
```

I want to access a column called `names` from this table.

```SQL
SELECT names FROM people
```

Assume that `people` is a directory containing the CTF data.

```python
import CTF

names = CTF.load_column("people", "names")
```

TODO: look at `load_column`, see what the most common name is for reading / loading data.
How closely can we copy `csv` from the standard library?

Use case: it would be great if we could access the data as a stream, without necessarily loading everything in memory.
We can get this feature by having `names` be an iterator or generator over the column values.
 
Example processing names:

```
from Collections import Counter

counts = Counter(names)
```

## Use case 2 - column types

```
age = CTF.load_column("people", "age")
```

`age` should generate integer values corresponding to each entry of the `age` column.
CTF knows that the `age` column means integer because of the metadata file in the `people` directory.
TODO: link to W3 standard.

```
# User should not write this- it's just the idea we want
def create_age():
    for x in [21, 20, 34]:
        yield x

age = create_age()

# User can do something like this:
>>> list(age)
[21, 20, 34]
```


## Use case 3 - compatibility with `csv`

```
import csv

# Referring to file `people.csv` in CSV format
r = csv.reader("people.csv")

# Referring to directory `people` in CTF format
r2 = CTF.reader("people")
```

`r2` should essentially be a drop in replacement for `r`.

```
for row in r:
    process(row)
```

TODO: Process a csv file using Python's `csv` package- any kind of data analysis is fine.
For example, find the set of all values in one column.

# Python notes
I used this link for helping me construct the iterable.
[Python special methods](https://levelup.gitconnected.com/python-dunder-methods-ea98ceabad15)
[W3C metadata](https://www.w3.org/TR/tabular-metadata/)

# Outline
- Ctf modeled after csv and/or dictionary
    - [ ] Should Ctf be accessed with a reader like csv or through itself like a dictionary
    - [x] Column accessed with ["column_name"]
    - [ ] Can convert a csv file to ctf
    - [ ] Reader runs like csv reader returning iterable rows
    - [ ] class Row to give a guide for adding new columns using values from metadata.json
    - [ ] Use custom exceptions
    - [ ] Get type from metadata.json or autodetect

```python
with Ctf.open() as ctf_file:
    ctf_file["column"]
    for row in ctf_file:
        print(row)
```

```python
Ctf.open()
Ctf.close()
```
