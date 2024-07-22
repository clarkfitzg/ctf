#' Conversion From CSV To CTF
#' 
#' Direct conversion from CSV file to CTF data.
#'
#' @param csvpath a CSV file or file path
#' @param datadir directory used to write CTF files in
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
to_ctf = function(csvpath, datadir = tools::file_path_sans_ext(csvpath), ...)
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
      	metafile_path = file.path(datadir, paste0(name, "-metadata.json"))
	meta = jsonlite::read_json(metafile_path)
	meta[["tables"]][[1]][["rowCount"]] = nrow(read_one_col(file.path(datadir, col_names[1])))
	jsonlite::write_json(meta, metafile_path)
	invisible(NULL)
}
