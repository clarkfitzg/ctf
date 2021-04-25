## What’s the problem?
The increased usage of technology has produced a greater amount of data that can be used to extract valuable information. An issue with this approach is that storing large amounts of data and then processing it is not a straightforward task. 

For instance, a researcher may have a large data set like the GDELT (will need to specify which one) which is data on news media from around the world and is stored as a CSV file that has 61 columns and approximately 61 million rows. If they are interested in performing an operation on the data to do something like counting how many of the 61 million observations were from Sacramento, CA they would have to look at the column referring to the location of each observation and then count how many rows correspond to Sacramento. Since there are 61 million observations it would be very costly to traverse the entire CSV file. 

Thus, one approach would be to isolate the specified column using a unix pipeline command like `Cut -d, 37 GDELT.csv | Grep sacramento | wc`. However, this is not optimal since the delimiter, and the column index 37, are simply arbitrary. Furthermore, if the researcher were performing similar tasks repeatedly then it would also be costly to keep cutting an arbitrary column. 

If the data were not stored in a CSV file and instead stored in a binary format, a similar approach could be taken using a command like `Dump GDELT.fancy.binary.format -c geo_location_column | Grep sacramento | wc`. The downside to this approach is that the binary has to be converted which results in a cost but possibly not that great of one. Moreover, binary formats are complicated to work with and not as accessible as text based formats.

Therefore, there is still the need to address this problem with a column based format that would provide speed advantages of working only with the desired columns and be very accessible to users with varying levels of technical ability. 
