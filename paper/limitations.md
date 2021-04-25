## Limitations
While `ctf` is a simple, hackable, and efficient solution to many data storage tasks, it is not perfect and its limitations need to be addressed. 

First, the columnFiles are not joined together so some applications that need to access many columnFiles corresponding to a row are not as efficient as in CSV. For example, if a user wanted to not only count how many observations were from Sacramento but also take the average of all those observations’ Goldstein Score, which quantifies how an event will impact the stability of a country and is stored in its own column, the Unix pipeline would be more difficult to create for the `ctf` case than the CSV case. 

Second, if a user wishes to access nearly all of the columns of data stored in a matrix structure then there wouldn’t be as much, or any, speed advantage over the CSV format. Some testing has been conducted that compares the performance of `ctf` vs CSV depending on how many columns need to be accessed and the results are below. (put the results) 

Third, `ctf` is a new format and has not had the rigorous testing that the alternatives have had. Thus, the infrastructure will be in an inferior state until it is more widely adopted and then improved upon based on real world usage. 

Fourth, if a user is storing an excessively large amount of columnFiles, like several thousand, then `ctf` may not be able to support their needs as the amount of files that can be opened bounds the number of columnFiles in a `ctf` directory. 

