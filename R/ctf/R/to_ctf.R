#' Conversion From CSV To CTF
#' 
#' Direct conversion from CSV file to CTF data.
#'
#' @param csvpath a CSV file or file path
#' @param datadir 
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
#' to_ctf(d, "vgsales")
#' 
#' # A new directory contains plain text files for each column in vgsales
#' list.files("vgsales")
#' 
#' Clean up
#' unlink("vgsales", recursive = TRUE)
to_ctf = function(csvpath, datadir, ...)
{
	name = basename(datadir)
	cutdf = iotools::read.csv.raw(csvpath, header = FALSE, nrows = 1)
	col_names = unlist(split(cutdf, seq(nrow(cutdf))))
	iotools::chunk.apply(csvpath, 
			     function(x){
				df = iotools::read.csv.raw(x)
				colnames(df) = col_names
				write.ctf(df, datadir, name = name, appendRows = TRUE, ...)
				}, 
				CH.MAX.SIZE = 2e5)
      	invisible(NULL)
}
