
# ---------------------- <분할표> ----------------------
### 싹쓰리 예시로 분할표 실습을 해보자!

## 1.분할표 직접 만들어보기
#2차원 분할표(2X3) 생성
SSak_Three <- matrix(c(78, 49, 15, 23, 46, 37), nrow=2) 
dimnames(SSak_Three) <- list(성별 = c("남", "여"), 최애 = c("유두래곤", "비룡","린다.G")) 
SSak_Three

#비율에 대한 분할표
prop.table(SSak_Three) # 비율에 대한 분할표를 prop.table()으로 쉽게 만들 수 있다.

#주변합까지 표시한 분할표
addmargins(SSak_Three) #도수
addmargins(prop.table(SSak_Three)) #비율

#분할표 시각화 (모자이크 플랏)
mosaicplot(SSak_Three, color = c("pink", "black",'yellow'))  


## 2.원본 데이터를 보고 2차원 분할표 만들기 
#보통 우리가 접하는 데이터는 이렇게 생겼다! 이 데이터를 갖고 분할표를 만들어보자

#원본 데이터
raw_2D <- data.frame(성별 = c(rep("남", 78), rep("여", 49),rep("남", 15), rep("여", 23),rep("남", 46), rep("여", 37)), 
                       최애 = c(rep("유두래곤",127), rep("비룡",38),rep("린다.G",83)))
raw_2D

#2차원 분할표 만들기
table(raw_2D$성별,raw_2D$최애) #table(변수1, 변수2) 함수로 2차원 분할표를 만들 수 있다.

#비율에 대한 분할표 만들기
prop.table(raw_2D$성별, raw_2D$최애) #prop.table()은 분할표만 받기 때문에 오류가 난다.

table_2D = table(raw_2D$성별,raw_2D$최애)
prop.table(table_2D) #이런 식으로 분할표를 함수에 넣어줘야 한다.

#주변합까지 표시한 분할표
addmargins(table_2D)

## 3.원본 데이터를 보고 3차원 분할표 만들기 
# 범주 대대로 내려오는 연애 예시로 실습해보자!

#원본 데이터 
raw_3D <- data.frame(성별 = c(rep("남", 75), rep("여", 88)), 
                       연애 = c(rep("O", 41), rep("X", 34), rep("O", 39),rep("X", 49)), 
                       학과 = c(rep("통계", 11), rep("경영", 16), rep("경제", 14),rep("통계", 25), rep("경영", 4), rep("경제", 5),
                                rep("통계", 10), rep("경영", 22), rep("경제", 7), rep("통계", 27), rep("경영", 10), rep("경제", 12)))
raw_3D

#3차원 분할표 만들기(1)
table(raw_3D$성별, raw_3D$연애, raw_3D$학과)

table_3D = table(raw_3D$성별, raw_3D$연애, raw_3D$학과)
prop.table(table_3D) #비율에 대한 분할표

#주변합 표시한 분할표
addmargins(table_3D)

#분할표 시각화
mosaicplot(table_3D, color = c("pink", "black",'yellow'))

#3차원 분할표 만들기(2)
ftable(raw_3D$성별, raw_3D$연애, raw_3D$학과) # 3차원 분할표의 경우는 ftable()이 깔끔!

ftable_3D=ftable(raw_3D$성별, raw_3D$연애, raw_3D$학과)
prop.table(ftable_3D) #비율에 대한 분할표

#주변합 표시한 분할표
addmargins(ftable_3D)

#분할표 시각화
mosaicplot(ftable_3D, color = c("pink", "black",'yellow'))



# ---------------------- <독립성 검정> ----------------------

## 1. 명목형 변수 독립성 검정
#피어슨 카이제곱 검정 
chisq.test(table_2D) #p-value가 0.056! 

#가능도비 검정
library(DescTools) #가능도비 검정 함수 GTest()가 있는 패키지
GTest(table_2D) #p-value가 0.057!

#피어슨 카이제곱 / 가능도비를 한꺼번에~!
library(vcd) #두 검정을 한꺼번에 해주는 함수 assocstats()가 있는 패키지 
assocstats(table_2D)


## 2. 순서형 변수 독립성 검정
library(vcdExtra) #순서형 독립성 검정을 위한 패키지

#순서형 정보가 있는 데이터 불러오기
JobSat #vcdExtra 패키지 안에 있는 데이터셋

# MH 검정 
CMHtest(JobSat, types = 'cor') #p-value가 0.08! / CMHtest() 함수는 vcdExtra 패키지 안에 있음 
MHChisqTest(JobSat) # p-value가 동일! / MHchisqTest() 함수는 DescTools 패키지 안에 있음

chisq.test(JobSat) #순서형 정보를 무시하고 명목형 검정을 했더니 왜곡된 p-value 값이 나온다!



# ---------------------- <연관성 측도> ----------------------

##이번엔 연애 예시로 실습을 해보자!
love <- matrix(c(509, 398, 116, 104), nrow=2) 
dimnames(love) <- list(성별 = c("여", "남"), 애인 = c("O","X")) 
love

## 1.직접 구하는방법
addmargins(love)
n = apply(love,1,sum) #행별 합계
n 

love_con = sweep(love,1,n,'/') # sweep() 함수는 행렬에 함수와 통계량을 적용하는 함수이다! /  행별로 행별합(n)으로 나누어줘서  조건부 확률을 계산한다.
addmargins(love_con,2) #행별 조건부 확률 / addmargins()에 1하면 열의 주변합, 2하면 행의 주변합 계산해준다.

#비율의 차이
love_con[1,1] - love_con[2,1] #비율의 차이 계산

#상대위험도
love_con[1,1] / love_con[2,1] #상대위험도 계산 / 1.027

#오즈비
love_con[1,1] / love_con[1,2] #여성이 애인이 있을 오즈
love_con[2,1] / love_con[2,2] #남성이 애인이 있을 오즈
(love_con[1,1] / love_con[1,2]) / (love_con[2,1] / love_con[2,2]) #오즈비 / 1.146

## 2.자동으로 한꺼번에 구하는 방법
library(epiR) # 2x2분할표의 상대위험도와 오즈비를 구해주는 함수가 들어있다.
epi.2by2(love)
