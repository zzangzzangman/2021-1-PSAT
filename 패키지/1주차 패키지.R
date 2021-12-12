##chapter 1
#문제 0
library(plyr)
library(tidyverse)
library(data.table)
setwd("C:/Users/bounc/Desktop/1주차패키지")
data = fread("data.csv")

#문제 1
str(data)
colSums(is.na(data)) #NA는 confirmed_date에 3개
data %>% sapply(., function(x) length(unique(x)))

#문제2-1
data = na.omit(data)

#문제2-2
data = data[-c(which(data[,2]=="" | data[,3]=="" | data[,6]==""))] #2,3,6
colSums(is.na(data)) #NA는 전부 0개
data %>% sapply(., function(x) length(unique(x)))

#문제3
data = data[data$country == "Korea"]
data = data[,-4]

#문제4
for(i in 1:length(data$province)){
  if (data$province[i]=="서울"){
    data$province[i]="서울특별시"
  } else if(data$province[i]=="부산"){
    data$province[i]="부산광역시"
  }else if(data$province[i]=="대구"){
    data$province[i]="대구광역시"
  }else if(data$province[i]=="인천"){
    data$province[i]="인천광역시"
  }else if(data$province[i]=="대전"){
    data$province[i]="대전광역시"
  }else if(data$province[i]=="세종"){
    data$province[i]="세종특별자치시"
  }else if(data$province[i]=="울산"){
    data$province[i]="울산광역시"
  }else if(data$province[i]=="제주도"){
    data$province[i]="제주특별자치도"
  }
}
unique(data$province)

#문제5
data$confirmed_date = as.Date(data$confirmed_date) 
str(data)

#문제6
confirmed_number = data %>% group_by(data$confirmed_date) %>% summarise(n=n())
confirmed_number


#문제7

wday = case_when(
  weekdays(data$confirmed_date) %in% c('월요일','화요일','수요일','목요일','금요일') ~'주중',
  weekdays(data$confirmed_date) %in% c('토요일','일요일') ~ '주말',
)
wday

#문제8
new_data = data %>% group_by(data$age,data$confirmed_date) %>% summarise(n=n()) 
tapply(new_data$n,new_data$`data$age`,summary)


##chapter2
#문제1
graph_data = data %>% group_by(data$confirmed_date) %>% summarise(n=n())
graph_data %>% ggplot(aes(x=`data$confirmed_date`,y=n)) + geom_line(color='lightblue') + labs(title='코로나 확진자수 추이 \n -국내인 기준', x ="confirmed_date", y = "confirmed_number")  + theme_bw() + theme(plot.title = element_text(face='bold',hjust=0.5)) + geom_point(aes(x=`data$confirmed_date`[28],y=n[28]),color='navy') + annotate(geom="text",x=as.Date('2020-3-11'),y=143,label='2020-3-11(143명)',color='navy',fontface=2,hjust=1.3)  

#문제1-2
graph_data2 = data %>% group_by(data$province,data$confirmed_date) %>% summarise(n=n()) 
graph_data2 %>% ggplot(aes(x=`data$confirmed_date`,y=n,color=`data$province`)) + geom_line() +facet_wrap(~`data$province`) + xlab("confirmed_date") + ylab("confirmed_number") + labs(color = "province")

#문제2
graph_data3 = data %>% group_by(state,province) %>% summarise(n=n())
graph_data3 %>% ggplot(aes(x=reorder(province,n),y=n,fill=state,color=state)) + geom_bar(stat='identity',alpha=0.4) + coord_flip() + xlab("지역") + ylab("확진자 수")

#문제3
new_data %>% ggplot(aes(x=`data$age`,y=n,fill=`data$age`,color=`data$age`)) + geom_boxplot(outlier.shape = NA,alpha=0.5) + stat_boxplot(geom ='errorbar')  + xlab("age") + ylab("일단위 확진자수") + theme_bw() + labs(fill = "age", color = "age")

#문제3-2
result = aov(new_data$n ~as.factor(new_data$`data$age`), data=new_data)
summary(result) #p값이 매우 작게 나오므로 귀무가설 기각, 즉 나이대별로 일단위확진자수의 차이가 있다. 

#문제4
library(raster)
library(rgeos)
library(rgdal)
library(maptools)



m = readOGR('CTPRVN_202101/TL_SCCO_CTPRVN.shp')
head(m)
map = fortify(m,region='CTP_KOR_NM') 
head(map)
map_data = data %>% group_by(.$province) %>% summarise(n=n()) %>% rename(id=`.$province`)
map_data
korea = left_join(map,map_data,by='id')
korea
ggplot() + geom_polygon(data=korea, aes(x=long, y=lat, group=group, fill=n)) + scale_fill_gradient(low='white', high='red') + ggtitle('지역별 누적 확진자 수')

##chapter3
library(MASS)
library(corrplot)
library(caret)
library(MLmetrics)

#문제 1
boston = MASS::Boston
corrplot(cor(boston),method='number',type='upper') #rad와 tax의 상관계수가0.91로 상당히 높고 몇몇 변수들도 0.7이상의 상관계수를 갖는다.  다중공선성 가능성 크다. 

#문제2
boston %>% gather(key='key',value='val',-medv)%>% ggplot(aes(x=val,y=medv))+geom_point() + facet_wrap(~key,scales = "free_x") + geom_smooth(color='lightblue',method='lm') + ggtitle('Scatter plot of dependent variables vs Median Value (medv)')

#문제3
set.seed(1234)
index = sample(1:nrow(boston),size=nrow(boston)*0.7) #70%를 뽑아서 인덱스를 보여줌
boston_train = boston[index,]
boston_test = boston[-index,]

#문제3-2
boston_lm =lm(medv~.,data=boston_train)
summary(boston_lm) # crim, zx, chas, nox, rm, dis, rad, tax, ptratio,black,lstat의 계수는 유의미하다.
pred = predict(boston_lm,boston_test)
sqrt(mean((boston_test$medv-pred)^2))

#문제 3-3
#model의 complexity를 적절히 조정해서 model variance나 model bias를 줄인다

#문제4
lm_data = data.frame(value=boston_lm$coefficients) %>% rownames_to_column(var ='name' )
lm_data %>% ggplot(aes(x=reorder(name ,value),y=value,fill=value,color=value)) + geom_bar(stat='identity',alpha=0.2) + coord_flip() + xlab('intercept and variables') + geom_text(aes(label=round(value,2)),position = position_stack(vjust=0.5),color='black') + scale_fill_gradient2(low='blue',mid='yellow',high='red') + scale_color_gradient2(low='blue',mid='yellow',high='red') + theme_bw( ) + theme(legend.position = "none")

