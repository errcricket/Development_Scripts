#!/usr/bin/Rscript 

options(warn=1)

library(ggplot2)

original.parameters=par()
options(width=9999)

myDF <- read.csv('GC_skew', header = TRUE, sep='\t')
attach(myDF)
print(names(myDF))
plot(Count, GC_Skew)
