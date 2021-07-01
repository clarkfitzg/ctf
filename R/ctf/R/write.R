#' Write Data Frame To CTF
#' 
#' Save a data frame using Column Text Format
#' 
#' @param x data frame to write
#' @param datadir directory to write the metadata and CTF columns
#' @param name table name
#' @param ... further arguments to \code{\link[iotools]{write.table.raw}}
#' @return \code{NULL}, used for its side effect
#' @seealso \code{\link{read.ctf}} to read CTF, \code{\link[iotools]{write.table.raw}} for the underlying functionality, and \code{\link[base]{save}} for writing any R objects.
#' @export
#' @examples
#' d <- file.path(tempdir(), "iris_ctf_data")
#' write.ctf(iris, d)
#' 
#' # Same object as iris, but carries around some extra metadata
#' iris2 <- read.ctf(d)
#' 
#' # This directory contains plain text files for each column in iris
#' list.files(d)
#' 
#' # Clean up
#' unlink(d, recursive = TRUE)
write.ctf = function(x, datadir = name, name = deparse(substitute(x)), ...)
{
    # Assume metadata and data are in the same directory, which seems like a reasonable best practice for local files, but we'll want to generalize it for objects in cloud storage.

    meta = list(`@context` = "http://www.w3.org/ns/csvw"
                , url = "."
                , rowCount = nrow(x)
                , name = name
    )
    # TODO: Allow users to add their own metadata

    # Eventually we'll want to preserve the factor structure in the metadata.
    x = factor_to_character(x)

    col_names = colnames(x)
    R_class = sapply(x, class)

    meta[["tableSchema"]] = list(columns = Map(list
        , url = col_names
        , titles = col_names
        , datatype = map_types(R_class, to = "meta")
    ))

    metafile_path = file.path(datadir, paste0(name, "-metadata.json"))

    # Begin saving
    # TODO: TDD if(dir.exists(datadir) && (notempty)) stop("best practice is to write data in an empty directory. The directory ... contains the files ... Move these files or use a different datadir")
    dir.create(datadir)
    jsonlite::write_json(meta, metafile_path)
    Map(iotools::write.table.raw, x, file = file.path(datadir, col_names), MoreArgs = list(...))

    invisible(NULL)
}


factor_to_character = function(x)
{
    factor_cols = sapply(x, is.factor)
    x[factor_cols] = lapply(x[factor_cols], as.character)
    x
}
