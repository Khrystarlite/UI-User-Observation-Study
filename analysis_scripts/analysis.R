

# Clear out lingering environment variables.
rm(list = ls())

#
# # Targets
# Targets <- read.table("../data/targets/target_keystrokes.txt",sep=",",header=FALSE)
#
# # Subject 1
# sub_1_V1 <- read.table("../data/subject_1/key_v1.txt",sep=",",header=FALSE)
# sub_1_V2 <- read.table("../data/subject_1/key_v2.txt",sep=",",header=FALSE)
# # Subject 2
# sub_2_V1 <- read.table("../data/subject_2/key_v1.txt",sep=",",header=FALSE)
# sub_2_V2 <- read.table("../data/subject_2/key_v2.txt",sep=",",header=FALSE)
# # Subject 3
# sub_3_V1 <- read.table("../data/subject_3/key_v1.txt",sep=",",header=FALSE)
# sub_3_V2 <- read.table("../data/subject_3/key_v2.txt",sep=",",header=FALSE)
# # Subject 4
# sub_4_V1 <- read.table("../data/subject_4/key_v1.txt",sep=",",header=FALSE)
# sub_4_V2 <- read.table("../data/subject_4/key_v2.txt",sep=",",header=FALSE)
# # Subject 5
# sub_5_V1 <- read.table("../data/subject_5/key_v1.txt",sep=",",header=FALSE)
# sub_5_V2 <- read.table("../data/subject_5/key_v2.txt",sep=",",header=FALSE)
#
# avg_key_V1 <- sub_1_V1$V1 + sub_2_V1$V1 + sub_3_V1$V1 + sub_4_V1$V1 + sub_5_V1$V1
# avg_key_V2 <- sub_1_V2$V1 + sub_2_V2$V1 + sub_3_V2$V1 + sub_4_V2$V1 + sub_5_V2$V1
# avg_time_V1 <- sub_1_V1$V2 + sub_2_V1$V2 + sub_3_V1$V2 + sub_4_V1$V2 + sub_5_V1$V2
# avg_time_V2 <- sub_1_V2$V2 + sub_2_V2$V2 + sub_3_V2$V2 + sub_4_V2$V2 + sub_5_V2$V2
#
# target_key <-Targets$V1


# Load Data
key_V1 <- read.table("../data/keystrokes_V1.txt",sep=",",header=TRUE)
key_V2 <- read.table("../data/keystrokes_V2.txt",sep=",",header=TRUE)
time_V1 <- read.table("../data/time_V1.txt",sep=",",header=TRUE)
time_V2 <- read.table("../data/time_V2.txt",sep=",",header=TRUE)

target_key <- key_V1$Target
target_time <- time_V1$Target / 1000
avg_key_V1 <- (key_V1$Subject_1 + key_V1$Subject_2 + key_V1$Subject_3 + key_V1$Subject_4 + key_V1$Subject_5) / 5
avg_key_V2 <- (key_V2$Subject_1 + key_V2$Subject_2 + key_V2$Subject_3 + key_V2$Subject_4 + key_V2$Subject_5) / 5
avg_time_V1 <- (time_V1$Subject_1 + time_V1$Subject_2 + time_V1$Subject_3 + time_V1$Subject_4 + time_V1$Subject_5) / 5000
avg_time_V2 <- (time_V2$Subject_1 + time_V2$Subject_2 + time_V2$Subject_3 + time_V2$Subject_4 + time_V2$Subject_5) / 5000


plot(target_key,target_time,main ="Target Performance",xlab = "Target Accuracy (keystrokes)",ylab = "Target Speed (s)",col="red")
legend("topleft",legend=c("Target"),col=c("red"),lty=1:2, cex=0.8)
plot(avg_key_V1,avg_time_V1,main ="Average V1 Performance",xlab = "Average V1 Accuracy",ylab = "Average V1 Speed",col="blue")
points(target_key,target_time,col="red")
legend("topleft",legend=c("Target","V1"),col=c("red","blue"),lty=1:2, cex=0.8)
plot(avg_key_V2,avg_time_V2,main ="Average V2 Performance",xlab = "Average V2 Accuracy",ylab = "Average V2 Speed",col="green")
points(target_key,target_time,col="red")
legend("topleft",legend=c("Target","V2"),col=c("red","green"),lty=1:2, cex=0.8)

plot(target_key,target_time,main ="Performance",xlab = "Accuracy",ylab = "Reaction Time",col="red",xlim = c(0,70),ylim=c(0,50))
points(avg_key_V1,avg_time_V1,col="blue")
points(avg_key_V2,avg_time_V2,col="green")
legend("topleft",legend=c("Target","V1","V2"),col=c("red","blue","green"),lty=1:2, cex=0.8)

Trial <- factor(c(1,2,3,4,5,6,7,8,9,10))
adjTrial <- factor(c(1:8))
# avgK1_ER <- (target_key - avg_key_V1)
# avgK2_ER <- (target_key - avg_key_V2)
# avgT1_ER <- (target_time - avg_time_V1)
# avgT2_ER <- (target_time - avg_time_V2)



avgK1_ER <- sqrt((target_key - avg_key_V1)^2)
avgK2_ER <- sqrt((target_key - avg_key_V2)^2)
avgT1_ER <- sqrt((target_time - avg_time_V1)^2)
avgT2_ER <- sqrt((target_time - avg_time_V2)^2)

barplot(avgK1_ER, main="Average V1 Error",xlab = "Trial", names = Trial,ylab="Error (keystrokes)",col="blue",ylim=c(0,15))
barplot(avgK2_ER, main="Average V2 Error",xlab="Trial",names = Trial,ylab="Error (keystrokes)",col="green")
barplot(avgK1_ER[1:8], main="Average V1 Error Adjusted",xlab = "Trial", names = adjTrial, ylab="Error (keystrokes)",col="blue",ylim=c(0,15))
barplot(avgK2_ER[1:8], main="Average V2 Error Adjusted",xlab="Trial",names = adjTrial,ylab="Error (keystrokes)",col="green")


barplot(avgT1_ER, main="Average V1 Speed Error",xlab="Trial",names = Trial,ylab="Error (sec)",col="blue",ylim=c(0,20))
barplot(avgT2_ER, main="Average V2 Speed Error",xlab="Trial",names = Trial,ylab="Error (sec)",col="green",ylim=c(0,20))
barplot(avgT1_ER[1:8], main="Average V1 Speed Error",xlab="Trial",names = adjTrial,ylab="Error (sec)",col="blue",ylim=c(0,20))
barplot(avgT2_ER[1:8], main="Average V2 Speed Error",xlab="Trial",names = adjTrial,ylab="Error (sec)",col="green",ylim=c(0,20))

axis(side=1, at=c(0:10))
legend("topleft",legend=c("V2 Speed Err"),col=c("green"),lty=1:2, cex=0.8)
target_key
plot.new()
plot(Trial,target_key,main ="Accuracy Performance",xlab = "Trial",ylab = "Accuracy",col="red", ylim = c(0,70), pch=1)
points(Trial,avg_key_V1,col="blue")
points(Trial,avg_key_V2,col="green")
legend("bottomleft",legend=c("Target","Avg V1", "Avg V2"),col=c("black","blue", "green"),lty=1:2, cex=0.8)

barplot(avg_time_V1[1:8],main ="V1 Speed Performance adj",xlab = "Trial",names = adjTrial,ylab = "Trial Time (sec)",col="blue", ylim= c(0,50),pch=1)
barplot(avg_time_V2[1:8],main ="V2 Speed Performance",xlab = "Trial",names = adjTrial,ylab = "Trial Time (sec)",col="green", ylim= c(0,50),pch=1)
# plot(Trial,target_time,main ="Speed Performance",xlab = "Trial",ylab = "Reaction Time",col="red")
axis(side=1, at=c(0:10))
points(Trial,avg_time_V1,col="blue")
points(Trial,avg_time_V2,col="green")
legend("bottomleft",legend=c("Target","Avg V1", "Avg V2"),col=c("red","blue", "green"),lty=1:2, cex=0.8)

# plot(Trial,avg_key_V1,main ="Performance",xlab = "Target Accuracy",ylab = "Target Speed",col="blue")
# axis(side=1, at=c(0:10))
# plot(Trial,target_key,main ="Target Performance",xlab = "Target Accuracy",ylab = "Target Speed",col="green")
# axis(side=1, at=c(0:10))


# SSE
avgk1SSE = sum(avgK1_ER) # = 48.6
avgk2SSE = sum(avgK2_ER) # = 54.8
avgT1SSE = sum(avgT1_ER) # = 46672.8
avgkT2SSE = sum(avgT2_ER) # - 56967

t.test(avg_key_V1,avg_key_V2)
t.test(avg_time_V1,avg_time_V2)

mean(avg_key_V1)
mean(avg_time_V1)
mean(avgK1_ER)
mean(avgT1_ER)

mean(avg_key_V2)
mean(avg_time_V2)
mean(avgK2_ER)
mean(avgT2_ER)




adjTarg = target_key[1:8]
adj_key_v1 = avg_key_V1[1:8]
adj_key_v2 = avg_key_V2[1:8]
adj_time_v1 = avg_time_V1[1:8]
adj_time_v2 = avg_time_V2[1:8]
adj_K1_Err = avgK1_ER[1:8]
adj_K2_Err = avgK2_ER[1:8]
adj_T1_Err = avgT1_ER[1:8]
adj_T2_Err = avgT2_ER[1:8]



mean(avg_key_V1[1:8])
mean(adj_K1_Err[1:8])
mean(avg_time_V1[1:8])
mean(adj_T1_Err[1:8])

mean(avg_key_V2[1:8])
mean(adj_K2_Err[1:8])
mean(avg_time_V2[1:8])
mean(adj_T2_Err[1:8])

plot(adj_K1_Err,adj_key_v1,main ="V1  Speed v Accuracy",xlab = "Error (keystrokes)",ylab = "Trial Time (s)",col="Blue")
plot(adj_K2_Err,adj_key_v2,main ="V2 Speed v Accuracy",xlab = "Error (keystrokes)",ylab = "Trial Time (s)",col="green")
