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
#' iris2 <- read.ctf(d)
write.ctf = function(x, datadir = name, name = deparse(substitute(x)), ...)
{
    # This first implementation assumes metadata and data are in the same directory.
    # This assumption seems like a reasonable best practice for local files, but we'll want to generalize it for objects in cloud storage.

    meta = list(`@context` = "http://www.w3.org/ns/csvw"
                , url = "."
                , rowCount = nrow(x)
                , name = name
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

    metafile_path = file.path(datadir, paste0(name, "-metadata.json"))

    # Begin saving
    # TODO: TDD if(dir.exists(datadir) && (notempty)) stop("best practice is to write data in an empty directory. The directory ... contains the files ... Move these files or use a different datadir")
    dir.create(datadir)
    jsonlite::write_json(meta, metafile_path)
    # TODO: Check if cat() or writeLines() is faster.
    Map(cat, x, file = file.path(datadir, col_file_names), sep = "\n", MoreArgs = list(...))

    invisible(NULL)
}
