#' Read CTF data
#' 
#' Read external CTF data into the corresponding R data frame.
#' 
#' @param location location of the CTF data, either a file path to a CTF metadata JSON file, or a directory containing a single CTF metadata JSON file.
#' @param columns names of the columns to read.
#'      If missing, then read in all columns.
#' @param nrows integer, the maximum number of rows to read in.
#'      If missing, then read in all rows.
#' @return data frame
#' @seealso \code{\link{write.ctf}} to write CTF
#' @export
#' @examples
#' # An example CTF metadata file included in this package
#' d <- system.file("extdata", "vgsales", "vgsales-metadata.json", package = "ctf")
#'
#' # Read all the rows and columns
#' vgsales <- read.ctf(d)
#'
#' # Read 10 rows of two columns, Name and Rank
#' vgsales2 <- read.ctf(d, columns = c("Name", "Rank"), nrows = 10)
read.ctf = function(location, columns, nrows)
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

    if(missing(columns)){
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
    type_iotools = map_types(metatypes, to = "type_iotools")

    if(missing(nrows)){
        # TODO: handle missing in metadata
        nrows = meta[["rowCount"]]
    }

    columns = Map(read_one_col, con = colfiles, type = type_iotools, nrows = nrows)

    out = do.call(data.frame, columns)

    colnames(out) = titles
    
    # The metadata contains info on ALL the columns, rather than just the ones selected.
    # I'm not sure this is ideal.
    attr(out, "ctf_metadata") = meta

    out
}


map_types = function(x, to)
{
	# These 4 are really all we can do.
    lookup = utils::read.table(header = TRUE, text = "
meta        type_iotools
boolean     logical
integer     integer
double      numeric
string      character
")

    if(to == "type_iotools"){
        from = "meta"
    } else if(to == "meta"){
        from = "type_iotools"
    }

    locs = match(x, lookup[[from]])
    lookup[locs, to]
}


read_one_col = function(con, ...)
{
    iotools::mstrsplit(iotools::readAsRaw(con), sep = NA, ncol = 1L, ...)
}
