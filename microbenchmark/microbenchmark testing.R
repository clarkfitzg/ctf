library(microbenchmark)
library(ctf)
library(iotools)
library(tidyverse)

#6.8million rows x 22 columns
#Flight Dataset for 2023: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD&QO_anzr=Nv4yv0r%FDb0-gvzr%FDcr4s14zn0pr%FDQn6n

setwd("C:/Users/LapWork/Downloads/flights2023 dataset")

#Adjusted the default for microbenchmark of 1000 times to 100 times for time convenience 

#testing 1 column 

column1 <- microbenchmark(
  ctf_one <- read.ctf("flights2023", "ORIGIN_STATE_NM"), 
  io_one <- read.csv.raw("filghts2023(1).csv")["\"ORIGIN_STATE_NM\""],
  csv_one <- read.csv("filghts2023(1).csv")["ORIGIN_STATE_NM"],
  times = 100, unit="second"
)

boxplot(column1,unit = "s",ylab = "time (seconds)",xlab = "Time Reading One Column",names=c("read.ctf","read.csv.raw","read.csv"))

#Testing 3 columns
cols = c("DAY_OF_WEEK","ARR_DELAY","DEP_DELAY")
colsio = c("\"DAY_OF_WEEK\"","\"ARR_DELAY\"","\"DEP_DELAY\"")

column3 <- microbenchmark(
  ctf_three <- read.ctf("flights2023", cols),
  io_three <- read.csv.raw("filghts2023(1).csv")[colsio],
  csv_three <- read.csv("filghts2023(1).csv")[cols],
  times = 100, unit = "second"
)

boxplot(column3,unit = "s",ylab = "time (seconds)",xlab = "Time Reading Three Column",names=c("read.ctf","read.csv.raw","read.csv"))

#ten columns
cols1 <- c("DISTANCE","AIR_TIME","MONTH","DAY_OF_MONTH","DAY_OF_WEEK","ARR_DELAY","DEP_DELAY","ORIGIN_STATE_NM","DEST_STATE_NM","YEAR")
cols1io <- c("\"DISTANCE\"","\"AIR_TIME\"","\"MONTH\"","\"DAY_OF_MONTH\"","\"DAY_OF_WEEK\"","\"ARR_DELAY\"","\"DEP_DELAY\"","\"ORIGIN_STATE_NM\"","\"DEST_STATE_NM\"","\"YEAR\"")

column10 <- microbenchmark(
  ctf_ten <- read.ctf("flights2023", cols1),
  io_ten <- read.csv.raw("filghts2023(1).csv")[colsio],
  csv <- read.csv("filghts2023(1).csv")[cols1],
  times = 100, unit = "second"
)

boxplot(column10,unit = "s",ylab = "time (seconds)",xlab = "Time Reading Ten Column",names=c("read.ctf","read.csv.raw","read.csv"))

#read over everything
entire <- microbenchmark(
  ctf_whole <- read.ctf("flights2023"),
  io_whole <- read.csv.raw("filghts2023(1).csv"),
  csv_whole <- read.csv("filghts2023(1).csv"),
  times = 100, unit = "second"
)

boxplot(entire,unit = "s",ylab = "time (seconds)",xlab = "Time to Reading Flights 2023 Dataset",names=c("read.ctf","read.csv.raw","read.csv"))
