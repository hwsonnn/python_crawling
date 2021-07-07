# https://www.kaggle.com/erikbruin/titanic-2nd-degree-families-and-majority-voting

# 3 Loading and Exploring Data

## 3.1 Loading libraries required and reading the data into R

#install.packages("Hmisc")
#install.packages("knitr")
#install.packages("ggplot2")
#install.packages("dplyr")
#install.packages("caret")
#install.packages("randomForest")
#install.packages("gridExtra")
#install.packages("ROCR")
#install.packages("corrplot")
library(Hmisc)
library(knitr)
library(ggplot2)
library(dplyr)
library(caret)
library(randomForest)
library(gridExtra)
library(ROCR)
library(corrplot)

setwd("C:/Users/jsdata/Desktop/python/randomForest")

# stringsAsFactors = F 를 사용하면 요인형이 아닌 문자형 그대로 사용할 수 있다.
# na.strings=c("NA", "")) 를 사용하면 
train = read.csv("train.csv", stringsAsFactors=F, na.strings=c("NA", ""))
test = read.csv("test.csv", stringsAsFactors=F, na.strings=c("NA", ""))

## 3.2 Data size and structure

str(train)
str(test)
dim(train)
# train set은 12개의 variable과 891개의 observation을 가진다.
# Survived -> 0 = no, 1 = yes
# Pclass -> 1 = 1st, 2 = 2nd, 3 = 3rd
# Embarked -> "S" = Southampton, "C" = Cherbourg, "Q" = Queenstown
# 으로 대충 변수 설명을 할 수 있다.

dim(test)
# test set은 11개의 variable과 418개의 observation을 가진다. train set에서 Survived 변수가 사라진 것을 알 수 있다.
str(test)
# 내가 생각했을 때는 Survived 변수가 반응변수라고 생각한다.

# 데이터 전처리와 EDA를 위하여 train set과 test set을 병합해보자

test$Survived = NA
all = rbind(train, test)
str(all)
dim(all)

## 3.3 Completeness of the data

sapply(all, function(x){sum(is.na(x))})
# Survived 안에 418개의 NA값은 test set에서의 관측치의 총합이다.
# 그리고 Cabin은 1014, Age는 263, Embarked는 2, Fare는 1개의 missing value를 가진다.

## 3.4 Exploring some of the most important variables

## Factor형으로 변환하기
all$Sex = as.factor(all$Sex)
all$Survived = as.factor(all$Survived)
all$Pclass = as.factor(all$Pclass)

str(all)

### 3.4.1 The response variable ; Survived
### EDA
## 반응 변수 Survived에 대한 EDA

ggplot(all[!is.na(all$Survived),], aes(x = Survived, fill = Survived)) + 
	geom_bar(stat='count') +
	labs(x = "How many people died and survived on the Titanic?") +
		geom_label(stat='count', aes(label=..count..), size = 7) + 
		theme_grey(base_size = 18)

# all[!is.na(all$Survived),] -> NA인 값을 제외한 all을 만든다.
# geom_label 을 사용하여 549, 342를 나타내는 상자를 만들어 줬다.
# ..count.. 을 이용하여 빈도수를 나타낸 것이다.
# theme_grey 를 사용하여 배경 테마를 회색으로 변경해주었다.


### 3.4.2 Sex / Gender
summary(all$Sex)
843/(843 + 466)
# female : 466, male : 843으로 남자가 약 64%를 차지한다.
train$Sex = as.factor(train$Sex)
summary(train$Sex)
577/(577 + 314)
# 보면 알 수 있듯이 train set에서도 남자가 약 64%를 차지하여 비슷한 비율을 차지함을 알 수 있다.

# scale_fill_manual 함수를 사용하면 각각의 그래프에 색상을 지정해 줄 수 있다.
# 단 위의 함수는 기존의 색상 위에 다른 색상을 입혀주는 함수이기 때문에 적용 전에 fill or color 함수를 적용한 뒤 사용해야 한다.
p1 = ggplot(all, aes(x = Sex, fill = Sex)) + geom_bar(stat='count', position = 'dodge') +
	theme_grey() + labs(x = 'All data') + geom_label(stat='count', aes(label = ..count..)) +
	scale_fill_manual("legend", values = c("female" = "pink", "male" = "green"))

p2 = ggplot(all[!is.na(all$Survived),], aes(x = Sex, fill = Survived)) + 
	geom_bar(stat='count', position='dodge') + theme_grey() +
	labs(x = 'Training data only') + geom_label(stat='count', aes(label=..count..))

grid.arrange(p1, p2, nrow=1)

233/(233+81)
109/(468+109)
# 위의 그래프를 보면 알 수 있듯이, 남자 중 산 비율 = 약 19% 이고, 여자 중 산 비율 = 약 74% 이다.
# 이렇게 남녀간에 사망 비율이 매우 크게 차이가 나기 때문에 중요한 변수라고 예측할 수 있다.

### 3.4.3 Passenger Class

p3 = ggplot(all, aes(x = Pclass, fill = Pclass)) + geom_bar(stat="count", position='dodge') +
	labs(x = "Pclass, All data") + geom_label(stat='count', aes(label=..count..)) +
	theme(legend.position="none") + theme_grey()
# 'dodge' : 데이터의 종류를 나눠 따로 표시해주는 그래프

p4 = ggplot(all[!is.na(all$Survived),], aes(x = Pclass, fill = Survived)) +
	geom_bar(stat="count", position="dodge") + labs(x = "Training data only") +
	theme(legend.position = "none") + theme_grey()

p5 = ggplot(all[!is.na(all$Survived),], aes(x = Pclass, fill = Survived)) + 
	geom_bar(stat = "count", position = "stack") +
	labs(x = "Training data only", y = "Count") + facet_grid(.~Sex) +
	theme(legend.position="none") + theme_grey()
# 'stack' : 하나의 결과 위에 또 다른 것의 결과를 overlapping 하는것

p6 = ggplot(all[!is.na(all$Survived),], aes(x = Pclass, fill = Survived)) +
	geom_bar(stat = "count", position = "fill") +
	labs(x = "Training data only", y = "Percent") + facet_grid(.~Sex) +
	theme(legend.position='none') + theme_grey()
# 'fill' : 데이터의 종류를 비율로 표시해주는 bar 그래프

grid.arrange(p3, p4, p5, p6, ncol=2)

## 위의 그래프들을 보면 알 수 있듯이, 대부분의 사람들은 3rd class로 여행중이었으며
## 또한 생존률은 승객들의 class와 강하게 연관이 있다.
## 대부분의 1st class의 승객들은 많이 살았으며, 3rd class의 승객들은 대부분 사망하였다.
## 그리고 그래프를 보면 알 수 있듯이, 1st, 2nd의 대부분의 여자 승객들은 살았다. 반대로 2nd, 3rd의 남자들은 대부분이 사망하였다.
## facet_grid 명령어를 사용해서 요인 변수로 쪼개진 데이터에 대해 시각화해서 집합으로 묶어 보일 수 있다.(지금은 성별로 묶었다.)


# 그리고 모델의 'headline'이 실제로는 Pclass와 Sex의 결합이 될 꺼라고 알 수 있기 때문에 합쳐주자
all$PclassSex = c()
all$PclassSex[all$Pclass == '1' & all$Sex == 'male'] = "P1Male"
all$PclassSex[all$Pclass == '2' & all$Sex == 'male'] = "P2Male"
all$PclassSex[all$Pclass == '3' & all$Sex == 'male'] = "P3Male"
all$PclassSex[all$Pclass == '1' & all$Sex == 'female'] = "P1Female"
all$PclassSex[all$Pclass == '2' & all$Sex == 'female'] = "P2Female"
all$PclassSex[all$Pclass == '3' & all$Sex == 'female'] = "P3Female"
all$PclassSex = as.factor(all$PclassSex)
all$PclassSex
str(all)


# 4 Feature engineering

## 4.1 Creating the Title variable
## Name 변수는 NA값을 하나도 가지지 않지만 실제로 단지 성과 이름이 아닌 더 많은 값들을 가진다.
## 이것은 또한 각각의 사람들에게 Title을 가지고 이것은 깔끔한 데이터를 얻기 위해 이름으로부터 분리되어야한다.

# Extracting Title and Surname from Name
all$Surname = c()
all$Surname = sapply(all$Name, function(x) {strsplit(x, split='[,.]')[[1]][1]})
all$Surname
# strsplit(x, "")는 x를 ""안에 든 것을 기준으로 문자열을 나누라는 의미이다.

# correcting some surnames that also include a maiden name
all$Surname = sapply(all$Surname, function(x) {strsplit(x, split='[-]')[[1]][1]})
all$Surname
all$Title = sapply(all$Name, function(x) {strsplit(x, split='[,.]')[[1]][2]})
all$Title = gsub(' ', '', all$Title) # removing spaces before title
# sub 은 처음 등장하는 ' '를 ''로 바꿔주는 역할이고
# gsub은 모든 ' '를 ''로 바꿔주는 역할이다.
kable(table(all$Sex, all$Title))
# 패키지 knitr에 있는 kable함수는 문서 형태에 상관없이 Rmd에서 바로 테이블을 만들 수 있는 함수이다.
# 처음 오는 변수가 열이 되고, 뒤에 오는 변수가 행이 된다.

## 예측에 사용될 수 있는 더 좋은 Title들을 만들기 위해서 title의 수를 줄일 것이다.
## MS는 주로 결혼한 어린 여자에게 사용되며 Miss와 합칠것이다.
## Mlle는 프랑스에서 Mademoiselle을 상징한다고 추측한다. 이것 또한 Miss와 합칠 것이다.
## 그리고 Mme는 Madame을 뜻한다고 추측해서 이것을 Mrs와 합칠 것이다.
## Title간의 낮은 빈도를 위해서 나는 하나의 새로운 카테고리를 만들었다.

all$Title[all$Title %in% c("Mlle", "Ms")] = "Miss"
# %in%은 벡터 내 특정 값 포함 여부를 확인하는 연산자이다.
all$Title[all$Title == "Mme"] = "Mrs"
all$Title[!(all$Title %in% c("Master", "Miss", "Mr", "Mrs"))] = "Rare Title"
all$Title = as.factor(all$Title)
kable(table(all$Sex, all$Title))

ggplot(all[!is.na(all$Survived),], aes(x = Title, fill = Survived)) +
	geom_bar(stat = "count", position = "stack") + labs(x="Title") + theme_grey()

# 그래프를 보면 알 수 있듯이 Mr 즉, 남자들의 사망률이 많이 높은 것을 알 수 있다.

## 4.2 Finding groups of people traveling together

### 4.2.1 Families ; siblings, spouses(배우자), parents and children

# creating familly size variable (Fsize)
all$Fsize = all$SibSp + all$Parch + 1 # 1을 더하는 이유는 자기 자신도 쳐 줘야하기 때문이다.

ggplot(all[!is.na(all$Survived),], aes(x = Fsize, fill = Survived)) +
	geom_bar(stat = 'count', position = 'dodge') +
	scale_x_continuous(breaks = c(1:11)) +
	labs(x = "Family Size") + theme_grey()
# 위의 그래프를 보면 알 수 있겠지만 솔로인 사람들의 사망률이 훨씬 높게 나왔음을 알 수 있다.
# 게다가 2~4명이서 여행을 온 가족의 경우에는 생존률이 상대적으로 높음을 알 수 있다.
# scale_x_continuous(breaks=seq()) : 일정한 간격으로 x축, y축 설정
# scale_x_continuous(breaks=c()) : 분석가 마음대로 x축, y축 설정

# 이제 이 가족수를 solo, small family, large family로 범주형으로 전환시킨다.

### 4.2.2 Family Size inconsistencies, and correcting the effects of a cancellation
# 불일치한 가족 size 데이터를 확인하기 위해서 surname과 Fsize를 결합한 하나의 변수를 생성하자.
# 그 후에 이 결함들이 가족들의 수를 이끄는 결합인지를 확인하자
# Composing variable that combines total Fsize and Surname
all$FsizeName = paste(as.character(all$Fsize), all$Surname, sep="")

SizeCheck = all %>%
	group_by(FsizeName, Fsize) %>%
	summarise(NumObs = n())
SizeCheck$NumFam = SizeCheck$NumObs/SizeCheck$Fsize
SizeCheck$modulo = SizeCheck$NumObs %% SizeCheck$Fsize
SizeCheck = SizeCheck[SizeCheck$modulo != 0, ]
sum(SizeCheck$NumObs) # total number of Observations with inconsistencies

# summarise(NumObs = n()) 는 group_by와 함께 쓰이는 함수로 그룹별 관측치의 갯수를 구하는 n()을 사용한다. NumObs대신 n.obs로 사용가능
# %% : 나머지를 구하는 함수

kable(SizeCheck[SizeCheck$FsizeName %in% c('3Davies', '5Hocking', '6Richards', '2Wilkes', '3Richars', '4Hocking'),])

# 이 자료는 항상 가족들의 어림수를 추가하지는 않는다. 진짜로는 약 1300명의 승객들이 탑승했었던 리스트가 완벽해 보였다. 나머지는 승무원
# 약간의 불일치는 취소에 의해 설명 될 수 있을것이다. 예를 들어서 2 Davies 가족들이 탑승했었을 것이다.
# 반면에 SizeCheck는 오직 3Davies라는 FsizeName을 가진 5개의 관측치만을 보여준다.

kable(all[all$FsizeName == '3Davies', c(2,3,14,5,6,7,8,17,9,15)])

# A/4 48871과 A/4 48873의 티켓을 가진 Davies들은 완벽한 그룹처럼 봉인다. 이 오류는 Mrs Davies [1222]가 아이들 2명과 같이 여행을 온 것 처럼 보인다.
# 하지만 결국, Master Davies[550] 한명하고만 여행을 한다.
# 빠른 인터넷 검색은 Davies라고 불리는 한 사람이 병때문에 그의 여행을 취소했다고 알려줬다.

all$FsizeName[c(550, 1222)] = '2Davies'
all$SibSp[550] = 0
all$Parch[1222] = 1
all$Fsize[c(550, 1222)] = 2
kable(all[all$FsizeName == '2Davies', c(2,3,14,5,6,7,8,17,9,15)])

# 완전하게 옳게 관리되지 못했던 취소들이 훨씬 더 많았을 것이라고 생각한다. 
# 하지만 또한 마지막 모델에서의 효과들은 더욱 작을 것이다.

### 4.2.3 Families ; what about uncles, aunts, cousins, nieces, grandparents, brothers/sisters-in law?(시아버지/시누이)

# 여기에 소수의 취소들보다 더 흥미로운 정보들이 숨겨져있음을 찾았다. 예를 들어서, Hockings와 Richards가 관련이 있다는게 밝혀졌다. 
# 이 연관은 승객 438명이 2명의 아이들, 한 부모, 형제자매들과의 여행이었을 것이다.
# 예를 들어, 오직 남형제와 엄마의 수만 진짜로 가족으로 쳤을 때, 이것은 대부분의 가족들을 'apples to apples'와 비교될 수 없는 Fsize를 이끈다.
# 그들의 Fsizes는 일반적으로 매우 높을 것이지만, 이 사람들이 더 작은 그룹들로 갈라질 것이다.
# 엄마는 그녀의 아이들과 머물 것이고, 남동생과 여동생은 아마도 할머니와 머물 것이다.
## 노트 : 이 가족은 실제로 더 복잡할것이다. 할머니 또한 같은 결혼전의 성을 가진 여동생과 여행을 왔기 때문이다.
## 하지만, 이것은 진짜로 예외로 보이며, 또 다른 Mrs Needs는 이미 합리적인 2의 Fsize를 가지고 있기 때문에, 그녀를 고려하지 않을것이다.

kable(all[all$Ticket %in% c('29104', '29105', '29106'),c(2,3,4,5,6,7,8,9,15)])

# 이 문제들을 해결하기 위해, 처음으로 maiden name(결혼 정 성)을 사용하여 함께 가족들을 합쳐보자.

NC = all[all$FsizeName %in% SizeCheck$FsizeName,] #create data frame with only relevant Fsizenames

# extraqcting maiden names
NC$Name = sub("\\s$", "", NC$Name) #removing spaces at end Name
NC$Maiden = sub(".*[^\\)]$", "", NC$Name) #removing when not ending with ')'
NC$Maiden = sub(".*\\s(.*)\\)$", "\\1", NC$Maiden)
NC$Maiden[NC$Title!='Mrs'] = "" #cleaning up other stuff between brackets (including Nickname of a Mr)
NC$Maiden = sub("^\\(", '', NC$Maiden) #removing opening brackets(sometimes single name, no spaces between brackets)
# making an exceptions match
NC$Maiden[NC$Name == "Andersen-Jensen, Miss. Carla Christine Nielsine"] = 'Jensen'
# take only Maiden names that also exist as surname in other Observation
NC$Maiden2[NC$Maiden %in% NC$Surname] = NC$Maiden[NC$Maiden %in% NC$Surname]
NC$Maiden

# create surname+maiden name combinations
NC$Combi[!is.na(NC$Maiden2)] = paste(NC$Surname[!is.na(NC$Maiden2)], NC$Maiden[!is.na(NC$Maiden2)])

# create labels dataframe with surname and maiden merged into one column
labels1 = NC[!is.na(NC$Combi), c("Surname", "Combi")]
labels2 = NC[!is.na(NC$Combi), c('Maiden', 'Combi')]
colnames(labels2) = c('Surname', 'Combi')
labels1 = rbind(labels1, labels2)

NC$Combi = NULL
NC = left_join(NC, labels1, by='Surname')

# Find the maximum Fsize within each newly found 'second degree' family
CombiMaxF = NC[!is.na(NC$Combi),] %>%
	group_by(Combi) %>%
	summarise(MaxF = max(Fsize)) # summarise(MaxF = n())
NC = left_join(NC, CombiMaxF, by = 'Combi')

# create family names for those larger families
NC$FsizeCombi[!is.na(NC$Combi)] = paste(as.character(NC$Fsize[!is.na(NC$Combi)]), NC$Combi[!is.na(NC$Combi)], sep="")
NC$FsizeCombi[!is.na(NC$Combi)]

# find the ones in which not all Fsizes are the same
FamMaid = NC[!is.na(NC$FsizeCombi),] %>%
	group_by(FsizeCombi, MaxF, Fsize) %>%
	summarise(NumObs = n())
FamMaidWrong = FamMaid[FamMaid$MaxF != FamMaid$NumObs,]

kable(unique(NC[!is.na(NC$Combi) & NC$FsizeCombi %in% FamMaidWrong$FsizeCombi, c('Combi', 'MaxF')]))

# 7개 나온 조합결과(28명의 승객들로 얻어진)는 같은 Fsize를 가지는 모든 멤버들이 아닌 가족들로 찾아졌다.
# 일단은 어떤 가족들이 유사하게 남자편으로 연결되어있는지 찾아보자

NC$MaxF = NULL #erasing MaxF column maiden combi's

# Find the maximum Fsize within remaining families (no maiden combi's)
FamMale = NC[is.na(NC$Combi),] %>%
	group_by(Surname) %>%
	summarise(MaxF = max(Fsize))
NC = left_join(NC, FamMale, by = "Surname")

NCMale = NC[is.na(NC$Combi),] %>%
	group_by(Surname, FsizeName, MaxF) %>%
	summarise(count = n()) %>%
	group_by(Surname, MaxF) %>%
	filter(n() > 1) %>%
	summarise(NumFsizes = n())

NC$Combi[NC$Surname %in% NCMale$Surname] = NC$Surname[NC$Surname %in% NCMale$Surname]

kable(NCMale[, c(1,2)])

# 예를 들어서, Mr Julius Vander Planke는 배우자와 2명의 형제와 여행을 했다.
# 그의 배우자와 형제는 서로서로 'indiredctly' 관계이다.

kable(all[all$Surname == "Vander Planke", c(2,3,4,5,6,7,8,9,15)])

# 이것은 (37명의 승객들로 이루어진) 9 가족들이 'second degree' 가족 멤버를 포함함을 의미한다.
# 이제 원하는 것은 같은 Fsize를 여러 가족에서 각각의 멤버들에게 부여하는것이다.

# selecting those 37 passengers In Not Correct dataframe
NC = NC[(NC$FsizeCombi %in% FamMaidWrong$FsizeCombi)|(NC$Surname %in% NCMale$Surname),]

# calculatin the average Fsize for those 9 families
NC1 = NC %>%
	group_by(Combi) %>%
	summarise(Favg = mean(Fsize))
kable(NC1)

# 결과는 예를 들어서, Fsize가 Richards-Hockings 가족의 모든 6 사람들에 대하여 4이다.
# 이것은 지금 이 사람들을 같은 Fsize를 가진 모든 멤버들의 그룹에 합치는 것이 원했던 것이기 때문에 정확하게 원했던 것이다.
# 하지만 first degree 가족들 보다 덜 같이 머물기 때문에 maximum size는 아니다.

NC = left_join(NC, NC1, by = 'Combi') #adding Favg to NC dataframe
NC$Favg = round(NC$Favg) #rounding those averages to integers
NC = NC[, c("PassengerId", "Favg")]
all = left_join(all, NC, by = "PassengerId")

# replacing Fsize by Favg
all$Fsize[!is.na(all$Favg)] = all$Favg[!is.na(all$Favg)]

### 4.2.4 Can we still find more second degree families?

# creating a variable with almost the same ticket numbers (only last 2 digits varying)
all$Ticket2 = sub("..$", "xx", all$Ticket)

rest = all %>%
	select(PassengerId, Title, Age, Ticket, Ticket2, Surname, Fsize) %>%
	filter(Fsize == '1') %>%
	group_by(Ticket2, Surname) %>%
	summarise(count = n())
rest = rest[rest$count > 1,]
rest1 = all[(all$Ticket2 %in% rest$Ticket2 & all$Surname %in% rest$Surname & all$Fsize == '1'),
	c('PassengerId', 'Surname', 'Title', 'Age', 'Ticket', 'Ticket2', 'Fsize', 'SibSp', 'Parch')]
rest1 = left_join(rest1, rest, by = c("Surname", "Ticket2"))
rest1 = rest1[!is.na(rest1$count),]
rest1 = rest1 %>%
	arrange(Surname, Ticket2)
kable(rest1[1:12, ])

# replacing Fsize size in my overall dataframe with the count numbers in the table above
all <- left_join(all, rest1)

for (i in 1:nrow(all)){
	if(!is.na(all$count[i])){
		all$Fsize[i] = all$count[i]
	}
}

all

### 4.2.5 Did people book together?
kable(all[all$Ticket == '1601', c('Survived', 'Pclass', 'Title', 'Surname', 'Age', 'Ticket', 'SibSp', 'Parch',
	'Fsiez')])

# 사람들의 수를 각각의 ticket에 변수로 더한다.
# composing data frame with group size for each Ticket
TicketGroup = all %>%
	select(Ticket) %>%
	group_by(Ticket) %>%
	summarise(Tsize = n())
all = left_join(all, TicketGroup, by = "Ticket")

# 가족간 그룹 크기는 매우 비슷하고, 같은 티켓으로 함께 여행다니는 2-4명으로 이루어진 작은 그룹은 높은 생존율을 가진다.

ggplot(all[!is.na(all$Survived),], aes(x = Tsize, fill = Survived)) +
	geom_bar(stat = "count", position = "dodge") +
	scale_x_continuous(breaks = c(1:11)) +
	labs(x = "Ticket Size") + theme_grey()


# taking the max of family and ticket size as the group size
all$Group = all$Fsize
for (i in 1:nrow(all)){
	all$Group[i] = max(all$Group[i], all$Tsize[i])
}

all$GroupSize[all$Group == 1] = 'solo'
all$GroupSize[all$Group == 2] = 'duo'
all$GroupSize[all$Group >= 3 & all$Group <= 4] = 'group'
all$GroupSize[all$Group >= 5] = 'large group'
all$GroupSize = as.factor(all$GroupSize)
all$GroupSize

g1 = ggplot(all[!is.na(all$Survived),], aes(x = Group, fill = Survived)) +
	geom_bar(stat = "Count", position = "dodge") +
	scale_x_continuous(breaks = c(1:11)) +
	labs(x = "Final Group Sizes") + theme_grey()

g2 = ggplot(all[!is.na(all$Survived),], aes(x = GroupSize, fill = Survived)) +
	geom_bar(stat = "count", position = "dodge") +
	labs(x = "Final Group Categories") + theme_grey() +
	scale_x_discrete(limits = c("solo", "duo", "group", "large group"))

grid.arrange(g2, g1)

### 4.3.1 Which data relevvant to fare are missing?

# display passengers with missing Embarked
kable(all[which(is.na(all$Embarked)), c("Surname", "Title", "Survived", "Pclass", "Age", "SibSp",
	"Parch", "Ticket", "Fare", "Cabin", "Embarked", "Group")])

all$FarePP = all$Fare / all$Tsize #creating the Fare Per Person variable

tab2 = all[(!is.na(all$Embarked) & !is.na(all$Fare)),] %>%
	group_by(Embarked, Pclass) %>%
	summarise(FarePP = median(FarePP))
kable(tab2)

# imputing missing Embarked values
all$Embarked[all$Ticket == '113572'] = 'C'
#converting Embarked into a factor
all$Embarked = as.factor(all$Embarked)

# display passengers with missing Fare
kable(all[which(is.na(all$Fare)), c("Surname", "Title", "Survived", "Pclass", "Age", "SibSp", "Parch",
	"Ticket", "Fare", "Cabin", "Embarked", "Group")])

# imputing FarePP (as the Fare will be dropped later on anyway)
all$FarePP[1044] = 7.8

### 4.3.2 The Fare Per Person Variable

tab3 = all[(!is.na(all$FarePP)),] %>%
	group_by(Pclass) %>%
	summarise(MedianFarePP = median(FarePP))
all = left_join(all, tab3, by = "Pclass")
all$FarePP[which(all$FarePP == 0)] = all$MedianFarePP[which(all$FarePP == 0)]

ggplot(all, aes(x = FarePP)) + geom_histogram(binwidth = 5, fill = 'blue') +
	theme_grey() + scale_x_continuous(breaks = seq(0, 150, by = 10))


# Note Hmisc needs to be loaded before dplyr, as the other way around errors occured due to the kernel
# using the Hmisc summarize function instead of the dplyr summarize function
all$FareBins = cut2(all$FarePP, g = 5)

ggplot(all[!is.na(all$Survived),], aes(x = FareBins, fill = Survived)) +
	geom_bar(stat='count') + theme_grey() + facet_grid(.~Pclass) +
	theme(axis.text.x = element_text(angle = 45, hjust = 1))

## 4.4 Predicting missing Age values

ggplot(all[(!is.na(all$Survived) & !is.na(all$Age)),], aes(x = Age, fill = Survived)) +
	geom_density(alpha = 0.5, aes(fill = factor(Survived))) + labs(title = "Survival density and Age") +
	scale_x_continuous(breaks = scales::pretty_breaks(n = 10)) + theme_grey()


ggplot(all[!is.na(all$Age),], aes(x = Title, y = Age, fill = Pclass)) +
	geom_boxplot() + scale_y_continuous(breaks = scales::pretty_breaks(n = 10)) + theme_grey()

# predicting Age with Linear Regression

set.seed(12000)
AgeLM = lm(Age ~ Pclass + Sex + SibSp + Parch + Embarked + Title + GroupSize, data=all[!is.na(all$Age),])
summary(AgeLM)

all$AgeLM = predict(AgeLM, all)

par(mfrow = c(1,2))
hist(all$Age[!is.na(all$Age)], main = 'Original data, non-missing', xlab = "Age", col = "green")
hist(all$AgeLM[is.na(all$Age)], main = 'LM NA predictions', xlab = 'Age', col = 'orange', xlim=range(0:80))

# disply which passengers are predicted to be children (age < 18) with Linear Regression
all[(is.na(all$Age) & all$AgeLM < 18), c('Sex', 'SibSp', 'Parch', 'Title', 'Pclass', 'Survived', 'AgeLM')]

# imputing Linear Regression predictions for missing Ages
indexMissingAge = which(is.na(all$Age))
indexAgeSurvivedNotNA = which(!is.na(all$Age) & (!is.na(all$Survived))) # needed in sections 4.6 and 4.7

## 4.5 What to do with Cabin?

# replacing NAs with imaginary Deck U, and keeping only the first letter of ech Cabin ( = Deck )
all$Cabin[is.na(all$Cabin)] = "U"
all$Cabin = substring(all$Cabin, 1, 1)
all$Cabin = as.factor(all$Cabin)

ggplot(all[(!is.na(all$Survived) & all$Cabin != "U"),], aes(x = Cabin, fill = Survived)) +
	geom_bar(stat = 'count') + theme_grey() + facet_grid(.~Pclass) +
	labs(title = "Survivor split by class and Cabin")

c1 = round(prop.table(table(all$Survived[(!is.na(all$Survived)&all$Cabin != 'U')],
	all$Cabin[(!is.na(all$Survived)&all$Cabin!='U')]),2)*100)
kable(c1)


## 4.6 How to deal with Children in the model?

ggplot(all[all$Age < 14.5 & !is.na(all$Survived),], aes(x = Pclass, fill = Survived)) +
	geom_bar(stat = 'count') + theme_grey(base_size = 18)

all$IsChildP12 = 'No'
all$IsChildP12[all$Age <= 14.5 & all$Pclass %in% c('1', '2')] = 'Yes'
all$IsChildP12 = as.factor(all$IsChildP12)

## 4.7 What does Embarked tell us?

d1 = ggplot(all[!is.na(all$Survived),], aes(x = Embarked, fill = Survived)) +
	geom_bar(stat = 'count') + theme_grey() + labs(x = 'Embarked', y = 'Count')
d2 = ggplot(all[!is.na(all$Survived),], aes(x = Embarked, fill = Survived)) +
	geom_bar(stat = 'count', position = 'fill') + theme_grey() + labs(x = 'Embarked', y = 'Percent')

grid.arrange(d1, d2, nrow = 1)

ggplot(all[indexAgeSurvivedNotNA,], aes(x = Age, fill =Survived)) +
	geom_histogram(aes(fill = factor(Survived))) +
	labs(title = "Survival density, known-ages, and Embarked") +
	scale_x_continuous(breaks = scales::pretty_breaks(n=5)) + theme_grey() + facet_grid(.~Embarked)


tab1 <- rbind(table(all$Embarked[!is.na(all$Survived)]),table(all$Embarked[indexAgeSurvivedNotNA]))
tab1 <- cbind(tab1, (rowSums(tab1)))
tab1 <- rbind(tab1, tab1[1,]-tab1[2,])
tab1 <- rbind(tab1, round((tab1[3,]/tab1[1,])*100))
rownames(tab1) <- c("All", "With Age", "Missing Age", "Percent Missing")
colnames(tab1) <- c("C", "Q", "S", "Total")
kable(tab1)

## 4.8 Ticket survivors

TicketSurvivors <- all %>%
	group_by(Ticket) %>%
	summarize(Tsize = length(Survived),
		NumNA = sum(is.na(Survived)),
		SumSurvived = sum(as.numeric(Survived)-1, na.rm=T))

all <- left_join(all, TicketSurvivors)

all$AnySurvivors[all$Tsize==1] <- 'other'
all$AnySurvivors[all$Tsize>=2] <- ifelse(all$SumSurvived[all$Tsize>=2]>=1, 'survivors in group', 'other')
all$AnySurvivors <- as.factor(all$AnySurvivors)

kable(x=table(all$AnySurvivors), col.names= c('AnySurvivors', 'Frequency'))

## 4.9 Adding an "Is Solo" variable based on Siblings and Spous (SibSp) only

all$IsSolo[all$SibSp==0] <- 'Yes'
all$IsSolo[all$SibSp!=0] <- 'No'
all$IsSolo <- as.factor(all$IsSolo)

ggplot(all[!is.na(all$Survived),], aes(x = IsSolo, fill = Survived)) +
  geom_bar(stat='count') + theme_grey(base_size = 18)


# 5 Predictions (with caret cross validation)

#splitting data into train and test set again
trainClean <- all[!is.na(all$Survived),]
testClean <- all[is.na(all$Survived),]

## 5.1 Random Forest model

install.packages("e1071")
library(e1071)

set.seed(2017)
caret_matrix = train(x = trainClean[, c('PclassSex', 'GroupSize', 'FarePP', 'AnySurvivors', 'IsChildP12')],
	y=trainClean$Survived, data = trainClean, method = 'rf', trControl = trainControl(method="cv",number=5))
caret_matrix








































