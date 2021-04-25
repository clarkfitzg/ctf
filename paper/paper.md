goal for Spring 2021: 3-5 page paper suitable for conference.
Can expand it later.

## Abstract


## What's the problem?
The increased usage of technology has produced a greater amount of data that can be used to extract valuable information. An issue with this approach is that storing large amounts of data and then processing it is not a straightforward task. 

For instance, a researcher may have a large data set like the GDELT (will need to specify which one) which is data on news media from around the world and is stored as a CSV file that has 61 columns and approximately 61 million rows. If they are interested in performing an operation on the data to do something like count how many of the 61 million observations were from Sacramento, CA they would have to look at the column referring to the location of each observation and then count how many rows correspond to Sacramento. Since there are 61 million observations it would be very costly to traverse the entire CSV file. 

Thus, one approach would be to isolate the specified column using a unix pipeline command like `Cut -d, 37 GDELT.csv | Grep sacramento | wc`. However, this is not optimal since the delimiter, and the column index 37, are arbitrary. Furthermore, if the researcher were performing similar tasks repeatedly then it would also be costly to keep cutting the needed column. 

If the data were not stored in a CSV file and instead stored in a binary format, a similar approach could be taken using a command like `Dump GDELT.fancy.binary.format -c geo_location_column | Grep sacramento | wc`. The downside to this approach is that the binary has to be converted which results in a cost but possibly not that great of one. Moreover, binary formats are complicated to work with and not as accessible as text based formats.

Therefore, there is still the need to address this problem with a column based format that would provide speed advantages of working only with the desired columns and be very accessible to users with varying levels of technical ability.

## How `ctf` addresses this problem
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


In one of the JSS articles I [read](https://www.jstatsoft.org/article/view/v097i01) they included a series of examples using the Boston housing data set. This may be obvious but we should also include a series of examples as well as nice graphs that correspond to them. 

## Limitations
While `ctf` is a simple, hackable, and efficient solution to many data storage tasks, it is not perfect and its limitations need to be addressed. 

First, the columnFiles are not joined together so some applications that need to access many columnFiles corresponding to a row are not as efficient as in CSV. For example, if a user wanted to not only count how many observations were from Sacramento but also take the average of all those observations’ Goldstein Score, which quantifies how an event will impact the stability of a country and is stored in its own column, the Unix pipeline would be more difficult to create for the `ctf` case than the CSV case. 

Second, if a user wishes to access nearly all of the columns of data stored in a matrix structure then there wouldn’t be as much, or any, speed advantage over the CSV format. Some testing has been conducted that compares the performance of `ctf` vs CSV depending on how many columns need to be accessed and the results are below. (put the results) 

Third, `ctf` is a new format and has not had the rigorous testing that the alternatives have had. Thus, the infrastructure will be in an inferior state until it is more widely adopted and then improved upon based on real world usage. 

Fourth, if a user is storing an excessively large amount of columnFiles, like several thousand, then `ctf` may not be able to support their needs as the amount of files that can be opened bounds the number of columnFiles in a `ctf` directory. 


### Design goals
For the CTF python package we wanted to mirror the current [CSV package](https://docs.python.org/3/library/csv.html) as closely as possible since that is the storage technology that it seeks to *?extend?*. 


The main objective of `ctf` is to be simple to use and thus the design goals will correspond to this. Since other file storage formats have already established a set of standards for working with said formats, the aim of `ctf` will be to maintain as much of those standards as possible. 

The most notable example is that `ctf` will mirror the API of the [CSV package](https://docs.python.org/3/library/csv.html) closely and only deviate from the API when the structural differences force `ctf` to do so. Thus, users who have experience working with CSV will find it intuitive to make the transition over to `ctf` to help them solve their data science needs. 

It is also important to recognize that cloud computing is an increasingly significant tool for many data science applications thus compatibility with the major cloud environment is a must for `ctf`. Amazon’s AWS is currently the leading provider of such services, hence integrating `ctf` with AWS will be prioritized. Users should be able to easily store their data in the `ctf` format as objects inside of AWS buckets and then be able to easily access their data either through an ec2 instance or a traditional Unix terminal. 

`ctf` users will likely be employing other data storage formats like CSV or binary, therefore, it is paramount to facilitate the smooth conversion to and from `ctf`. These conversions should be able to be performed in the case that the file is downloaded (need to reword this but idk what fits the best so I should ask) or in the case that the file is large and the user wants to stream it during the conversation. Thus, both functionalities will be available with `ctf`. 

Since one of the unique features of `ctf` is that it contains a metadata file it is important to establish how that metadata file will be organized. In a similar approach to how `ctf`’s API will mirror CSV, `ctf`’s metadata will mirror the [W3 metadata standards](https://www.w3.org/TR/tabular-data-primer/). While much can be extended, there are some key structural components that are different. For instance, `ctf` does not have columns like CSV files and instead data are stored in .txt files called columnFiles. Thus, this would be different from the W3 metadata standard. Another major difference is that `ctf` is a directory and not simply one file. QUESTION: how much should I do? Should I include all the stuff like here https://github.com/julianofhernandez/ctf/blob/main/examples_of_ctf_vs_csv/divergenceFromW3.md? It is pretty difficult to explain this in only words alone and having an example would help make what I have written concrete but if I did that then it would be much longer than usual. I know that this paper isn’t supposed to be the documentation so I’m wondering how much I should write.


## Other solutions to this problem


## Conclusions, Future work
