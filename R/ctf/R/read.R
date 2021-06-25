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
    # TODO: check there's only one metadata file, make sure it exists, etc.
    if(dir.exists(location)){
        metafile = list.files(location, pattern = "*.json")
        metafile = file.path(location, metafile)
    } else {
        metafile = location
    }

    meta = jsonlite::read_json(metafile)
    colschema = meta[["tableSchema"]][["columns"]]

    # TODO: Handle case of multiple titles identifying a single column, but that's far down the road.
    alltitles = sapply(colschema, `[[`, "titles")

    if(is.null(columns)){
        titles = alltitles
    } else {
        titles = columns
        selected_cols = match(columns, alltitles)
        # TODO: TDD Check for valid column names
        colschema = colschema[selected_cols]
    }

    colfiles = sapply(colschema, `[[`, "url")
    colfiles = file.path(dirname(metafile), colfiles)


    metatypes = sapply(colschema, `[[`, "datatype")
    R_scan_what = map_types(metatypes, to = "R")

    # TODO: handle missing
    nmax = meta[["rowCount"]]

    # We could imagine generalizing the format to allow different characters to separate records rather than just newlines.
    # For example, multiline text.
    sep = "\n"

    columns = Map(scan, file = colfiles, what = Rtypes, nmax = nmax, sep = sep, ...)

    out = do.call(data.frame, columns)
    browser()

    colnames(out) = titles
    
    # The metadata contains info on ALL the columns, rather than just the ones selected.
    # I'm not sure this is ideal.
    attr(out, "ctf_metadata") = meta

    out
}


type_lookup = function()
{
    read.table(header = TRUE, text = "
meta        R
boolean     logical
integer     integer
double      double
string      character
")
}


scan_what_args = function(meta_types)
{
    lookup = type_lookup()
    locs = match(meta_types, lookup[["meta"]])
    funcs = lookup[locs, "R"]
    lapply(funcs, do.call, list())  # What a strange line of code this is!
}
