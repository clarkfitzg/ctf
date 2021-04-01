## Goal
This test should be able to compare the average speed of CTF read vs CSV read based on how many columns are being accessed. It should run n times, n being the total number of columns in the file. It should start with checking the time to access a single column, then the next run should check two column, increasing until the last run checks all columns. It should have a configurable function that can be passed in that will be used on the data, this needs to be very similar but not the same for CTF and CSV. This can help normalize the extra time used to convert data types in CTF that isn't used in CSV.

## Results
For the following run I used 30 attempts, then found the mean for each column for plotting a single line. For CTF the function applied is simply a passthrough, however for CSV we are using a conversion statement that will convert the first column to an int. This should balance out the extra work being done in CTF to make conversions based on the metadata.
![CSV vs CTF image](../examples_of_ctf_vs_csv\example_speed_increase\csv_ctf_access_times.png)

The y axis is the time to access the columns in seconds.

The x axis is the total number of columns that were accessed during that run. This starts with one column being accessed and ends with all columns being accessed.

We can see that with one columns being accessed CTF brings a speed increase of whole magnitude of order. However, as we increase the amount of columns being accessed, the time for CTF increases at a linear rate higher than that of CSV. The break even point is roughly at x=6, a current hypothesis is that this might follow that half of the data is the breakeven point. More data will need to be collected to find out how to predict where CTF becomes slower than CSV.

## Next Steps
Going forward to better determine when CTF is faster than CSV this test will have to be expanded out to multiple files. The blocker for this is that CSV to CTF conversion with metadata has to be done manually, once we can automate metadata conversion then we can create many files to run this on. 