# 문제0 
library(tidyverse)
library(data.table)
library(gridExtra)
setwd('C:/Users/bounc/Desktop/3주차패키지')
train_data=fread('data.csv')
test_data=fread('test.csv')

# 문제1
mean_imputation = function(x){
    ifelse(is.na(x),mean(x,na.rm=T),x)
}
train_data = train_data %>% mutate(bmi=as.numeric(bmi)) %>% mutate(bmi=mean_imputation(bmi))
str(train_data)

# 문제2
train_data = train_data %>% mutate_if(is.character,as.factor)
str(train_data)


# 문제3
train_data = train_data %>% select(-id)
str(train_data)

# 문제4
is.integer = function(x){
  class(x)=="integer"
}
train_data = train_data %>% mutate_if(is.integer,as.factor) # 범주형 변수 생성
p1 = train_data %>% select(where((is.factor))) %>% gather(key='variable', value='value',-stroke) %>% filter(stroke==1) %>% ggplot(aes(x=variable,fill=value)) + geom_bar(position = 'fill',alpha=0.6) + coord_flip() + labs(title="stroke : 1", y = "",fill="") + theme_bw() + theme(plot.title = element_text(hjust = 0.5),legend.position = "bottom") 
p2 = train_data %>% select(where((is.factor))) %>% gather(key='variable', value='value',-stroke) %>% filter(stroke==0) %>% ggplot(aes(x=variable,fill=value)) + geom_bar(position = 'fill',alpha=0.6) + coord_flip() + labs(title="stroke : 0", y = "",fill='') + theme_bw() + theme(plot.title = element_text(hjust = 0.5),legend.position = "bottom") 
grid.arrange(p1,p2,ncol=2)

# 문제5
p3 = train_data %>% select(where((is.numeric)),stroke) %>% gather(key='variable', value='value',-stroke) %>% filter(stroke==1) %>% ggplot(aes(x=value,color=variable)) + geom_density() + labs(title="stroke : 1",color='') + theme_bw() + theme(plot.title = element_text(hjust = 0.5)) 
p4 = train_data %>% select(where((is.numeric)),stroke) %>% gather(key='variable', value='value',-stroke) %>% filter(stroke==0) %>% ggplot(aes(x=value,color=variable)) + geom_density() + labs(title="stroke : 0",color='') + theme_bw() + theme(plot.title = element_text(hjust = 0.5)) 
grid.arrange(p3,p4,nrow=2)

# 문제6
cate_var = train_data %>% select(where(is.factor),-stroke) %>% colnames()
result = data.frame(cate_var,chi=rep(NA,7),stringsAsFactors = F)
for(i in 1:7){
  data_table = table(as_vector(train_data[,cate_var[i],with=F]),train_data$stroke)
  a= chisq.test(data_table)
  if(a$p.value < 0.05){
    result$chi[i] = 'denied'
  } else{
    result$chi[i] = 'accept'
  }
}
result

# 문제7
train_data = train_data %>% select(-c(gender,Residence_type))

# 문제8
test_data = test_data %>% mutate(bmi=as.numeric(bmi)) %>% mutate(bmi=mean_imputation(bmi))
str(test_data)

test_data = test_data %>% mutate_if(is.character,as.factor)
test_data = test_data %>% mutate_if(is.integer,as.factor) # 범주형 변수 생성
str(test_data)

test_data = test_data %>% select(-c(id,gender,Residence_type))
str(test_data)


## chapter2
library(catboost)
library(caret)
library(MLmetrics)

#문제0
# Catboost는 gradient boosting의 한 종류로, ordered boosting, random permutation, Ordered Target Encoding 등의 기법을 통해 오버피팅을 감소시킨다. 
# 대표적인 파라미터로는 손실함수, 트리 깊이, 학습률 등이 있다.  

#문제1
logloss_cb = expand.grid(depth=c(4,6,8),iterations=c(100,200),logloss=NA)
logloss_cb

#문제2
set.seed(1234)
index = createFolds(train_data$stroke,k=5,list=F)
cv_start = Sys.time()
for(i in 1:6){
  temp = NULL
  
  for(k in 1:5){
    
    cv_train = train_data[which(index==k),]
    cv_test = train_data[which(index==k),]
    
    #catboost에 맞는 형식으로 전환
    train_pool = catboost.load_pool(data=cv_train[,-"stroke"],label = as.double(cv_train$stroke))
    test_pool = catboost.load_pool(data=cv_test[,-"stroke"],label = as.double(cv_train$stroke))
    
    #시작시간 및 모수 설정
    start =Sys.time()
    param =list(loss_function='Logloss',random_seed = 1234, iterations = logloss_cb[i,2],depth=logloss_cb[i,1],custom_loss ='Logloss') 
    
    #catboost 학습 및 시간 측정
    cat = catboost.train(learn_pool=train_pool,test_pool = test_pool, params = param)
    test_error <- read.table("catboost_info/test_error.tsv", sep = "\t", header = TRUE)
    temp = c(temp,test_error[nrow(test_error),'Logloss'])
    
  }
  logloss_cb[i,'logloss'] = min(temp)
  print(min(cat_runtime))
}

Sys.time()-cv_start
logloss_cb

#문제3
logloss_cb %>% arrange(logloss) %>% head(1)

#문제4

#catboost에 맞는 형식으로 전환
train_pool_t = catboost.load_pool(data=train_data[,-"stroke"],label = as.double(train_data$stroke))
test_pool_t = catboost.load_pool(data=test_data[,-"stroke"],label = as.double(test_data$stroke))

#depth =8, iteration =200으로 모수 설정
param =list(loss_function='Logloss',random_seed = 1234, iterations = 200,depth=8,custom_loss ='Logloss') 

cat_total = catboost.train(learn_pool=train_pool_t,test_pool = test_pool_t, params = param)
test_error = read.table("catboost_info/test_error.tsv", sep = "\t", header = TRUE)
test_error[nrow(test_error),'Logloss']


#chapter 3

library(factoextra)
library(cluster)
#문제1
scale_train_data = train_data %>% select(where(is.numeric)) %>% scale()

#문제2
p5 = fviz_nbclust(scale_train_data,kmeans,method='wss')
p6 = fviz_nbclust(scale_train_data,kmeans,method='silhouette')
grid.arrange(p5,p6,ncol=2)
#적절한 k 값은 오른쪽 그래프에서 점선으로 나타난 4

#문제3
set.seed(1234)
km = kmeans(scale_train_data, centers = 3, nstart = 1, iter.max =30)
fviz_cluster(km,data=scale_train_data) + theme_bw()

#문제4
pp = train_data %>% select(where(is.numeric)) %>% mutate(cluster= km$cluster) 
p7 = pp %>% ggplot(aes(x=factor(cluster),y=age)) + geom_boxplot(outlier.shape = NA, alpha=0.6,fill=c( '#845ec2', '#ffc75f', '#ff5e78'),color=c( '#845ec2', '#ffc75f', '#ff5e78')) + stat_boxplot(geom='errorbar',color=c( '#845ec2', '#ffc75f', '#ff5e78')) + labs(x='cluster') + theme_bw()
p8 = pp %>% ggplot(aes(x=factor(cluster),y=avg_glucose_level)) + geom_boxplot(outlier.shape = NA, alpha=0.6,fill=c( '#845ec2', '#ffc75f', '#ff5e78'),color=c( '#845ec2', '#ffc75f', '#ff5e78')) + stat_boxplot(geom='errorbar',color=c( '#845ec2', '#ffc75f', '#ff5e78')) + labs(x='cluster') + theme_bw()
p9 = pp %>% ggplot(aes(x=factor(cluster),y=bmi)) + geom_boxplot(outlier.shape = NA, alpha=0.6,fill=c( '#845ec2', '#ffc75f', '#ff5e78'),color=c( '#845ec2', '#ffc75f', '#ff5e78')) + stat_boxplot(geom='errorbar',color=c( '#845ec2', '#ffc75f', '#ff5e78')) + labs(x='cluster') + theme_bw()
grid.arrange(p7,p8,p9,ncol=3)
#cluster 2는 age에서 가장 낮은 평균값을 보이고, cluster1은 avg_glucose_level에서 가장 높은 평균값을 보인다. bmi에서는 세cluster의 평균이 비슷해보인다.
