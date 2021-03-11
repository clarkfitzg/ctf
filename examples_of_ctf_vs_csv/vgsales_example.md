
In this narrative we describe how to represent `vgsales`, a CSV file containing video game sales.

TODO: explain `vgsales`.


## Basics

The simplest possible CTF file has just one column.

The files in our directory `vgsales` include:

- `metadata.json`
- `Rank.txt`

The contents of `Rank.txt` are:

```
10
1
5
20
...
```

The contents of `metadata.json` are:

```JSON
{
	"tableSchema": {
		"columns": [{
			"titles": "Rank",
			"url": "Rank.txt",
			}]}
}
```

This means that the table `vgsales` has one column called `Rank` saved in the file `Rank.txt`.

In CSVW, `url` refers to the location of the CSV file.
In CTF, each column has a URL for a local file, because the columns are stored separately.


## Metadata

The `Rank` column has integer values.
We need to represent that in the metadata, or ctf will assume that they are strings.
While we're add it, let's add a `description` for the semantic meaning of the column.
We represent that in `metadata.json` as follows:

```JSON
{
	"tableSchema": {
		"columns": [{
			"titles": "Rank",
			"description": "The rank of different video games based on their global sales.", 
			"datatype": "integer"
			}]}
}
```


## Multiple columns

Add a couple more columns, show the original CSV file and how ctf represents it.
We only need a handful of rows.


## Value constraints

The minimum value is 1 for rank.

