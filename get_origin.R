#!/usr/bin/Rscript 

options(warn=1)

library(ggplot2)
#library('data.table')
#library('plyr')
#library(reshape2)
#library(scales)

original.parameters=par()
options(width=9999)

myDF <- read.csv('GC_skew', header = TRUE, sep='\t')
attach(myDF)
print(names(myDF))
#plot(Count, New_Skew)
plot(Count, GC_Skew)
#plot('GC_Skew', 'Count')
#p <- ggplot(myDF, aes(x=GC_Skew))
#p + geom_line()
