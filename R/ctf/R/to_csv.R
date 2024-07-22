#' Conversion From CTF To  CSV
#' 
#' Direct conversion from CTF data to CSV file.
#'
#' @param ctfpath a directory containing a single CTF metadata JSON file
#' @param columns names or numbers of the columns to read.
#'      If missing, then read in all columns.
#' @param nrows integer, the maximum number of rows to read in.
#'      If missing, then read in all rows.
#' @return a CSV file
#' @export
#'
#' @examples
#' # An example CTF metadata file included in this package
#' d <- "inst/extdata/vgsales"
#' 
#' # Writes a CSV file in the working directory
#' to_csv(d)
#' 
#' # Clean up
#' file.remove("vgsales.csv")
to_csv = function(ctfpath, columns, nrows)
{
	  df = read.ctf(ctfpath, columns, nrows)
  name = basename(ctfpath)
    filename = paste0(name, ".csv")
    write.csv(df, filename, row.names = FALSE)
}
