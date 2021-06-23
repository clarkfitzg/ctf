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
#' d <- system.file("extdata", "vgsales", "vgsales-metadata.json", package = "ctf")
#'
#' # Read all the columns
#' vgsales <- read.ctf(d)
#'
#' # Read two columns, Name and Rank
#' vgsales2 <- read.ctf(d, columns = c("Name", "Rank"))
read.ctf = function(location, columns = NULL, ...) 
{
    # TODO: Assume for the moment that location is a metadata file.
    # We'll use TDD and handle directories later
    metafile = location

    meta = jsonlite::read_json(metafile)
    colmeta = meta[["tableSchema"]][["columns"]]

    colfiles = sapply(colmeta, `[[`, "url")
    colfiles = file.path(dirname(metafile), colfiles)


    metatypes = sapply(colmeta, `[[`, "datatype")
    Rtypes = map_types(metatypes, to = "R")

    # TODO: handle missing
    nmax = meta[["rowCount"]]

    # We could imagine generalizing the format to allow different characters to separate records rather than just newlines.
    # For example, multiline text.
    sep = "\n"

    # TODO: Handle columns = NULL
    columns = Map(scan, file = colfiles, what = Rtypes, nmax = nmax, sep = sep, ...)

    out = do.call(data.frame, columns)

    # TODO: Handle case of multiple titles, but that's far down the road
    colnames(out) = sapply(colmeta, `[[`, "titles")
    
    attr(out, "ctf_metadata") = meta

    out
}


map_types = function(x, to = "R")
{
    tm = read.table(header = TRUE, text = "
meta        R
integer     integer
string      character
")

    if(to == "R"){
        from = "meta"
    } else if(to == "meta"){
        from = "R"
    }

    locs = match(x, tm[[from]])
    tm[locs, to]
}
