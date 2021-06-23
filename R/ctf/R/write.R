#' Write Data Frame To CTF
#' 
#' Save a data frame using Column Text Format
#' 
#' @param x data frame to write
#' @param location to write CTF data
#' @param ... further arguments to \code{\link[base]{cat}}
#' @return \code{NULL}, used for its side effect
#' @seealso \code{\link{read.ctf}} to read CTF, \code{\link[base]{cat}} for the underlying functionality, and \code{\link[base]{save}} for writing any R objects.
#' @export
#' @examples
#' d <- file.path(tempdir, "iris_ctf_data")
#' write.ctf(iris, d)
#' 
#' # Same object as iris, but carries around some extra metadata
#' iris2 <- read.ctf("iris_ctf_data")
write.ctf = function(x, location, ...)
    NULL
