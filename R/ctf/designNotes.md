## Design Notes

It's not sufficient to return a data frame from `read.ctf`, because that will ignore all the description metadata that existed in the JSON file, for example, the description of the columns.
We need a way to preserve and represent this metadata in R.

Here's a couple options for what `read.ctf` could return:

1. list with the data frame and the metadata objects
2. data frame with metadata as an attribute
3. data frame with metadata in a comment- seems like a bad idea to put metadata back into a string.

Ideally, we could pick the functionality of describing data up from an existing package.
Based on a few Google searchs like this [StackOverflow post](https://stackoverflow.com/questions/11348320/is-there-a-standard-way-to-document-data-frames?noredirect=1&lq=1) it looks like the "Hmisc" package may have this functionality.
The [labelVector package](https://cran.r-project.org/package=labelVector) also seems like the right idea.
Unfortunately, the `get`, `set` methods aren't idiomatic R, and the package isn't on Github.

Short term, storing the metadata in an attribute seems like the best design.
It's a data frame, so it won't break code if we switch from a list to a data frame in the future.
Long term, it makes more sense to create and depend on a more focused package for labeled data that's tied to CSVW.
This is close to the original xarray approach of creating a Python object in memory that mirrors the netCDF object on disk.

---

It's simpler not to append `.txt` to the end of the column names, because a column name might end with `.txt`, and that would be confusing.
