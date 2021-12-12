library(tidyverse)
library(data.table)
library(plyr)
library(vcd)
library(vcdExtra)
library(GoodmanKruskal)
library(DescTools)


dat=fread('C:/Users/bounc/Desktop/백신 주제/final_train.csv') %>% mutate_all(as.factor)
str(dat)


#y변수 독립성 검정
dat_table=table(dat$h1n1_vaccine,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #y변수끼리는 독립 아님


#y와 x변수 독립성 검정

dat_table=table(dat$h1n1_concern,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$h1n1_knowledge,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$behavioral_antiviral_meds,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) # 기각X

dat_table=table(dat$behavioral_avoidance,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$behavioral_face_mask,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$behavioral_wash_hands,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$behavioral_large_gatherings,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$behavioral_outside_home,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$behavioral_touch_face,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$doctor_recc_h1n1,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$doctor_recc_seasonal,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$chronic_med_condition,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$child_under_6_months,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각X

dat_table=table(dat$health_worker,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$health_insurance,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$opinion_h1n1_vacc_effective,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$opinion_h1n1_risk,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$opinion_h1n1_sick_from_vacc,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$opinion_seas_vacc_effective,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$opinion_seas_risk,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$opinion_seas_sick_from_vacc,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$age_group,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$education,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$race,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$sex,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$income_poverty,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$marital_status,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$rent_or_own,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$employment_status,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$hhs_geo_region,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$census_msa,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$household_adults,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$household_children,dat$seasonal_vaccine)
dat_table %>% MHChisqTest() #기각

dat_table=table(dat$employment_industry,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

dat_table=table(dat$employment_occupation,dat$seasonal_vaccine)
dat_table %>% chisq.test(correct=F) #기각

#명목형 연관성
k=datt %>% select(-c(h1n1_concern,h1n1_knowledge,respondent_id,opinion_h1n1_vacc_effective,opinion_h1n1_risk,opinion_h1n1_sick_from_vacc,opinion_seas_vacc_effective,opinion_seas_risk,opinion_seas_sick_from_vacc,age_group,income_poverty,education,employment_industry)) %>% select(a=behavioral_antiviral_meds, b = behavioral_avoidance, c=behavioral_face_mask, d=behavioral_wash_hands, e= behavioral_large_gatherings,f=behavioral_outside_home, g=behavioral_touch_face, h=doctor_recc_h1n1, i= doctor_recc_seasonal, j=chronic_med_condition,kk=child_under_6_months, l=health_worker, m= health_insurance, n=race,o=sex, p= marital_status, q=rent_or_own, r=employment_status,s=hhs_geo_region, t=census_msa, u=employment_occupation, v=household_adults, w=household_children)
ya=GKtauDataframe(k)
plot(ya)
ya

#33.6% behavioral_large_gatherings / behavioral_outside_home
#53.3% doctor_recc_seasonal /  doctor_recc_h1n1
#26.1% health_worker /child_under_6_months
#32.1%'employment_occupation /  health_worker
#65.9% employment_occupation / employment_status
#marital_status / household adults 0.36

#순서형 상관관계 비교
dat2=fread('C:/Users/bounc/Desktop/백신 주제/training_set_features.csv')

q=dat2 %>% select(c(h1n1_concern,h1n1_knowledge,opinion_h1n1_vacc_effective,opinion_h1n1_risk,opinion_h1n1_sick_from_vacc,opinion_seas_vacc_effective,opinion_seas_risk,opinion_seas_sick_from_vacc,age_group,income_poverty,education))
q$age_group <- q$age_group %>% revalue(c('18 - 34 Years' = 0, '35 - 44 Years' = 1, '45 - 54 Years' = 2, '55 - 64 Years' = 3, '65+ Years' = 4))  %>% as.numeric()

# education
q$education <- q$education %>% revalue(c('< 12 Years' = 0, '12 Years' = 1, 'Some College' = 2, 'College Graduate' =3)) %>% as.numeric()

# income_poverty
q$income_poverty <- q$income_poverty %>% revalue(c('Below Poverty' = 0, '<= $75,000, Above Poverty' = 1, '> $75,000' = 2)) %>% as.numeric()

aa=matrix(0,11,11)

for (i in 1:11){
  for(j in 1:11){
    temp=cor.test(q[[i]],q[[j]],method='spearman')
    aa[i,j]=temp$estimate
  }
  
}
row.names(aa) = c('h1n1_concern','h1n1_knowledge','opinion_h1n1_vacc_effective','opinion_h1n1_risk','opinion_h1n1_sick_from_vacc','opinion_seas_vacc_effective','opinion_seas_risk','opinion_seas_sick_from_vacc','age_group','income_poverty','education')
colnames(aa) = c('h1n1_concern','h1n1_knowledge','opinion_h1n1_vacc_effective','opinion_h1n1_risk','opinion_h1n1_sick_from_vacc','opinion_seas_vacc_effective','opinion_seas_risk','opinion_seas_sick_from_vacc','age_group','income_poverty','education')
aa[lower.tri(aa)]=NA
aa

library(corrplot)
corrplot(aa,type='upper',method='number')

qq =cbind(q$income_poverty,q$education)
GKgamma(qq)
#spearman 상관계수
# opinion_h1n1_risk / opinion_seas_risk : 56.4%
# opinion_h1n1_sick_from_vacc / opinion_seas_sick_from_vacc : 50.2%
# opinion_h1n1_vacc_effective / opinion_seas_vacc_effective : 44.4%
# income_poverty / education : 41.5%
# h1n1_concern / opinion_h1n1_risk : 38.6%
# h1n1_concern / opinion_h1n1_sick_from_vacc : 36.8%
# opinion_seas_vacc_effective / opinion_seas_risk : 36.6% 
# opinion_h1n1_risk / opinion_h1n1_sick_from_vacc : 33.7%
# h1n1_concern  / opinion_seas_risk : 33.6%
# h1n1_knowledge / education : 30.7%


## 변수 시각화 #y변수랑 같이 고려하기
dat3=fread('C:/Users/bounc/Desktop/백신 주제/training_set_labels.csv')
datt = join(dat2,dat3, by='respondent_id') %>%  lapply(napro) %>% as.data.frame() %>% mutate_all(as.factor)

train = datt %>% select(doctor_recc_h1n1,doctor_recc_seasonal,chronic_med_condition,child_under_6_months,health_worker,health_insurance,h1n1_vaccine,seasonal_vaccine)

#h1n1
train %>% gather(-c(h1n1_vaccine, seasonal_vaccine), key = 'medical', value = 'value') %>% ggplot(aes(x = factor(value),fill=h1n1_vaccine)) +geom_bar()+ facet_wrap(~medical) +theme_bw() + scale_fill_manual(values=c('#86D1C7','#E892C4')) 
train %>% gather(-c(h1n1_vaccine, seasonal_vaccine), key = 'medical', value = 'value') %>% ggplot(aes(x = factor(value),fill=h1n1_vaccine)) +geom_bar(position='fill')+ facet_wrap(~medical) +theme_bw() + scale_fill_manual(values=c('#86D1C7','#E892C4')) 

#seasonal
train %>% gather(-c(h1n1_vaccine, seasonal_vaccine), key = 'medical', value = 'value') %>% ggplot(aes(x = factor(value),fill=seasonal_vaccine)) +geom_bar()+ facet_wrap(~medical) +theme_bw() + scale_fill_manual(values=c('#86D1C7','#E892C4')) 
train %>% gather(-c(h1n1_vaccine, seasonal_vaccine), key = 'medical', value = 'value') %>% ggplot(aes(x = factor(value),fill=seasonal_vaccine)) +geom_bar(position='fill')+ facet_wrap(~medical) +theme_bw() + scale_fill_manual(values=c('#86D1C7','#E892C4')) 


# h1n1
#의사 말 잘듣는 사람들
prop.table(table(datt$h1n1_vaccine,datt$doctor_recc_h1n1),2)
datt %>% ggplot(aes(x=doctor_recc_h1n1,fill=h1n1_vaccine)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4')) 
                                                                                                                                                                    
prop.table(table(datt$h1n1_vaccine,datt$doctor_recc_seasonal),2)
datt %>% ggplot(aes(x=doctor_recc_seasonal,fill=h1n1_vaccine)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4')) 

prop.table(table(datt$h1n1_vaccine,datt$chronic_med_condition),2)
datt %>% ggplot(aes(x=chronic_med_condition,fill=h1n1_vaccine)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4'))

prop.table(table(datt$h1n1_vaccine,datt$child_under_6_months),2)
datt %>% ggplot(aes(x=child_under_6_months,fill=h1n1_vaccine)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4'))

#의사와 소득 -> 좋은 의사가 추천? 의미 없.
datt %>% ggplot(aes(x=doctor_recc_h1n1,fill=income_poverty)) + geom_bar(position='fill') #+ scale_fill_manual(values=c('#86D1C7','#E892C4')) 

#만성질환자에게 백신 권유? -> 2배 가까이나 더 많이.-> 의사는 역할을 다하고 있다.
prop.table(table(datt$doctor_recc_h1n1,datt$chronic_med_condition),2)
datt %>% ggplot(aes(x=chronic_med_condition,fill=doctor_recc_h1n1)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4','#6397D6')) 
prop.table(table(datt$doctor_recc_seasonal,datt$chronic_med_condition),2)
datt %>% ggplot(aes(x=chronic_med_condition,fill=doctor_recc_seasonal)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4','#6397D6')) 


#6개월 미만 아이를 자주 접하는 직업? -> 산부인과? 산후조리원?  I(의료계)와 U / n(의사),q가 많음
datt %>% ggplot(aes(x=employment_industry,fill=child_under_6_months)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4','#6397D6'))
datt %>% ggplot(aes(x=employment_occupation,fill=child_under_6_months)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4','#6397D6'))

#직업과 성별 
datt %>% ggplot(aes(x=employment_occupation,fill=sex)) + geom_bar(position='fill')  + scale_fill_manual(values=c('#E892C4','#86D1C7')) #m(간호사) 여성 비율 압도적
datt %>% ggplot(aes(x=employment_industry,fill=sex)) + geom_bar(position='fill')  + scale_fill_manual(values=c('#E892C4','#86D1C7'))

#직업과 접종여부
datt %>% ggplot(aes(x=employment_occupation,fill=h1n1_vaccine)) + geom_bar(position='fill') #n(의사), w, m(간호사)가 압도적
datt %>% ggplot(aes(x=employment_industry,fill=h1n1_vaccine)) + geom_bar(position='fill') #I(의료진), T가 압도적

#직업과 소득
datt %>% ggplot(aes(x=employment_occupation,fill=income_poverty)) + geom_bar(position='fill') 
datt %>% ggplot(aes(x=employment_industry,fill=income_poverty)) + geom_bar(position='fill') 

#직업과 나이
datt %>% ggplot(aes(x=employment_occupation,fill=age_group)) + geom_bar(position='fill') 

datt %>% filter(employment_industry=='T') %>% select(employment_occupation) #T와 w는 세트 -> 아이를 많이 만나진 않지만 접종비율 상당히 높음+남성비율 높음 + 소득 높음 + 주로 젊은 층
datt %>% filter(employment_industry=='I') %>% group_by(employment_occupation) %>% dplyr::summarise(n=n())
datt %>% filter(employment_industry=='U') %>% group_by(employment_occupation) %>% dplyr::summarise(n=n()) #b,i,j
datt %>% filter(employment_occupation=='q') %>% group_by(employment_industry) %>% dplyr::summarise(n=n()) #I, J와 세트 + 여성비율 높음 + 6개월 아기 많이 + 소득 별로 +의료종사자 비율 높음 -> 간호조무사..?

#의료진과 성별/소득/6개월 미만 아이
datt %>% ggplot(aes(x=health_worker,fill=sex)) + geom_bar(position='fill') + scale_fill_manual(values=c('#E892C4','#86D1C7'))
datt %>% ggplot(aes(x=health_worker,fill=income_poverty)) + geom_bar(position='fill') 
datt %>% ggplot(aes(x=health_worker,fill=child_under_6_months)) + geom_bar(position='fill') 

#직업 중 의료종사자
datt %>% ggplot(aes(x=employment_industry,fill=health_worker)) + geom_bar(position='fill') #의료진은 I 산업군
datt %>% ggplot(aes(x=employment_occupation,fill=health_worker)) + geom_bar(position='fill') #의료진은 m(간호사),n(의사) 


prop.table(table(datt$h1n1_vaccine,datt$health_worker),2)
datt %>% ggplot(aes(x=health_worker,fill=h1n1_vaccine)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4'))

prop.table(table(datt$h1n1_vaccine,datt$health_insurance),2)
datt %>% ggplot(aes(x=health_insurance,fill=h1n1_vaccine)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4'))

# seasonal
prop.table(table(datt$seasonal_vaccine,datt$doctor_recc_h1n1),2)
datt %>% ggplot(aes(x=doctor_recc_h1n1,fill=seasonal_vaccine)) + geom_bar() + scale_fill_manual(values=c('#86D1C7','#E892C4'))

#의사 말 잘듣는 사람들
prop.table(table(datt$seasonal_vaccine,datt$doctor_recc_seasonal),2)
datt %>% ggplot(aes(x=doctor_recc_seasonal,fill=seasonal_vaccine)) + geom_bar(position='fill') + scale_fill_manual(values=c('#86D1C7','#E892C4'))

prop.table(table(datt$seasonal_vaccine,datt$chronic_med_condition),2)
datt %>% ggplot(aes(x=chronic_med_condition,fill=seasonal_vaccine)) + geom_bar()+ scale_fill_manual(values=c('#86D1C7','#E892C4'))

prop.table(table(datt$seasonal_vaccine,datt$child_under_6_months),2)
datt %>% ggplot(aes(x=child_under_6_months,fill=seasonal_vaccine)) + geom_bar()+ scale_fill_manual(values=c('#86D1C7','#E892C4'))

prop.table(table(datt$seasonal_vaccine,datt$health_worker),2)
datt %>% ggplot(aes(x=health_worker,fill=seasonal_vaccine)) + geom_bar()+ scale_fill_manual(values=c('#86D1C7','#E892C4'))

prop.table(table(datt$seasonal_vaccine,datt$health_insurance),2)
datt %>% ggplot(aes(x=health_insurance,fill=seasonal_vaccine)) + geom_bar() + scale_fill_manual(values=c('#86D1C7','#E892C4'))

## 재범주화 

datt$age_group = datt$age_group %>% revalue(c('18 - 34 Years' = 0, '35 - 44 Years' = 1, '45 - 54 Years' = 2, '55 - 64 Years' = 3, '65+ Years' = 4)) 
datt$education = datt$education %>% revalue(c('< 12 Years' = 0, '12 Years' = 1, 'Some College' = 2, 'College Graduate' =3)) 
datt$income_poverty = datt$income_poverty %>% revalue(c('Below Poverty' = 0, '<= $75,000, Above Poverty' = 1, '> $75,000' = 2)) 
datt$employment_industry = datt$employment_industry %>%  
  revalue(c('pxcmvdjn' = 'A', 'rucpziij' = 'B', 'wxleyezf' = 'C', 'saaquncn' = 'D', 'xicduogh' = 'E',
            'ldnlellj' = 'F', 'wlfvacwt' = 'G', 'nduyfdeo' = 'H', 'fcxhlnwr' = 'I', 'vjjrobsf' = 'J',
            'arjwrbjb' = 'K', 'atmlpfrs' = 'L', 'msuufmds' = 'N', 'xqicxuve' = 'M', 'phxvnwax' = 'O',
            'dotnnunm' = 'P', 'mfikgejo' = 'Q', 'cfqqtusy' = 'R', 'mcubkhph' = 'S', 'haxffmxo' = 'T',
            'qnlwzans' = 'U'))
datt$employment_occupation = datt$employment_occupation %>% 
  revalue(c('xgwztkwe' = 'a', 'xtkaffoo' = 'b', 'emcorrxb' = 'c', 'vlluhbov' ='d', 'xqwwgdyp' = 'e',
            'ccgxvspp' = 'f', 'qxajmpny' = 'g', 'kldqjyjy' ='h', 'mxkfnird' = 'i', 'hfxkjkmi' = 'j',
            'bxpfxfdn' = 'k', 'ukymxvdu' = 'l', 'cmhcxjea' = 'n', 'haliazsg' = 'm', 'dlvbwzss' = 'o',
            'xzmlyyjv' = 'p', 'oijqvulv' = 'q', 'rcertsgn' = 'r', 'tfqavkke' = 's', 'hodpvpew' = 't',
            'uqqtjvyb' = 'u', 'pvmttkik' = 'v', 'dcjcmpih' = 'w'))
datt$hhs_geo_region = datt$hhs_geo_region %>% 
  revalue(c('oxchjgsf' = 'Region1', 'bhuqouqj' = 'Region2', 'qufhixun' = 'Region3', 'lrircsnp' = 'Region4',
            'atmpeygn' = 'Region5', 'lzgpxyit' = 'Region6', 'fpwskwrf' = 'Region7', 'mlyzmhmf' = 'Region8',
            'dqpwygqj' = 'Region9', 'kbazzjca' = 'Region10'))
datt$household_adults = datt$household_adults %>% revalue(c('1'=1,'2'=1,'3'=1,'0'=0))
datt$household_children = datt$household_children %>% revalue(c('1'=1,'2'=1,'3'=1,'0'=0))
datt = datt %>% mutate(live_alone= ifelse(household_adults == 0 & household_children ==0,1,ifelse(household_adults == 'na' | household_children =='na','na',0)))
datt$marital_status = datt$marital_status %>% revalue(c('Married'=1,'Not Married'=0))
datt$rent_or_own = datt$rent_or_own %>% revalue(c('Rent'=0,'Own'=1))
datt$sex = datt$sex %>% revalue(c('Male'=1,'Female'=0))

datt %>% ggplot(aes(x=household_adults,fill=h1n1_vaccine)) + geom_bar(position ='fill' ) + scale_fill_manual(values=c('#86D1C7','#E892C4'))
datt %>% ggplot(aes(x=household_children,fill=h1n1_vaccine)) + geom_bar(position ='fill' ) + scale_fill_manual(values=c('#86D1C7','#E892C4'))
datt %>% ggplot(aes(x=live_alone,fill=h1n1_vaccine)) + geom_bar(position ='fill' ) + scale_fill_manual(values=c('#86D1C7','#E892C4'))

datt %>% ggplot(aes(x=household_adults,fill=seasonal_vaccine)) + geom_bar(position ='fill' ) + scale_fill_manual(values=c('#86D1C7','#E892C4'))
datt %>% ggplot(aes(x=household_children,fill=seasonal_vaccine)) + geom_bar(position ='fill' ) + scale_fill_manual(values=c('#86D1C7','#E892C4'))
datt %>% ggplot(aes(x=live_alone,fill=seasonal_vaccine)) + geom_bar(position ='fill' ) + scale_fill_manual(values=c('#86D1C7','#E892C4'))

## 회귀 분석

# H1N1 회귀(na제거)
d_h1n1 = join(dat,dat2, by='respondent_id') %>% select(-c(respondent_id ,seasonal_vaccine)) %>% mutate_all(as.factor) %>% na.omit()
h1n1_lm = glm(h1n1_vaccine ~.,family = binomial,data=d_h1n1)
summary(h1n1_lm)
lm1=step(h1n1_lm)
summary(lm1)

napro = function(x){
  ifelse(is.na(x) | x=="","na",x)
  
}
#na 인정
d2_h1n1 = join(dat,dat2, by='respondent_id') %>% select(-c(respondent_id ,seasonal_vaccine)) %>% lapply(napro) %>% as.data.frame() %>% mutate_all(as.factor)
str(d2_h1n1)
h1n1_lm2 = glm(h1n1_vaccine ~.,family = binomial,data=d2_h1n1)
summary(h1n1_lm2)
lm2=step(h1n1_lm2)
summary(lm2)

# seasonal 회귀(na제거)
d_sea = join(dat,dat2, by='respondent_id') %>% select(-c(respondent_id ,h1n1_vaccine )) %>% mutate_all(as.factor) %>% na.omit()
sea_lm = glm( seasonal_vaccine ~.,family = binomial,data=d_sea)
summary(sea_lm)
lm3=step(sea_lm)
summary(lm3)

napro = function(x){
  ifelse(is.na(x) | x=="","na",x)
  
}
#na 인정
d2_sea = join(dat,dat2, by='respondent_id') %>% select(-c(respondent_id ,h1n1_vaccine)) %>% lapply(napro) %>% as.data.frame() %>% mutate_all(as.factor)
str(d2_sea)
sea_lm2 = glm(seasonal_vaccine ~.,family = binomial,data=d2_sea)
summary(sea_lm2)
lm4=step(sea_lm2)
summary(lm4)

## 거리계산
library(cluster)
k = k %>% mutate_if(is.integer,as.factor) %>% mutate_if(is.character,as.factor)
dis = daisy(k[1:1000,],metric=c('gower')) #k 개수 일단 1000개로
summary(dis)

#군집 개수 지정
sil_width <- c(NA)
for(i in 2:13){  
  pam_fit <- pam(dis, diss = TRUE, k = i)  
  sil_width[i] <- pam_fit$silinfo$avg.width  
}
plot(1:13, sil_width,
     xlab = "Number of clusters",
     ylab = "Silhouette Width")
lines(1:13, sil_width)

#클러스터링
pam_fit <- pam(dis, diss = TRUE, 2)
pam_results <- k[1:1000,] %>%
  mutate(cluster = pam_fit$clustering) %>%
  group_by(cluster) %>%
  do(the_summary = summary(.))
pam_results$the_summary

library(Rtsne)
tsne_obj <- Rtsne(dis, is_distance = TRUE)
tsne_data <- tsne_obj$Y %>%
  data.frame() %>%
  setNames(c("X", "Y")) %>%
  mutate(cluster = factor(pam_fit$clustering))
ggplot(aes(x = X, y = Y), data = tsne_data) +
  geom_point(aes(color = cluster))

setwd('C:/Users/bounc/Desktop/백신 주제')
a=read.csv('final_train.csv')
b=read.csv('Hotdeck_data.csv')
c=fread('NAfactor_train2.csv')

c = c %>% mutate_if(is.integer,as.factor)
str(c)

levels(c$respondent_id) =c(26707:53414)

levels(cc$h1n1_concern) = c(0:5)
levels(cc$h1n1_knowledge) = c(0:4)

levels(a$opinion_h1n1_risk) = c(1:6)
levels(cc$opinion_h1n1_vacc_effective) = c(1:6)
levels(cc$opinion_h1n1_sick_from_vacc)= c(1:6)
levels(cc$opinion_seas_vacc_effective)= c(1:6)
levels(cc$opinion_seas_risk)= c(1:6)
levels(cc$opinion_seas_sick_from_vacc)= c(1:6)



levels(c$behavioral_antiviral_meds) = c(0:2)
levels(c$behavioral_avoidance) = c(0:2)
levels(c$behavioral_face_mask) = c(0:2)
levels(c$behavioral_wash_hands) = c(0:2)
levels(c$behavioral_large_gatherings) = c(0:2)
levels(c$behavioral_outside_home) = c(0:2)
levels(c$behavioral_touch_face) = c(0:2)

levels(c$doctor_recc_h1n1) = c(0:2)
levels(c$doctor_recc_seasonal) = c(0:2)
levels(c$chronic_med_condition) = c(0:2)
levels(c$child_under_6_months) = c(0:2)
levels(c$health_worker) = c(0:2)
levels(c$health_insurance) = c(0:2)

levels(c$race) = c(0:3)
levels(c$sex) = c(0,1)
levels(c$income_poverty) = c(0:3)
levels(c$marital_status) = c(0,1,2)
levels(c$rent_or_own) = c(0,1,2)
levels(c$employment_status) = c(0:3)
levels(c$hhs_geo_region) = c(0:9)
levels(c$employment_industry) = c(0:21)
levels(c$employment_occupation) = c(0:23)
levels(c$education)= c(0:4)
levels(c$census_msa)= c(0:2)

levels(c$household_adults)= c(0:2)
levels(c$household_children)= c(0:2)

levels(c$h1n1_vaccine) = c(0:1)
levels(c$seasonal_vaccine) = c(0:1)

str(cc)
write.csv(c,'NAfactor_train2.csv')

#mice test 변경
aa=fread('mice_imputed_test.csv')
napro = function(x){
  ifelse(is.na(x) | x=="","na",x)
  
}
aa= aa %>% lapply(napro) %>% as.data.frame() %>% mutate_if(is.character,as.factor)
levels(aa$race) = c(1:4)
levels(aa$sex) = c(0,1)
levels(aa$marital_status) = c(0,1)
levels(aa$hhs_geo_region) = c(1:10)
levels(aa$employment_industry) = c(1:22)
levels(aa$employment_occupation) = c(1:24)
levels(aa$census_msa)= c(1:3)
write.csv(aa,'a2.csv')

#knn test 변경
c=fread('knn_test.csv')
c$respondent_id = c(26707:53414)
c = c %>% mutate_if(is.character,as.factor)
c = c %>% mutate_if(is.numeric,as.factor)
c = c %>% select(-V1)
str(c)
write.csv(c,'knn_test.csv')

#knn train 변경
c=fread('knn_train.csv')
write.csv(c,'knn_train.csv')


importance = c(1.49756645e-04,  3.93111194e-03,  8.23661550e-04,  5.61587420e-04,
-5.24148259e-04, -7.48783227e-04,  3.36952452e-04,  2.99513291e-04,
1.42268813e-03,  5.04679895e-02,  5.00187196e-02,  2.54586297e-03,
-4.11830775e-04,  5.09172595e-03,  3.86746537e-02,  1.56121303e-02,
1.45638338e-02,  4.26806440e-03,  4.65368776e-02,  5.75439910e-02,
1.45263946e-02,  3.30213403e-02,  5.65331337e-03,  8.98539873e-04,
1.23549232e-03, -2.62074130e-04, -1.87195807e-04,  1.87195807e-03,
6.36465743e-04,  7.86222389e-04, -3.74391614e-05,  6.73904905e-04,
1.46012729e-03,  3.66903781e-03,  1.79707975e-03)

index=c('h1n1_concern', 'h1n1_knowledge',
        'behavioral_antiviral_meds', 'behavioral_avoidance',
        'behavioral_face_mask', 'behavioral_wash_hands',
        'behavioral_large_gatherings', 'behavioral_outside_home',
        'behavioral_touch_face', 'doctor_recc_h1n1', 'doctor_recc_seasonal',
        'chronic_med_condition', 'child_under_6_months', 'health_worker',
        'health_insurance', 'opinion_h1n1_vacc_effective', 'opinion_h1n1_risk',
        'opinion_h1n1_sick_from_vacc', 'opinion_seas_vacc_effective',
        'opinion_seas_risk', 'opinion_seas_sick_from_vacc', 'age_group',
        'education', 'race', 'sex', 'income_poverty', 'marital_status',
        'rent_or_own', 'employment_status', 'hhs_geo_region', 'census_msa',
        'household_adults', 'household_children', 'employment_industry',
        'employment_occupation')
a=data.frame(index,importance)

b %>% ggplot(aes(x=reorder(index,importance),y=importance)) + geom_bar(stat='identity',fill='#86D1C7') + coord_flip() +theme_bw() 

kk = expand.grid(dataset= c('Hotdeck', 'MICE','NAfactor'), method=c('Chain classifier','Label Powerset'), hamloss=NA,accuracy=NA)
kk['hamloss']=c(0.19384,0.18560,0.18064,0.19627,0.19047,0.18017)
kk['accuracy']=c(0.68326,0.69225,0.70254,0.68232,0.69000,0.70310)
par(mfrow=c(1,2))
kk %>% ggplot(aes(x=dataset,y=hamloss)) + geom_bar(stat='identity',fill='#6397D6') +facet_wrap(~method) + geom_text(aes(label=hamloss),vjust=-0.4) + theme_classic()
kk %>% ggplot(aes(x=dataset,y=accuracy)) + geom_bar(stat='identity',fill='#E892C4') + facet_wrap(~method) + geom_text(aes(label=accuracy),vjust=-0.4)+ theme_classic()


data=read.table('C:/Users/bounc/Desktop/water-quality.txt',sep = ',',header = T)
data
write.csv(data,'a.csv')



##동질성 검정
dat=fread('C:/Users/bounc/Desktop/백신 주제/nafactor_train.csv') %>% mutate_all(as.factor)
dat
dat2=fread('C:/Users/bounc/Desktop/백신 주제/smote_nafactor_train.csv') %>% mutate_all(as.factor)
dat2 
sum(dat$seasonal_vaccine == 1)
sum(dat$seasonal_vaccine == 0)
sum(dat2$seasonal_vaccine == 1)
sum(dat2$seasonal_vaccine == 0)
a=matrix(c(sum(dat$seasonal_vaccine == 1),
         sum(dat$seasonal_vaccine == 0),
         sum(dat2$seasonal_vaccine == 1),
         sum(dat2$seasonal_vaccine == 0)),2,2,byrow = T)

dimnames(a) <- list("type" = c("X", "O"),  "vaccine" = c("1", "0"))
chisq.test(a)
