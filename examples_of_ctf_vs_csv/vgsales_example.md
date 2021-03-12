
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

We will now add more columns to represent our entire `vgsales` CSV file and we will also show 
what the first few rows of the `vgsales` CSV file looks like. 

```JSON
{
        "tableSchema": {
                "columns": [{
                        "titles": "Rank",
                        "description": "The rank of different video games based on their global sales.",
                        "datatype": "integer"
                        }, {
			"titles": "Name",
			"description": "The name of the video game."
			}, {
			"titles": "Platform",
			"description": "The type of device or console the came is played on."			
			}]}
}
```
The CTF version of `vgsales`. Also I sort of drifted from your version and made what looks like a mix of 
example 8 and 18 from [w3](https://www.w3.org/TR/tabular-data-primer/) because it seemed like it would fit their standards more.

```JSON
{
  "@context": "http://www.w3.org/ns/csvw",
  "title": "vgsales"
  "description": "Data on the highest selling video games around the world."
  "creator": "Gregory Smith",
  "tables": [{
    "url": "Rank.txt",
    "tableSchema": {
      "columns": [{
      "titles": "Rank",
      "description": "The rank of different video games based on their global sales."
      "datatype": "integer"
      }]
  }
  }, {
    "url": "Name.txt",
    "tableSchema": {
      "columns": [{
      "titles": "Name",
      "description": "The name of the video game."
      }]
  } 
  }, {
    "url": "Platform.txt",
    "tableSchema": {
      "columns": [{
      "titles": "Platform",
      "description": "The type of device or console the game is played on."
      }]
  }
  }]
}



```




```CSV
Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales
1,Wii Sports,Wii,2006,Sports,Nintendo,41.49,29.02,3.77,8.46,82.74
2,Super Mario Bros.,NES,1985,Platform,Nintendo,29.08,3.58,6.81,0.77,40.24
3,Mario Kart Wii,Wii,2008,Racing,Nintendo,15.85,12.88,3.79,3.31,35.82
4,Wii Sports Resort,Wii,2009,Sports,Nintendo,15.75,11.01,3.28,2.96,33
5,Pokemon Red/Pokemon Blue,GB,1996,Role-Playing,Nintendo,11.27,8.89,10.22,1,31.37
```



Add a couple more columns, show the original CSV file and how ctf represents it.
We only need a handful of rows.


## Value constraints

The minimum value is 1 for rank.

