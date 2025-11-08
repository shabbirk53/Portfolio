### Task 1: Usage Data Analysis

# Load necessary libraries
library(ggplot2)
library(dplyr)
library(fitdistrplus)
library(car)


# Load the data
usage_data <- read.csv("BatMobile_Usage_20714352.csv")

# a) Exploratory Analysis
summary(usage_data)
sd((usage_data$A))
sd(usage_data$B)
sd(usage_data$C)

# Plotting the distribution of usage lifetimes for each manufacturer
ggplot(usage_data, aes(x = A)) +
  geom_histogram(aes(y = ..density..), binwidth = 30, fill = "blue", alpha = 0.5) +
  geom_density(color = "blue") +
  labs(title = "Distribution of Usage Lifetimes for Manufacturer A", x = "Usage Lifetime (minutes)", y = "Density")

ggplot(usage_data, aes(x = B)) +
  geom_histogram(aes(y = ..density..), binwidth = 30, fill = "green", alpha = 0.5) +
  geom_density(color = "green") +
  labs(title = "Distribution of Usage Lifetimes for Manufacturer B", x = "Usage Lifetime (minutes)", y = "Density")

ggplot(usage_data, aes(x = C)) +
  geom_histogram(aes(y = ..density..), binwidth = 30, fill = "red", alpha = 0.5) +
  geom_density(color = "red") +
  labs(title = "Distribution of Usage Lifetimes for Manufacturer C", x = "Usage Lifetime (minutes)", y = "Density")


# b) 98% Confidence Interval for Manufacturer B
#T Test
t.test(usage_data$B,conf.level = 0.98)$conf.int

#using sample mean and variance
n=nrow(usage_data_df)
n
sampmean=mean(usage_data$B) # calculate the sample mean
sampvar=var(usage_data$B) # calculate the sample variance
sampsd=sd(usage_data$B) #calculate the sample sd
sampsd
sampmean
sampvar
lower=sampmean-qt(0.99,n-1)*sqrt(sampvar/n) # calculate the lower limit of the confidence interval from the formula
upper=sampmean+qt(0.99,n-1)*sqrt(sampvar/n) # calculate the upper limit of the confidence interval from the formula
lower
upper

# c) Testing Gamma Distribution for Manufacturer C
fit_gamma <- fitdist(usage_data$C, "gamma",method="mle")
ks_test <- ks.test(usage_data$C, "pgamma", shape = fit_gamma$estimate[1], rate = fit_gamma$estimate[2])
fit_gamma$estimate
ks_test

alpha = fit_gamma$estimate[1]
beta = fit_gamma$estimate[2]
hist(usage_data$C,freq=F,main="",xlab="Days")
x<-seq(min(usage_data$C),max(usage_data$C),by=1)
y=dgamma(x,shape=alpha,rate=beta)
lines(x,y,col="red")


### Task 2: Comparison Data Analysis
# Load the comparison data
comparison_data <- read.csv("BatMobile_Comparison_20714352.csv")
summary(comparison_data)

#Remove rows with NA Values
comparison_data <- na.omit(comparison_data)


# a) Visual Summary of the Imputed Data
mean(comparison_data$TurboBM)
mean(comparison_data$BMClassic)
sd(comparison_data$TurboBM)
sd(comparison_data$BMClassic)

##Histograms for comparison
ggplot(comparison_data, aes(x = TurboBM)) +
  geom_histogram(aes(y = ..density..), binwidth = 30, fill = "blue", alpha = 0.5) +
  geom_density(color = "blue") +
  labs(title = "Distribution of Usage Lifetimes for TurboBM Batteries", x = "Usage Lifetime (minutes)", y = "Density")

ggplot(comparison_data, aes(x = BMClassic)) +
  geom_histogram(aes(y = ..density..), binwidth = 30, fill = "green", alpha = 0.5) +
  geom_density(color = "green") +
  labs(title = "Distribution of Usage Lifetimes for BMClassic Batteries", x = "Usage Lifetime (minutes)", y = "Density")

#Box plot
boxplot(comparison_data[2:3],main = "Box Plot of TurboBM and BMClassic Battery 
        Lifetime Usage",xlab="Battery",ylab="Usage Lifetimes (Minutes)")

#Scatter plot
plot(comparison_data$TurboBM,comparison_data$BMClassic,
     main = "Scatter Plot of Usage Lifetimes for Batteries", 
     xlab = "Usage Lifetime of TurboBM Batteries (Minutes)", ylab = "Usage Lifetime of BMClassic Batteries (Minutes)",geom_abline(mapping = ))

# b) Correlation between TurboBM and BMClassic usage lifetimes
correlation <- cor.test(comparison_data$TurboBM, comparison_data$BMClassic)
correlation

# c) Testing if the variances of TurboBM and BMClassic usage lifetimes are the same
var_test <- var.test(comparison_data$TurboBM, comparison_data$BMClassic)
var_test

# d) Testing if the mean usage lifetime of TurboBM is at least 65 minutes longer than BMClassic
mean_diff <- mean(comparison_data$TurboBM) - mean(comparison_data$BMClassic)
t_test <- t.test(comparison_data$TurboBM, comparison_data$BMClassic, alternative = "greater",mu=65)
mean_diff
t_test

# Print the results
cat("T-test statistic:", t_test$statistic, "\n")
cat("P-value:", t_test$p.value, "\n")
cat("Mean difference:", mean_diff, "\n")

# Determine if there is evidence that the mean usage lifetime of TurboBM is at least 65 minutes longer than BMClassic
if (mean_diff >= 65 && t_test$p.value < 0.05) {
  cat("There is evidence that the mean usage lifetime of a TurboBM battery is at least 65 minutes longer than the mean usage lifetime of a BMClassic battery.\n")
} else {
  cat("There is no evidence that the mean usage lifetime of a TurboBM battery is at least 65 minutes longer than the mean usage lifetime of a BMClassic battery.\n")
}


### Task 3: Laboratory Data Analysis
# Load the laboratory data
lab_data <- read.csv("BatMobile_Laboratory_20714352.csv")
# a) Relationship between usage lifetime and temperature
ggplot(lab_data, aes(x = Temperature, y = Lifetime)) +
  geom_point() +
  labs(title = "Relationship between Temperature and Usage Lifetime", x = "Temperature (°C)", y = "Usage Lifetime (minutes)")

#Plot Temp and Temp^2
# Scatter plot of Lifetime vs temp
ggplot(df, aes(x = Temperature, y = Lifetime)) +
  geom_point(alpha = 0.7, color = "black") +
  stat_smooth(method = "lm", color = "red", se = FALSE)+
  labs(title = "Scatter Plot: Temperature vs Lifetime", x = "Temperature", y = "Lifetime") +
  theme_minimal()

# Scatter plot of Lifetime vs temp squared
ggplot(df, aes(x = Temperature_sqr, y = Lifetime)) +
  geom_point(alpha = 0.7, color = "black") +
  stat_smooth(method = "lm", color = "red", se = FALSE)+
  labs(title = "Scatter Plot: Temperature Squared vs Lifetime", x = "Temperature Squared", y = "Lifetime") +
  theme_minimal()


lab_data$Temperature_sqr<-(lab_data$Temperature)^2
model_quadratic<-lm(Lifetime~Temperature_sqr,data=lab_data)
model_quadratic
hist(model_quadratic$residuals,xlab="Residuals",freq=FALSE)
curve(dnorm(x,0,sd(model_quadratic$residuals)),-100,100,col=2,add=TRUE) 
# curve(dnorm(x,0,summary(model)$sigma),-5,5,lty=2,add=TRUE)
plot(model_quadratic$fitted.values,model_quadratic$residuals,xlab="Fitted values",ylab="Residuals")
abline(h=0,lty=2)


# b,c,d) Fit a linear model to the usage lifetime
model<-lm(Lifetime~.,data=lab_data) # Fit a linear model with Lifetime as the response variable and everything else "." as covariates
summary(model) # Display a summary of the model
AIC(model)
step_model<-step(model)
step_model
# Try removing each covariate in turn till the best one is not found with lowest AIC.
hist(step_model$residuals,xlab="Residuals",main ="",freq=FALSE)
curve(dnorm(x,0,sd(step_model$residuals)),-200,200,col=2,add=TRUE) 
# curve(dnorm(x,0,summary(model)$sigma),-5,5,lty=2,add=TRUE)
plot(step_model$fitted.values,step_model$residuals,xlab="Fitted values",ylab="Residuals")
abline(h=0,lty=2)

# e) 75% Prediction Interval for a specific case
new_data <- data.frame(Temperature = 11.8, Recharge = 147, Memory = 64, Level = "Low", Device = "B", Temperature_sqr=11.8^2)
predict(step_model, newdata = new_data, interval = "prediction", level = 0.75)