
library(tidyverse)

#--------------------GLM-----------------------------------------------

#사용데이터 
mtcars
str(mtcars)
data = data.frame(cyl = as.ordered(mtcars$cyl),am = mtcars$am, mpg = mtcars$mpg,wt=mtcars$wt, gear=as.factor(mtcars$gear),carb = as.factor(mtcars$carb))
str(data)

##로지스틱 회귀 모형
# 이항랜덤성분 & 로짓연결함수
# glm() 함수 사용!
# 반응변수 ~ 독립변수 꼴
# family에서 랜덤성분의 분포(binomial)와 연결함수(link='logit') 지정!
logit_model = glm(am ~ mpg, family = binomial(link='logit'),data = data) 
summary(logit_model)

#해석
logit_model$coefficients %>% exp() #mpg가 1단위 증가할때 Y=1일 오즈가 exp(0.3)=1.35배만큼 증가한다.

#시각화
ggplot() +
  geom_point(aes(x = mpg, y = am),data=data) +
  geom_line(aes(x = data$mpg, y = fitted(logit_model)), color = "red", size = 1)

rm(logit_model)

##기준범주 로짓 모형
# 다항랜덤성분(명목형) & 로짓연결함수
#library(nnet)의 multinom()함수 사용!
library(nnet)
baseline_model = multinom(gear ~ mpg, data = data) 
summary(baseline_model) # 3을 기준범주로 삼음 / 수준이 3개니까 모델이 2개

#해석
#해석해보세요!

#시각화
ggplot() +
  geom_line(aes(x = data$mpg, y = fitted(baseline_model)[, 1]), size = 1, color = "red") +
  geom_line(aes(x = data$mpg, y = fitted(baseline_model)[, 2]), size = 1, color = "blue") #확률 합치면 1이 된다.

#수준 6개짜리로 한번더!
baseline_model2 = multinom(carb ~ mpg, data = data) #library(nnet)의 multinom()함수 사용!
summary(baseline_model2) # 5을 기준범주로 삼음 / 수준이 6개니까 모델이 5개

#시각화
ggplot() +
  geom_line(aes(x = data$mpg, y = fitted(baseline_model2)[, 1]), size = 1, color = "red") +
  geom_line(aes(x = data$mpg, y = fitted(baseline_model2)[, 2]), size = 1, color = "blue") +
  geom_line(aes(x = data$mpg, y = fitted(baseline_model2)[, 3]), size = 1, color = "green") +
  geom_line(aes(x = data$mpg, y = fitted(baseline_model2)[, 4]), size = 1, color = "yellow") +
  geom_line(aes(x = data$mpg, y = fitted(baseline_model2)[, 5]), size = 1, color = "orange") 
#확률 합치면 1이 된다.

#해석
#해석해보세요!

rm(baseline_model,baseline_model2)


##누적 로짓 모형
# 다항랜덤성분(순서형) & 로짓연결함수
#library(VGAM)의 vglm()함수로 구현 가능!
#glm() 함수와 거의 동일.
#parallel =  : 비례오즈가정 여부를 결정!
library(VGAM) 
cumulative_model = vglm(cyl~mpg, family = cumulative(link='logit', parallel=T),data=data)
summary(cumulative_model) #마찬가지로 식 2개! / 비례오즈 가정에 의해 mpg의 계수는 동일! / 절편만 다름

#해석
#해석해보세요!

#시각화
ggplot() +
  geom_line(aes(x = data$mpg, y = fitted(cumulative_model)[, 1]), size = 1, color = "red") +
  geom_line(aes(x = data$mpg, y = (exp(-31.7172 + 1.7282*data$mpg)/(1+exp(-31.7172 + 1.7282*data$mpg)))), size = 1, color = "blue") #교차하지 않는다!
  
rm(cumulative_model)


##포아송 회귀모형
# 포아송 랜덤성분 & 로그연걸함수
dat = data.frame(count = rpois(32,3),mpg=mtcars$mpg,neg = rnbinom(32,10,0.5)) #도수자료 생성
dat
# family에서 랜덤성분의 분포(poisson)와 연결함수(link='log') 지정!
poisson_model = glm(count ~ mpg, family = poisson(link = "log"), dat)
summary(poisson_model)

#해석
poisson_model$coefficients %>% exp() #mpg가 1단위 증가할때 기대도수가 exp(-0.0007)=0.999배만큼 증가한다.

#시각화
ggplot() +
  geom_point(aes(x = mpg, y = count), dat) +
  geom_line(aes(x = dat$mpg, y = fitted(poisson_model)), color = "red", size = 1)

rm(poisson_model)

##음이항 회귀모형
#음이항 랜덤성분 & 로그연결함수
#library(MASS)의 glm.nb()함수로 구현 가능!
library(MASS) 
negative_model = glm.nb(neg ~ mpg,dat)
summary(negative_model)

#시각화
ggplot() +
  geom_point(aes(x = mpg, y = neg), dat) +
  geom_line(aes(x = dat$mpg, y = fitted(negative_model)), color = "red", size = 1)

rm(negative_model)

##Quasi-Poisson 모형
# 포아송 랜덤성분 & 로그연결함수
# family에서 랜덤성분의 분포(quasipoisson)와 연결함수(link='log') 지정!
quasi_model = glm(count ~ mpg , family = quasipoisson(link = "log"), dat)
summary(quasi_model) #포아송 회귀모형과 똑같지만 회귀계수의 분산이 좀 더 커짐!

#시각화
ggplot() +
  geom_point(aes(x = mpg, y = count), dat) +
  geom_line(aes(x = dat$mpg, y = fitted(quasi_model)), color = "red", size = 1)

rm(quasi_model)


###--------유의성 검정----------------------------------

#포화모델
saturated_model = glm(am ~ mpg * wt , family = binomial(link='logit'),data = data) #교호작용을 추가한 모델!
summary(saturated_model)

#관심모델
guansim_model = glm(am ~ mpg + wt , family = binomial(link='logit'),data = data) #교호작용을 추가한 모델!
summary(guansim_model)

#왈드 검정 (범주나 소표본에서는 비추)
library(lmtest)
waldtest(saturated_model, test = "Chisq") #기각 / 모든 계수가 0은 아니다 -> saturated_model은 쓸만하다
waldtest(guansim_model, test = "Chisq") #기각 / 모든 계수가 0은 아니다 -> guansim_model은 쓸만하다

#가능도비 검정
#lmtest 패키지의 lrtest() 함수 사용
lrtest(saturated_model) #기각 / 모든 계수가 0은 아니다 -> saturated_model은 쓸만하다
lrtest(guansim_model)  #기각 / 모든 계수가 0은 아니다 -> guansim_model은 쓸만하다


###------이탈도 ---------------------------------
simple_model = glm(am ~ mpg, family = binomial(link='logit'),data = data) 

#이탈도로 모형 비교하기 
M0 = lrtest(simple_model,saturated_model)
M1 = lrtest(guansim_model,saturated_model)

#모형 간의 이탈도 차 
M0$Chisq[2] - M1$Chisq[2] #12.49

#pvalue 계산
#simple_model VS guansim_model
pchisq(M0$Chisq[2] - M1$Chisq[2], M0$Df[2] - M1$Df[2], lower.tail = F) #기각 / simple_model 사용할 수 없다!

#가능도비 검정통계량
#simple_model은 guansim_model에 nested 되어있기 때문에 이탈도로 비교 가능!
lrtest(simple_model, guansim_model) #검정통계량 12.49로 모형 간의 이탈도 차이와 같다!

rm(guansim_model, simple_model, saturated_model, M0, M1, data)

###----과산포 문제------------------------------
library(faraway)
gala #과산포 데이터셋 (갈라파고스 섬)
gala = gala[,-2] #수월한 분석 위해 데이터 약간 변형

#일반 포아송 회귀모형
dispersion_model = glm(Species ~ .,family=poisson(link='log'),gala)
summary(dispersion_model) #과산포로 표준오차를 작게 왜곡시키기 때문에 모두 유의하다는결과가 나옴 

#과산포 검정
#AER 패키지의 dispersiontest() 함수로 가능!
library(AER)
dispersiontest(dispersion_model) #기각 / 과산포 존재한다!

#음이항 회귀모형과 Quasi-Poisson모형으로 해결
nb_model = glm.nb(Species ~ ., gala) #음이항 회귀모형
qp_model =  glm(Species ~ ., family = quasipoisson(link = "log"), gala) #Quasi-Poisson 모형
  
summary(nb_model) 
summary(qp_model) # 두 모델 모두 표준오차가 증가 + 유의한 변수 동일 -> 과산포 해결

rm(gala, dispersion_model, nb_model, qp_model)

###----과대영 문제-------------------------------
#과대영 데이터
ovz = data.frame(cnt = c(rpois(10,3),rep(0,22)),mpg=mtcars$mpg,neg = rnbinom(32,10,0.5)) #도수자료 생성
#시각화
ovz %>% group_by(cnt) %>% summarise(n=n()) %>% ggplot() + geom_point(aes(x=cnt,y=n)) + geom_line(aes(x=cnt,y=n,group=1))

#ZIP 모델로 대안
#pscl 패키지의 zeroinfl() 함수를 통해 ZIP 모델 만들 수 있음!
library(pscl)
zip_model = zeroinfl(cnt ~ mpg, data = ovz)
summary(zip_model) # Count Model, Zero-inflation model 두 가지 모델 생성!
