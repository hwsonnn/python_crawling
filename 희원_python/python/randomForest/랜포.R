A <- iris
str(A)

# install.packages("party")
library(party)

# cforest

set.seed(2014)
# mtry=2 (하나의 트리에 2개의 변수를 선택해 트리를 구성)
# ntree = 100 (이런 트리를 100개 만들도록 한다)
# controls (cforest에서는 기본적으로 mtry, ntree가 주어져있는데, 이러한 조건을 변경하기 위해 필요한 인자?)
cf <- cforest(formula = Species~., data = A, controls = cforest_unbiased(mtry = 2, ntree = 100))
cf

# 랜포를 사용하는 경우는 주로 Variable Importance를 추출하기 위한 경우가 많다.
# 랜포 함수들은 반응변수(ex)Species)를 분류할 때 가장 영향을 끼치는 변수가 무엇인지 판단할 수 있는 수치를 제공한다.

cf_varimp <- varimp(cf)
cf_varimp

# 결과적으로 Species를 분류할 때 가장 중요한 역할을 하는 변수는
# Petal.Length > Petal.Width > Sepal.Length > Sepal.Width 순이라는 의미이다.

# install.packages("randomForest")
library(randomForest)

set.seed(2014)
rf <- randomForest(formula = Species ~., data = A, mtry = 2, ntree = 100, corr.bias = T)
rf

rf_varimp = importance(rf, type = 2)
rf_varimp
varImpPlot(rf)

# 결과적으로 해석하자면 Species를 분류할 때 가장 중요한 역할을 하는 변수는
# Petal.Width > Petal.Length > Sepal.Length > Sepal.Width 순이라는 의미이다.

# 수치는 다르지만, 결과는 유사하다. 하지만 우리가 randomForest를 더 많이 사용한는 이유는 처리시간에서 랜포가 훨씬 유리하기 때문이다.


## 랜덤 포레스트에 대한 이론적 설명
# 일반적으로 랜포는 배깅보다 더 좋은 성능을 보여주기 때문에 가장 자주 쓰이는 방법이다.
# 이는 랜포에서 생성하는 나무는 배깅과는 다르게 상관성을 제거하기 때문이다.
# 랜포의 경우 의사결정나무들을 만들 때, 나무 내에서 분할이 고려될 때마다 p개의 설명번수들의 전체집합에서
# m개의 설명번수들로 구성된 랜덤표본이 분할 후보로 선택된다. 분할은 이들 m개 설명변수들 중 하나만을 사용한다.
# 각 분할에서 m개 설명변수들의 새로운 표본이 선택되며, 보통 p(독립변수의 개수)의 제곱근의 수만큼 선택된다.
# 해당 개수를 조절하기 위해서는 mtry인자로 조정한다.

# ntree : 몇 개의 나무를 생성할지를 설정하는 인자
# mtry : 각 노드에서 랜덤하게 고려될 변수의 개수를 지정
# nodesize : 나무의 깊이를 설정하는 인자로,, 최소한의 노드의 개수를 뜻한다. 여기서 최소한의 노드란,
# 		 각 노드에서 가져야 할 값들의 최솟값이다. 때문에 해당 인자의 값이 작다면, 깊이가 깊은 나무가 생성되고
#		 값이 크다면 깊이가 얕은 나무가 생성된다.


setwd("C:/Users/jsdata/Desktop/python/randomForest")
data <- read.csv("german_credit.csv", header = T)
str(data)
summary(data)

# 변수 위치를 이용하여 데이터 타입을 factor형으로 변경하기
F <- c(1,2,4,5,7,8,9,10,11,11,12,13,15,16,17,18,19,20,21)
for(i in F) data[,i] = as.factor(data[,i])
str(data)

# 데이터 분리를 위한 패키지 불러오기(train:test = 7:3)
# install.packages("caret")
library(caret)

set.seed(2014)
intrain = createDataPartition(y=data$Creditability, p = 0.7, list = FALSE)
# caret::createDataPartition : 데이터를 훈련 데이터와 테스트 데이터로 분할한다.
# y : 분류(또는 레이블)
# times = 1 : 생성할 분할의 수
# p = 0.5 : 훈련 데이터에서 사용할 데이터의 비율
# list = F : 결과를 리스트로 반환할지 여부, FALSE면 행렬을 반환
# 반환 값은 훈련 데이터로 사용할 데이터의 색인이다.
train <- data[intrain,]
test <- data[-intrain,]

library("randomForest")

# 랜덤포레스트에서 중요한 인자는 3가지이다 : ntree, mtry, nodesize.
set.seed(2014)
rf <- randomForest(Creditability~., data=train, mtry=5, ntree=100)

#test 데이터 셋을 이용해 모델 정확도 평가
rf_predict = predict(rf, test, type="class")
confusionMatrix(rf_predict, test$Creditability)

install.packages("e1071")
library(e1071)











### Boosting
# Boosting은 초기 샘플 데이터를 조작하여 다수의 분류기를 생성하는 기법 중 하나이고 순차적 방법이다.
# Boosting은 이전 분류기의 학습 결과를 토대로 다음 분류기의 학습 데이터의 샘플가중치를 조정해 학습을 진행하는 방법이다.
# 즉, 이전 결과에 영향을 받는다는 것이다.
# 먼저 training data와 testing data를 적당한 비율로 random하게 추출하여 분할한다.
# 그 다음 training set에서 bagging에서와 같이 bootstrap sampling 기법을 이용해 sample을 추출하고
# 특정한 학습 알고리즘에 적용하여 분류기를 생성한다.
# 이렇게 생성된 분류기의 분류결과를 통해 잘못 분류한 데이터와 추출되지 않은(학습에 이용되지 않은)데이터에는 가중치를 부여하여
# 다음 학습에 이용한다.
# 이러한 일련의 과정을 부스팅라운드(Boosting round)라고 하는데, 이렇게 총 T번의 부스팅 라운드를 거쳐서 완성된
# 모형들을 이용해 최종 분류모형이 만들어지게 된다.
# 검증의 경우 사전에 독립적으로 추출해 두었던 testing data를 이용하여 모형의 성능을 평가한다.
# 이때 주의할 점은 마지막에 학습한 분류기만을 의사결정에 이용하는 것이 아니라, 학습에 이용되었던 모든 분류기들의 앙상블을 통해
# testing data의 집단을 결정하는 것이다.

## 부스팅의 간단한 공식
# 모델 M이 있다고 가정, 이 모델 M은 80%의 정확도를 가지고 있고, 정확도를 높이고 싶다
# 1. 변수와 상관관계가 있는 weight를 추가해줄 수 있다.
# Y = M(x) + weight
# 2. 여기서 weight는 다음과 같이 또 다른 weight를 줌으로써 정확도를 높일 수 있다.
# weight = G(x) + weight2
# 3. 정확한 정확도를 위해 weight에 또다른 weight를 줄 수 있다.
# weight2 = H(x) + weight3
# 그러면 우리는 Y = M(x) + G(x) + H(x) + weight3의 식을 얻을 수 있다.
# 이제 이 모델은 초기 80%의 정확도보다 더 높은 정확도를 가질 것이다.
# 여기서 부스팅이 수행하는 일은 바로, 각각의 M(x), G(x), H(x)에 대해 가중치를 조정하는 것이다.
# 바로 이 가중치를 적절하게 가져감으로써 정확도를 높일 수 있다.
# Y = alpha * M(x) + beta * G(x) + gamma * H(x) + weight4


## Gradient Boosting을 다루기 위한 3가지 중요한 인자
# n.trees : 생성할 나무의 개수
# interaction.depth : 각 노드에서 뻗어나갈 가지의 개수를 지정해줌으로써 나무의 깊이를 조절한다.
# 			    이 값을 N으로 지정한다면, 총 노드의 개수는 3*N+1개, 
#			    총 terminal 노드의 개수는 2*N+1개. 즉, 이 값이 클수록 더 깊은 나무가 생성된다.
# shrinkage : Learing Rate로써, gradient boosting을 학습하는데 걸리는 시간을 조절한다.
#		  만약 이 값이 크다면 그만큼 빨리 학습을 수행하게 되지만, 수행도중 중요한 점을 놓칠 수 있다.
#		  때문에 이 값이 크다면 n.trees인자로 나무를 많이 생성해야 함으로써 보완해야 한다.
#		  반대로 이 값이 작다면 학습시간이 오래 걸리고 그만큼 완벽한 부스팅을 수행한다.
#		  이때는 n.trees 인자에 적은 개수를 지정하면 된다.
#		  만약 shrinkage가 작은 값인데도 n.trees에 큰 값을 주면 수행 시간이 매우 오래 걸리며 과적합이 발생할 수 있다.

# 실습

df = read.csv("german_credit.csv", header = T)
str(df)
# gbm에서는 타겟변수를 연속형으로 설정한다. 단 함수 수행 때 자동으로 factor 데이터 타입으로 인식한다.
F <- c(2,4,5,7,8,9,10,11,11,12,13,15,16,17,18,19,20,21)
for(i in F) df[,i] = as.factor(df[,i])
str(df)

set.seed(2014)
intrain = createDataPartition(y = df$Creditability, p=0.7, list = FALSE)
train = df[intrain,]
test = df[-intrain,]

# install.packages("gbm")
library(gbm)

# gradient boosting 수행
# distribution 인자에 bernoulli는 분류분석ㅇ을 수행하기 위해 입력(타겟변수를 factor로 인식해주기 위함)
# n.trees는 100개의 나무를 생성, verbose는 생성과정 출력
# interaction.depth는 트리의 깊이를 간접적으로 조정(클수록 깊은 나무)
# shrinkage는 learning rate로써, 학습률을 말함

A <- gbm(Creditability~., distribution = "bernoulli", n.trees=100, verbose=TRUE,
	interaction.depth = 5, shrinkage = 0.001, data = train)

# A를 입력해 결과를 확인해보면 나무가 생성되도 Improve(모델 정확도 향상도)가 매우 적음을 알 수 있다.
# 즉, 해당 데이터는 부스팅을 수행해도 정확도가 크게 높아지지 않음을 알 수 있다.
# 이는 주로 모수 부족 및 하나의 나무를 생성하는 것만으로도 충분히 정확도 있는 나무가 생성될 정도로 깔끔한 데이터인 경우디ㅏ.

# 몇 개의 나무를 생성하는게 가장 적절한지 파악
gbm.perf(A)
# 100개를 생성하는게 적절하다고 추측할 수 있다.

# 변수별 상대 중요도 출력
a <- summary(A)
a

# 모델 정확도 검정
boost.probs <- predict(A, newdata=test, n.trees=100, type="response")
# 0.5를 초과하는 확률은 우량으로 취급하고 GOOD으로 변경
# 반대로 0.5이하는 불량으로 취급하고 BAD로 변경
gbm.pred <- rep("BAD", 300)
gbm.pred[boost.probs>.5] <- "GOOD"
gbm.pred[boost.probs<=.5] <- "BAD"

# 예측결과 확인
# 데이터 모수 부족 등의 이유로 랜덤포레스트와는 다르게 부스팅이 수행되도 정확도가 높아지지 않았을 뿐만 아니라
# 부스팅 결과확인 시 나무가 생성될수록 에러율 역시 감소하는 폭이 매우 작음을 알 수 있다.

table(gbm.pred, test$Creditability)
214/300







### 의사결정나무(Decision Tree)

# 의사결정나무는 한번에 하나씩의 설명변수를 사용하여 예측 가능한 규칙들의 집합을 생성하는 알고리즘이다.
# 한번 분기 때마다 변수 영역을 두개로 구분해 구분 뒤 각 영역의 순도가 증가/불확실성이 감소하도록 하는 방향으로 학습을 진행한다.
# 의사결정나무는 입력 변수 영역을 두 개로 구분하는 재귀적 분기와 너무 자세하게 구분된 영역을 통합하는 가지치기 두가지 과정으로 나뉜다.

# install.packages("rpart")
library(rpart)

# Fit1 <- rpart(반응변수, data, type="anova")
# 이런 형태로 만들 수 있다.

## 정확도 : 의사결정나무 < 로테이션포레스트 < 랜덤포레스트

# tree()함수
# binary recursive partitioning방법을 사용. 불순도의 측도로 엔트로피 지수를 사용하며 엔트로피는 주어진 데이터 집합의 혼잡도를 의미
# 즉, 주어진 데이터 집합에 레코드들에 서로 다른 클래스들이 많이 섞여있으면 엔트로피가 높고,
# 같은 클래스의 레코드들이 많이 있으면 엔트로피가 낮다.
# 엔트로피는 0~1 사이의 값을 가지며, 1에 가까울수록 혼잡도가 높다.
# 즉, tree()함수는 엔트로피가 높은 상태에서 낮은 상태가 되도록 나무 모양을 생성한다.

# rpart()함수
# CART방법을 사용, 이는 전체 데이터셋을 갖고 시작해, 반복해서 두 개의 자식 노드를 생성하기 위해 모든 예측 변수를 사용하여
# 데이터 셋의 부분집합을 쪼갬으로써 의사결정나무를 생성한다.
# CART는 Gini index가 작아지는 방향으로 움직이며, Gini index를 가장 많이 감소시켜 주는 변수가 영향을 가장 많이 끼치는 변수이다.

# ctree()함수
# Unbiased recursive partitioning based on permutation test 방법을 사용
# p-test를 거친 significance를 기준으로 가지치기를 할 변수를 결정하기 때문에 biased 될 위험이 없어
# 별도의 가지치기 할 필요가 없지만 입력 변수의 레벨이 31개까지로 제한되어있다.
# rpart()함수의 두 가지 문제점을 해결해준다.
## 1. 통계적 유의성에 대한 판단 없이 노드를 분할하는데 따른 과적합(Overfitting)
## 2. 다양한 값으로 분할 가능한 변수가 다른 변수에 비해 선호되는 문제



# party 패키지를 사용한 의사결정나무 분석 (ctree()함수 사용법)
# ctree(a, b)
# a : 타겟변수, b : 의사결정나무를 수행하게 될 데이터가 저장된 객체
german <- read.csv("german_credit.csv", header = TRUE)
str(german)

#factor 형태 데이터의 클래스 변경
F <- c(1,2,4,5,7,8,9,10,11,12,13,15,16,17,18,19,20,21)
for(i in F) german[,i] = as.factor(german[,i])
str(german)

#데이터 분리를 위한 패키지 불러오기)
library(caret)

# 데이터 분리
set.seed(2014)
intrain <- createDataPartition(y = german$Creditability, p=.7, list=FALSE)
train <- german[intrain,]
test <- german[-intrain,]

# ctree() 함수 수행을 위한 패키지 불러오기
# install.packages("party")
library(party)

# rpart를 위한 의사 결정 나무의 형성(깊이 설정)
A <- ctree_control(maxdepth = 20)
B <- ctree(Creditability~., data=train, control=A)
plot(B, compress=TRUE)

# 예측하기 & 모델 평가
library(e1071)
treepred <- predict(B, test)
confusionMatrix(treepred, test$Creditability)
(16+188)/(16+188+22+74)
# 약 68%로 정확도를 가짐을 알 수 있다.




## tree 패키지를 사용한 의사결정나무 분석
german <- read.csv("german_credit.csv", header = TRUE)
str(german)
F <- c(1,2,4,5,7,8,9,10,11,12,13,15,16,17,18,19,20,21)
for(i in F) german[,i] = as.factor(german[,i])
str(german)
library(caret)
set.seed(2014)
intrain <- createDataPartition(y = german$Creditability, p=.7, list=FALSE)
train <- german[intrain,]
test <- german[-intrain,]
# install.packages("tree")
library(tree)
treemod <- tree(Creditability~., data=train)
plot(treemod)
text(treemod)
# ctree()함수를 제외하고는 가지치기가 필요하다. why? : 과적합의 문제를 해결하기 위해서다.
# 가지치기(PRUNING)
cv.trees <- cv.tree(treemod, FUN=prune.misclass) #for classification decision tree
plot(cv.trees)
# 내가 생각하기에는 14개의 가지에서 분산이 제일 낮은 것으로 보인다.
prune.trees <- prune.misclass(treemod, best=7) # for regression decision tree, use prune tree function
plot(prune.trees)
text(prune.trees, pretty=0)
treepred <- predict(prune.trees, test, type = 'class')
confusionMatrix(treepred, test$Creditability)
(38+181)/(38+181+29+52)
# 약 73%의 정확도를 가짐을 알 수 있다.



## rpart 패키지를 사용한 의사결정나무 분석
# install.packages("rpart")
library(rpart)
rpartmod <- rpart(Creditability~., data=train, method="class")
plot(rpartmod)
text(rpartmod)
printcp(rpartmod)
plotcp(rpartmod)
# 4개의 split에서 가장 낮은 error를 보인다.
ptree <- prune(rpartmod, cp=rpartmod$cptable[which.min(rpartmod$cptable[,"xerror"]),"CP"])
plot(ptree)
text(ptree)
rpartpred <- predict(ptree, test, type='class')
confusionMatrix(rpartpred, test$Creditability)
(15+192)/(15+192+18+75)
# 약 69%의 정확도를 가짐을 알 수 있다.
# 이 데이터셋에 대해서는 tree패키지를 사용했을 때 예측 정확성이 가장 높았음을 알 수 있다.










### 로테이션포레스트(rotation forest)
# 로테이션포레스트는 학습데이터에 주성분분석(PCA)를 적용해 데이터 축을 회정(rotation)한 후  학습한다는 점을 제외하고는
# 랜덤포레스트와 같다. PCA로 회전한 축은 학습데이터의 분산을 최대한 보존하면서도 학습성능 향상에도 유의미할 것이라는 전제에서
# 고안된 방법으로 풀이된다.
# install.packages("rotationForest")
library(rotationForest)
# Fit <- rotationForest(x, y, K, L)
# 입력변수(x)와 예측변수(y)를 나눠서 넣어주어야 하며 2범주 분류만 수행할 수 있다.
# PCA를 수행해야 하기 때문에 x의 자료형은 반드시 숫자여야 하며 y 역시 0 또는 1로 바꿔주어야 한다.
# K와 L은 각각 randomForest 패키지의 mtry, ntree와 같다.










## 실습
# install.packages("tidyverse")
# install.packages("caret")
# install.packages("mlbench")
library(tidyverse)
library(caret)
library(mlbench)

set.seed(1234)
data(Sonar, package = "mlbench")
Sonar <- Sonar %>% tbl_df
Sonar
## tbl_df는 데이터프레임을 나타내는 하나의 형태로 데이터프레임을 현대적으로 업그레이드한 형태라고 생각하면 된다.
## mlbench : 데이터셋이 저장된 패키지
## :: 이 연산자는 빈칸이 필요 없다.

# createDataPartition() 함수를 사용해 train과 test set을 만든다.
indexTrain <- createDataPartition(Sonar$Class, p = .7, list=FALSE)
training <- Sonar[indexTrain,]
testing <- Sonar[-indexTrain,]
training #146개
testing #62개

# 머신러닝 알고리즘별 최적의 모수를 찾기 위한 학습방법 사전 설정
# KNN(K 최근접 이웃모델)을 통해 명목변수를 예측하려 한다면 먼저 "K"를 몇개로 설정할 건지 정해야한다.
# 또한 랜포에서 mtry를 얼마로 정해야 할지도 마찬가지이다.
# 이 모수들은 caret package에서 "Tuning parameters"로 설명하고 있고
# LOOCV, K-fold cross validation 등과 같은 방법을 통해서 데이터에 근거한 최적의 parameter를 찾는 과정을 거친다.
# 예를 들어서, KNN은 K 하나인 단모수이므로 3^1=3인 3가지 K값들을 후보로 두고 모델을 비교하게 된다.
# RRLDA의 경우 모수의 개수가 lambda, hp, penalty 총 3개인데 3^3=27인 27가지 후보를 비교하게 된다.
# 후보의 비교방법을 K-fold cross validation으로 한다고 할 경우 몇번을 접어 cross validation을 할 것이냐 란 질문의 K를 정해야 한다.
# caret패키지에서는 trainControl() 함수를 통해 일관된 비교방법을 각 후보에게 통일되게 적용하여 평가 가능

#10-fold cross validation을 5번 반복하여 가장 좋은 후보의 파라미터 그리드를 찾게 해주는 일종의 장치
fitControl <- trainControl(method = "repeatedcv",, number = 10, repeats = 5)

## RandomForest로 학습시켜보기
# 학습을 위한 표준화된 인터페이스는 바로 train()함수이다.
# 이 함수에서 method() 인자만 바꿔주면 원하는 학습모델 알고리즘을 구현할 수 있게 된다.
# 랜덤포레스트 알고리즘을 통해 학습할 것을 'method="rf"' 를 통해 선언한다.
# 랜덤포레스트에서 Tuning parameter에 해당되는 "mtry"는 10-fold cross validation을 5번 반복하여 가장 좋게 평가된 것을
# 선택하는 후보채택방법인 'fitControl'객체를 'trControl'인자에 입력한다
# 'verbose'인자는 기본적으로 TRUE로 설정되어 있는데 mtry 선정과정이 적나라하게 모두 출력되서 이 출력을 막고싶으면 FALSE로 지정

set.seed(1234)
rf_fit <- train(Class ~., data = training, method="rf", trControl=fitControl, verbose = FALSE)
rf_fit

# 자동으로 3^p 공식에 의해 정해진 mtry후보는 2, 31, 60개로 자동설정된 것을 볼 수 있고, 
# 이 중 Kappa 통계량과 정확도에 의해서 mtry=2가 최종적으로 선정됨

## 테스트셋에 적용하여 정확도 확인
predict(rf_fit, newdata = testing)

# confusionMatrix()를 통해 정확도외 다양한 통계량을 얻을 수 있다.
predict(rf_fit, newdata = testing) %>% confusionMatrix(testing$Class)
12/(12+32+18)
# 총 62개의 테스트 데이터 셋 중 12개가 오분류 되어 약 80%의 정확도를 가진 것으로 볼 수 있다.

## Tuning parameters의 그리드 조정하기
## 사용자 검색 그리드(custom search grid)
# 최적 파라미터 선정 시 탐색범위와 그리드를 수동으로 조절할 수 있다.
# 이번에는 mtry의 후보를 1~10로 바꾸어 설정하고 이 중에서 채택해보자

set.seed(1234)
customGrid <- expand.grid(mtry = 1:10)
rf_fit2 <- train(Class~., data=training, method = "rf", trControl=fitControl,	tuneGrid = customGrid, verbose = F)
rf_fit2


## 랜덤 검색 그리드
# 튜닝 파라미터의 개수가 많으면 많아질수록 탐색그리드의 개수는 지속적으로 증가하게 되고 동일한 간격의 그리드 구성으로 인해
# 탐색과정이 비효율적이 될 수 있다.
# 지금까지 튜닝 파라미터가 한개인 랜덤포레스트를 예시로 했는데 이번에는 튜닝 파라미터가 2개인 RDA를 통해 훈련을 해보자
# method = "rda"를 통해 선언 가능
rda_fit <- train(Class~., data = training, method = "rda", trControl = fitControl, verbose = F)
rda_fit
# 총 9개의 파라미터 조합을 비교하는 것을 볼 수 있다.
# expand.grid()함수를 이용하면 동일간격 그리드를 검색하게 될 것이다.
# trainControl()함수의 search = "random"을 통해 검색타입을 랜덤으로 바꾼다.
fitControl <- trainControl(method="repeatedcv", number = 10, repeats = 5, search = "random")
fitControl
rda_fit2 <- train(Class~., data=training, method = "rda", trControl=fitControl, verbose = F)
rda_fit2
# 튜닝파라미터가 gamma, lambda 2개인데 검색타입을 랜덤으로 바꾸는 순간 3^p공식으로 후보군을 설정하지 않는 것을 확인할 수 있다.
# 수동으로 튜닝파라미터 조합개수를 늘려보는데 이때는 train()함수의 tuneLength 인자를 이용
rda_fit2 <- train(Class~., data=training, method="rda", trControl=fitControl, tuneLength=50,verbose=F)
rda_fit2
# 이처럼 튜닝파라미터를 랜덤하게 50개로 설정하여 조금 더 융통성 있는 최적의 파라미터 튜닝 방법을 고려해볼 수 있다.




# https://m.blog.naver.com/tjdudwo93/221051481147
# svm

# https://m.blog.naver.com/tjdudwo93/221071886633
# xgboost

# https://m.blog.naver.com/tjdudwo93/221041154927
# gbm

# https://rpubs.com/chidungkt/300153
# randomForest





















