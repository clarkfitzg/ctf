#' Read CTF data
#' 
#' Read external CTF data into the corresponding R object
#' 
#' @param location location of the CTF data.
#'      Typically this is the file path to a local directory.
#' @param columns names of the columns to read.
#'      If \code{columns=NULL}, the default, then read in all columns.
#' @param ... further arguments to \code{\link[base]{scan}}
#' @return data frame of loaded data
#' @seealso \code{\link{write.ctf}} to write CTF, and \code{\link[base]{scan}} for the underlying functionality
#' @export
#' @examples
#' d <- system.file("inst", "extdata", "vgsales", "vgsales-metadata.json")
#'
#' # Read all the columns
#' vgsales <- read.ctf(d)
#'
#' # Read two columns, Name and Rank
#' vgsales2 <- read.ctf(d, columns = c("Name", "Rank"))
read.ctf = function(location, columns = NULL, ...) 
    NULL
