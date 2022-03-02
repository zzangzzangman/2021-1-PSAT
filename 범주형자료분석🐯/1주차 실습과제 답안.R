library(data.table)
library(tidyverse)
data = fread('1주차실습과제.csv') %>% mutate_all(as.factor)
str(data)

#1.원하는 변수 2개 골라서 2차원 분할표 만들어보기
a=table(data$sex,data$h1n1_vaccine)

#2. 원하는 변수 3개 골라서 3차원 분할표 만들어보기
table(data$sex,data$h1n1_vaccine,data$income_poverty)
ftable(data$sex,data$h1n1_vaccine,data$income_poverty)

#3. 독립성 검정 시행하기 
#명목
chisq.test(a) #기각, 독립아님, 성별과 접종여부는 연관성있음

library(DescTools)
GTest(a)

library(vcd)
assocstats(a)

#순서
library(vcdExtra)
b=table(data$income_poverty,data$h1n1_knowledge)
CMHtest(b,types = 'cor') #기각, 독립아님, 소득수준과 독감에 대한 지식수준은 연관성있음

MHChisqTest(b)


#4.비율의 차이, 상대위험도, 오즈비 계산하기
n = apply(a,1,sum) 
n 
a_con = sweep(a,1,n,'/')

#비율의 차이
a_con[1,1] - a_con[2,1] 
#상대위험도
a_con[1,1] / a_con[2,1] 
#오즈비
(a_con[1,1] / a_con[1,2]) / (a_con[2,1] / a_con[2,2])

#epiR
library(epiR)
epi.2by2(a)
