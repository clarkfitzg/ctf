#' Conversion From CSV To CTF
#' 
#' Direct conversion from CSV file to CTF data.
#'
#' @param csvpath a CSV file or file path
#' @param ... further arguments to \code{\link[ctf]{write.ctf}}
#'
#' @return a CTF directory
#' @export
#'
#' @examples
#' # An example of CSV file included in this package
#' d <- "inst/extdata/vgsales.csv"
#' 
#' # Writes a CTF directory in the working directory
#' to_ctf(d)
#' 
#' # A new directory contains plain text files for each column in vgsales
#' list.files("vgsales")
#' 
#' Clean up
#' unlink("vgsales", recursive = TRUE)
to_ctf = function(csvpath, ...)
{
	  df = read.csv(csvpath)
  directory_name = tools::file_path_sans_ext(basename(csvpath))
    write.ctf(df, directory_name, name = directory_name, ...)
}
