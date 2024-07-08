library(microbenchmark)
library(ctf)
library(iotools)

#6.8million rows x 22 columns
#Flight Dataset for 2023: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD&QO_anzr=Nv4yv0r%FDb0-gvzr%FDcr4s14zn0pr%FDQn6n

setwd("C:/Users/LapWork/Downloads/flights2023 dataset")

#Sanity check to see if # of obs are the same
check1 <- read.ctf("months/flights2023")
check2 <- read.csv("filghts2023(1).csv",row.names = "X")
isTRUE(nrow(check1) == nrow(check2))

#Testing 1 column
test_ctf <- microbenchmark(
  ctf_orgin_state <- read.ctf("months/flights2023", "ORIGIN_STATE_NM")
  )

test_ctf
boxplot(test_ctf)
#in milliseconds
#expr
#ctf_orgin_state <- read.ctf("months/flights2023", "ORIGIN_STATE_NM")
#     min       lq     mean   median      uq      max neval
#407.5784 414.1298 445.1361 421.5555 447.245 682.5236   100
  

#testing 1 column adjusting from default of 1000 times to 10 times
#since it would take around 10+ hours to finish the csv microbenchmark D:

test_ctf1 <- microbenchmark(
  ctf_orgin_state <- read.ctf("months/flights2023", "ORIGIN_STATE_NM"),
  times = 10, unit="second"
)
test_ctf1 #in seconds
#expr
#ctf_orgin_state <- read.ctf("months/flights2023", "ORIGIN_STATE_NM")
#      min        lq      mean   median        uq       max neval
#0.4199606 0.4274865 0.4538981 0.444983 0.4479771 0.5843112    10

test_csv <- microbenchmark(
  csv_flights = read.csv("filghts2023(1).csv")["ORIGIN_STATE_NM"],times = 10
)
test_csv #in seconds
#       expr      min       lq    mean   median       uq      max neval
#csv_flights 41.68518 43.25829 44.9239 44.78503 45.75674 50.96357    10

boxplot(test_ctf1,unit = "ms",ylab = "time (milliseconds)",xlab = "read.ctf reading one column")
boxplot(test_csv,unit = "ms",ylab = "time (milliseconds)",xlab = "read.csv reading one column")

#avg for ctf is 0.42 seconds
#avg for csv is 41 seconds
#Nearly 100 times faster when reading and selecting one column

#Testing 3 columns
cols = c("DAY_OF_WEEK","ARR_DELAY","DEP_DELAY")

test_ctf2 <- microbenchmark(
  ctf_orgin_state <- read.ctf("months/flights2023", cols),
  times = 10, unit = "second"
)
test_ctf2 #in seconds                                                            
#                                              expr      min
#ctf_orgin_state <- read.ctf("months/flights2023", cols) 2.798411
#      lq     mean   median      uq      max neval
#2.846725 2.921945 2.906899 2.97934 3.144385    10

test_csv1 <- microbenchmark(
  csv_flights = read.csv("filghts2023(1).csv")[cols],times = 10,unit = "second"
)
test_csv1
#       expr      min       lq     mean   median       uq      max neval
#csv_flights 42.21191 42.84613 224.2645 43.33161 44.76317 1850.895    10

boxplot(test_ctf2,unit = "ms",ylab = "time (milliseconds)",xlab = "read.ctf reading three column")
boxplot(test_csv1,unit = "ms",ylab = "time (milliseconds)",xlab = "read.csv reading three column")

#avg for ctf is 2.8 sec
#avg for csv is 42.21 sec
#ctf is over 20 times faster

#ten columns
cols1 <- c("DISTANCE","AIR_TIME","MONTH","DAY_OF_MONTH","DAY_OF_WEEK","ARR_DELAY","DEP_DELAY","ORIGIN_STATE_NM","DEST_STATE_NM","YEAR")

test_ctf3 <- microbenchmark(
  ctf_orgin_state <- read.ctf("months/flights2023", cols1),
  times = 10, unit = "second"
)

test_ctf3
#                                                    expr      min
#ctf_orgin_state <- read.ctf("months/flights2023", cols1) 7.537616
#     lq    mean   median       uq      max neval
#7.660731 7.77769 7.766608 7.866928 8.102262    10

test_csv2 <- microbenchmark(
  csv_flights = read.csv("filghts2023(1).csv")[cols1],times = 10,unit = "second"
)

test_csv2
#       expr      min      lq     mean   median      uq      max neval
#csv_flights 41.19611 41.4535 42.29192 42.58623 42.9014 43.18254    10

boxplot(test_ctf3,unit = "ms",ylab = "time (milliseconds)",xlab = "read.ctf reading ten column")
boxplot(test_csv2,unit = "ms",ylab = "time (milliseconds)",xlab = "read.ctf reading ten column")

#ctf is a bit over 5 time faster than csv when reading 10 columns
