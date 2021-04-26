
## How ctf addresses this problem 

A solution to the aforementioned problem is to create a new type of data storage known as `ctf`. This type of storage is text based and thus maintains many advantages of CSV. The major difference is that`ctf` is column based. The basic structure of `ctf` is not a file but a directory that contains individual text files for each column, called a columnFile, and also a file for the metadata. 

The CSV file, `vgsales.csv`, looks like this:
```CSV
Rank,Name,Platform,Year, Global_Sales
1,Wii Sports,Wii,2006,82.74
2,Super Mario Bros.,NES,1985,40.74
3,Mario Kart Wii,Wii,2008,35.82
4,Wii Sports Resort,Wii,2009,33
5,Pokemon Red/Pokemon Blue,GB,1996,31.37
```
A `ctf` file corresponding to the same data would be a directory named `vgsales` and would contain a metadata file and a columnFile file for each column like this:

`metadata.json` contains all the meta data

`Rank.txt` contains 
```
1
2
3
4
5
```
`Name.txt` contains 
```
Wii Sports
Super Mario Bros.
Mario Kart Wii
Wii Sports Resort
Pokemon Red/Pokemon Blue
```
`Platform.txt` contains
```
Wii
NES
Wii
Wii
GB
```
`Year.txt` contains 
```
2006
1985
2008
2009
1996
```
`Global_Sales.txt` contains
```
82.74
40.24
35.82
33
31.37
```

Thus, if a user wishes to work with only a subset of the columns, which are represented by text files, they can easily select only those that they want to work with. In the previous example of counting how many observations in the GDELT file are from Sacramento, we would easily be able to run a command like `cat Actor1Geo_Fullname.txt | Grep sacramento | wc` which would be more efficient than either of the previously mentioned solutions. Another key advantage is that since the metadata file is stored inside the `ctf` directory we can easily determine which column we need. The other formats would be more tedious since it isn’t obvious which column needs to be selected to search for Sacramento without the metadata file. The performance advantages are below. 

Plot the graphs and stuff comparing ctf vs csv...maybe binary

