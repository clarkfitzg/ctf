#' Write Data Frame To CTF
#' 
#' Save a data frame using Column Text Format
#' 
#' @param x data frame to write
#' @param datadir directory to write the metadata and CTF columns
#' @param name table name
#' @param ... further arguments to \code{\link[base]{cat}}
#' @return \code{NULL}, used for its side effect
#' @seealso \code{\link{read.ctf}} to read CTF, \code{\link[base]{cat}} for the underlying functionality, and \code{\link[base]{save}} for writing any R objects.
#' @export
#' @examples
#' d <- file.path(tempdir(), "iris_ctf_data")
#' write.ctf(iris, d)
#' 
#' # Same object as iris, but carries around some extra metadata
#' iris2 <- read.ctf("iris_ctf_data")
write.ctf = function(x, datadir = name, name = deparse(substitute(x)), ...)
{

    meta = list(`@context` = "http://www.w3.org/ns/csvw"
                , url = "."  # "." assumes metadata and data are in the same directory, which is reasonable for a first implementation.
                , rowCount = nrow(x)
                , name = name
    )
    # TODO: Allow users to add their own metadata

    col_names = colnames(x)
    col_file_names = paste0(col_names, ".txt")
    col_file_names = file.path(datadir, col_file_names)
    R_types = sapply(x, typeof)

    meta[["tableSchema"]] = list(columns = Map(list
        , url = col_file_names
        , titles = col_names
        , datatype = map_types(R_types, to = "meta")
    ))

    metafile_path = file.path(datadir, paste0(name, ".json"))

    # Begin saving
    # TODO: TDD if(dir.exists(datadir) && (notempty)) stop("best practice is to write data in an empty directory. The directory ... contains the files ... Move these files or use a different datadir")
    dir.create(datadir)
    jsonlite::write_json(meta, metafile_path)
    Map(cat, x, file = col_file_names, MoreArgs = list(...))
}
