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
{

    meta = list(`@context` = "http://www.w3.org/ns/csvw"
                , url = "."  # TODO: generalize- "." assumes column files are in the same directory.
                , rowCount = nrow(x)
    )
    # TODO: Allow users to add their own metadata

    col_names = colnames(x)
    col_file_names = paste0(col_names, ".txt")
    R_types = sapply(x, typeof)

    meta[["tableSchema"]] = list(columns = Map(list
        , url = col_file_names
        , titles = col_names
        , datatype = map_types(R_types, to = "meta")
    ))

    jsonlite::write_json(meta, meta_path)
    Map(cat, x, file = col_file_names, MoreArgs = list(...))
}
