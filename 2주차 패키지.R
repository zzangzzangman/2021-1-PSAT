## chapter 1

# 문제 0
library(tidyverse)
library(data.table)
library(VIM)

setwd("C:/Users/bounc/Desktop/2주차패키지")
data = fread("data.csv")
str(data)

#문제 1

data = data %>% select(-ends_with("2")) 

#문제 2
aggr(data, prop=F, numbers = T, col=c('lightyellow','pink'))
# 각 변수 당 8개의 NA가 있고 OC변수에는 0개, bedcount는 5개, employee1에는 10개, ownerchange 변수에는 12가 있다
#특히, NA가 있을경우 주로 "1"로 끝나는 변수가 통째로 결측치인 경우가 많았다. 이는 거의 아무런 정보가 없는 관찰값이 몇개 있다는 의미이다. 

#문제3-1
mean_imputation = function(x){
  ifelse(is.na(x),mean(x,na.rm=T),x)
  
}

is.integer64 <- function(x){
  class(x)=="integer64"
}
data = data %>% mutate_if(is.integer64,as.numeric) 
numeric_data = data %>% select(where(is.numeric)) %>% lapply(mean_imputation) %>% as.data.frame() 
colSums(is.na(numeric_data))

#문제3-2
mode_imputation = function(x){
  
  ifelse(is.na(x),names(which.max(table(x))),x)
  
}
categorical_data = data %>% select(where(is.character)) %>% lapply(mode_imputation) %>% as.data.frame() 
colSums(is.na(categorical_data))

#문제4
data = cbind(numeric_data,categorical_data) %>% relocate(ownerChange, .after= employee1) %>% relocate(OC)
data
data = data %>% mutate(OC = ifelse(OC=='open',1,0))

#문제5 
str(data)

##chapter2
library(caret)
library(MLmetrics)
library(randomForest)

#문제1
set.seed(1234)
index = data$OC %>% createDataPartition(p=0.3,list=F)
train_data = data[-index,]
validation_set = data[index,]

#문제2
model = glm(OC~.,family = binomial(), data = train_data )
summary(model)
prob= predict(model,validation_set,type='response') #pi hat
pred_cutoff = ifelse(prob>0.5,1,0) # cutoff에 따른 분류
Accuracy(validation_set$OC,pred_cutoff) #0.91

#문제3
step(model,direction='both') #OC ~ revenue1 + salescost1 + noi1 + interest1 + quickAsset1 + receivableS1 + nonCAsset1 + tanAsset1 + receivableL1 + ownerChange 
model2 = glm(OC ~ revenue1 + salescost1 + noi1 + interest1 + quickAsset1 + receivableS1 + nonCAsset1 + tanAsset1 + receivableL1 + ownerChange,family = binomial(), data = train_data)
summary(model2)
prob2= predict(model2,validation_set,type='response') #pi hat
pred_cutoff2 = ifelse(prob2>0.5,1,0) # cutoff에 따른 분류
Accuracy(validation_set$OC,pred_cutoff2) # 0.9340659

#문제4
acc_rf = expand.grid(mtry=c(3,4,5),acc=NA)
acc_rf

#문제5
set.seed(1234)
a = sample(1:5,nrow(data),replace=T)

for(i in 3:5){
  temp = NULL
  for(k in 1:5){
    cv_train = data[-which(a==k),]
    cv_test = data[which(a==k),]
    m = randomForest(OC ~ revenue1 + salescost1 + noi1 + interest1 + quickAsset1 + receivableS1 + nonCAsset1 + tanAsset1 + receivableL1 + ownerChange,ntree=10,mtry=i,data=cv_train)
    m_prob = predict(m,cv_test,type='response')
    m_cutoff = ifelse(m_prob>0.5,1,0)
    m_accuracy = Accuracy(m_cutoff,cv_test$OC)
    temp = c(temp,m_accuracy)
  }
  acc_rf[i-2,"acc"] = mean(temp)
}
acc_rf


#문제6
acc_rf %>% arrange(desc(acc)) %>% head(1)
  
#문제7
rf = randomForest(as.factor(OC) ~ revenue1 + salescost1 + noi1 + interest1 + quickAsset1 + receivableS1 + nonCAsset1 + tanAsset1 + receivableL1 + ownerChange,ntree=10,mtry=3,data=train_data)
rf_imp = varImpPlot(rf,main="") %>% as.data.frame() %>% rownames_to_column(var='name')
rf_imp %>%ggplot(aes(x=MeanDecreaseGini,y=reorder(name,MeanDecreaseGini))) + geom_point(col='pink') + geom_segment(aes(x=0,xend=MeanDecreaseGini,y=name,yend=name),col='pink',size=1) +theme_bw() + ylab("Variable Name")

## chapter3
library(MASS)

#문제1
set.seed(1234)
boston_index = Boston$medv %>% createDataPartition(p=0.2,list=F)
boston_train = Boston[-boston_index,]
boston_test = Boston[boston_index,]

#문제2
RMSE_rf = expand.grid(mtry=c(3,4,5),ntree=c(10,100,200),RMSE=c(NA))
RMSE_rf

#문제3
set.seed(1234)
boston_mtry= rep(3:5,3)
boston_ntree=rep(c(10,100,200),each=3)
b = sample(1:5,nrow(Boston),replace=T)

for(i in 1:9){
  temp=NULL
  for(k in 1:5){
    
    b_train = Boston[-which(b==k),]
    b_test = Boston[which(b==k),]
    b_model = randomForest(medv~.,ntree=boston_ntree[i],mtry=boston_mtry[i],data=b_train)
    b_pred = predict(b_model,b_test)
    b_RMSE = RMSE(b_pred,b_test$medv)
    temp = c(temp, b_RMSE)
  }
  RMSE_rf[i,"RMSE"]=mean(temp)
}
RMSE_rf

#문제4
RMSE_rf %>% top_n(n=-1, wt=RMSE)

#문제 5
boston_rf = randomForest(medv~.,ntree=200,mtry=5,data=boston_train)
boston_pred = predict(boston_rf,boston_test) 
boston_RMSE = RMSE(boston_pred, boston_test$medv) 
boston_RMSE

