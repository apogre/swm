getwd()
setwd("/home/apradhan/proj/swm")
data = read.csv("follow.csv",header = TRUE)

plot(data$friends_count,data$followers_count)

head(data)
