library(rCharts)
library(devtools)
install_github('rCharts','ramnathv')
install.packages(c("devtools", "RCurl", "rjson", "bit64","httr","ROAuth"))
install_github('rCharts', 'ramnathv')

getwd()
setwd("/home/apradhan/proj/swm")
data = read.csv("full_data1.csv",header = TRUE)
summary(data)
data[data==0]<-1


data$log_friends_count<-log(data$friends_count)
data$log_followers_count<-log(data$followers_count)


summary(data)

log_data <- data.frame(data$log_friends_count,data$log_followers_count)

wss <- (nrow(log_data)-1)*sum(apply(log_data,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(log_data,centers=i)$withinss)

plot(1:15, wss, type="b", xlab="Number of Clusters",ylab="Within groups sum of squares")

userMeans.log <- kmeans(log_data, centers=5, iter.max=10, nstart=100)
log_data$cluster=factor(userMeans.log$cluster)
data$cluster <-log_data$cluster


write.csv(data, file = "cluster_lfc_5.csv", row.names = FALSE)

head(data)

newdata <- data[ which(data$followers_count<10),]

data1<-data
data1$ratio = data1$friends_count/data1$followers_count

attach(newdata)
plot(friends_count,followers_count)

detach(newdata)
