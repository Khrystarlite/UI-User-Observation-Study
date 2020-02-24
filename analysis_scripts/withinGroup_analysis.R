rm(list = ls())


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

group_A_KV1 <- (key_V1$Subject_1 + key_V1$Subject_2) / 2
group_B_KV1 <- (key_V1$Subject_3 + key_V1$Subject_4 + key_V1$Subject_5) / 3
group_A_KV2 <- (key_V2$Subject_3 + key_V2$Subject_4 + key_V2$Subject_5) / 3
group_B_KV2 <- (key_V2$Subject_1 + key_V2$Subject_2) / 2

group_A_TV1 <- (time_V1$Subject_1 + time_V1$Subject_2) / 2000
group_B_TV1 <- (time_V1$Subject_3 + time_V1$Subject_4 + time_V1$Subject_5) / 3000
group_A_TV2 <- (time_V2$Subject_3 + time_V2$Subject_4 + time_V2$Subject_5) / 3000
group_B_TV2 <- (time_V2$Subject_1 + time_V2$Subject_2) / 2000

gA_avgK1_ER <- sqrt((target_key - group_A_KV1)^2)
gA_avgK2_ER <- sqrt((target_key - group_A_KV2)^2)
gA_avgT1_ER <- sqrt((target_time - group_A_TV1)^2)
gA_avgT2_ER <- sqrt((target_time - group_A_TV2)^2)

gB_avgK1_ER <- sqrt((target_key - group_B_KV1)^2)
gB_avgK2_ER <- sqrt((target_key - group_B_KV2)^2)
gB_avgT1_ER <- sqrt((target_time - group_B_TV1)^2)
gB_avgT2_ER <- sqrt((target_time - group_B_TV2)^2)

Vers = c(1, 2)

mu_KA = c(mean(gA_avgK1_ER[1:8]), mean(gA_avgK2_ER[1:8]))
mu_KB = c(mean(gB_avgK1_ER[1:8]), mean(gB_avgK2_ER[1:8]))
plot(factor(c(1,2)),c(10,10), col="blue", ylim = c(0,5),main="Keystroke Error Over Both versions",xlab="Temporal Version Order",ylab="Error (sec)")
points(mu_KA,col="blue")
points(mu_KB, col="green")
segments(Vers[1],mu_KA[1],Vers[2],mu_KA[2],col="blue")
segments(Vers[1],mu_KB[1],Vers[2],mu_KB[2],col="green")
legend("bottomright",legend=c("Discrete First", "Integrated First"),col=c("blue", "green"),lty=1:2, cex=0.8)

mu_TA = c(mean(gA_avgT1_ER[1:8]), mean(gA_avgT2_ER[1:8]))
mu_TB = c(mean(gB_avgT1_ER[1:8]), mean(gB_avgT2_ER[1:8]))
plot(factor(c(1,2)),c(20,20),ylim=c(0,10), col="blue",main="Trial Time Error Over Both versions",xlab="Temporal Version Order",ylab="Trial Time (sec)")
points(mu_TA,col="blue")
points(mu_TB, col="green")
segments(Vers[1],mu_TA[1],Vers[2],mu_TA[2],col="blue")
segments(Vers[1],mu_TB[1],Vers[2],mu_TB[2],col="green")
legend("bottomright",legend=c("Discrete First", "Integrated First"),col=c("blue", "green"),lty=1:2, cex=0.8)



mu_KA = c(mean(group_A_KV1[1:8]), mean(group_A_KV2[1:8]))
mu_KB = c(mean(group_B_KV1[1:8]), mean(group_B_KV2[1:8]))
plot(factor(c(1,2)),c(10,10), col="blue", ylim = c(37,41),main="Keystroke Error Over Both versions",xlab="Temporal Version Order",ylab="Error (sec)")
points(mu_KA,col="blue")
points(mu_KB, col="green")
segments(Vers[1],mu_KA[1],Vers[2],mu_KA[2],col="blue")
segments(Vers[1],mu_KB[1],Vers[2],mu_KB[2],col="green")
legend("bottomright",legend=c("Discrete First", "Integrated First"),col=c("blue", "green"),lty=1:2, cex=0.8)

mu_TA = c(mean(group_A_TV1[1:8]), mean(group_A_TV2[1:8]))
mu_TB = c(mean(group_B_TV1[1:8]), mean(group_B_TV2[1:8]))
plot(factor(c(1,2)),c(100,100),y_lim=c(0,10), col="blue",main="Trial Time Over Both versions",xlab="Trial",ylab="Error (sec)")
points(mu_KA,col="blue")
points(mu_KB, col="green")
segments(Vers[1],mu_KA[1],Vers[2],mu_KA[2],col="blue")
segments(Vers[1],mu_KB[1],Vers[2],mu_KB[2],col="green")
legend("bottomright",legend=c("Discrete First", "Integrated First"),col=c("blue", "green"),lty=1:2, cex=0.8)
