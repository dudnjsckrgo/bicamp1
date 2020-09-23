
from entity import Entity
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import kneighbors_graph
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

##### PassengerId  고객ID,
###### Survived 생존여부,
# Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
# Name,
# Sex,
# Age,
# SibSp 동반한 형제, 자매, 배우자,
# Parch 동반한 부모, 자식,
##### Ticket 티켓번호,
###### Fare 요금,
# Cabin 객실번호,
# Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼

# 메타데이터 = 스키마 =feature =variables =property
# row ,행 ,인스턴스, raw 데이터
# 

class Service:
    def __init__(self):
        self.entity = Entity() 
    # payload(컴퓨팅)
    # 전송되는 데이터
    def new_model(self, payload)-> object:
        this = self.entity
    
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this)-> object:
        return this.train.drop('Survived',axis=1) #train 은 답이 제거된 데이터셋이다.

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this,feature) -> object:
        this.train =this.train.drop([feature],axis=1)
        this.test = this.test.drop([feature],axis=1)
        return this
    @staticmethod
    def pclass_ordinal(this)-> object:
        return this
    @staticmethod
    def name_norminal(this)-> object:
        return this
    @staticmethod
    def sex_norminal(this)-> object:
        combine =[this.train,this.test]
        sex_mapping= {'male': 0,'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        this.train = combine[0] # overriding
        this.test= combine[1]
        return this
    @staticmethod
    def age_ordinal(this)-> object:
        train = this.train
        test = this.test
        train['Age']= train['Age'].fillna(-0.5)
        test['Age']= test['Age'].fillna(-0.5) 
        
        # age 는 가중치가 상당하므로 디테일한 접근이 필요합니다.
        # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일수 있다.
        # -0.5 라는 중간값으로 처리했습니다.
        bins =[-1,0,5,12,18,24,35,60,np.inf]
        # [] 에 있으니 이것은 변수명
        labels = ['Unknown','Baby','Child','Teenager','Student','Young Adult','Adult','Senior']
        train['AgeGroup']=pd.cut(train['Age'],bins,labels =labels)
        test['AgeGroup']=pd.cut(train['Age'],bins,labels =labels)
        age_title_mapping = {
            0:'Unknown',
            1:'Baby',
            2:'Child',
            3:'Teenager',
            4:'Student',
            5:'Young Adult',
            6:'Adult',
            7:'Senior'
        }

        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x]= age_title_mapping[train['Title'][x]]

        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
                test['AgeGroup'][x]= age_title_mapping[train['Title'][x]]       
        age_mapping = {
            'Unknown':0,
            'Baby':1,
            'Child':2,
            'Teenager':3,
            'Student':4,
            'Young Adult':5,
            'Adult':6,
            'Senior':7
        }    
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        return this
    
    @staticmethod
    def sibsp_numeric(this)-> object:
        return this
    @staticmethod
    def parch_numeric(this)-> object:
        return this
    @staticmethod
    def embarked_norminal(this)-> object:
        
        this.train = this.train.fillna({'Embarked':'S'}) # S가 가장 많아서 빈곳에 채움
        this.test = this.test.fillna({'Embarked':'S'}) #  교과서 144
        # 많은 머신러닝 라이브러리는 클래스 레이블이"정수"로 인코딩 되어있다고 기대함
        this.train['Embarked']= this.train['Embarked'].map({'S': 1, 'C':2 , 'Q':3} )
        this.test['Embarked']= this.test['Embarked'].map({'S': 1, 'C':2 , 'Q':3} )

        return this
    @staticmethod
    def fare_ordinal(this)-> object:
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1,2,3,4})
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1,2,3,4})
        return this   
    @staticmethod
    def fareBand_ordinal(this)-> object:
        this.train = this.train.fillna({"FareBand":1})
        this.test = this.test.fillna({"FareBand":1})
        return this
    @staticmethod
    def title_norminal(this)-> object:
        combine =[this.train,this.test]
        for dataset in combine:
            dataset['Title']= dataset.Name.str.extract('([A-Za-z]+)\.',expand= False)
        for dataset in combine:
            dataset['Title']= dataset['Title'].replace(['Mme','Capt', 'Col','Don','Dr','Major','Rev','Jonkheer','Dona'],'Rare')
            dataset['Title']= dataset['Title'].replace(['Countess','Lady','Sir'],'Rare')
            dataset['Title']= dataset['Title'].replace('Ms','Miss')
            dataset['Title']= dataset['Title'].replace('Mlle','Mr')
        title_mapping ={'Mr':1,'Miss':2,'Mrs':3,'Master':4,'Royal':5,'Rare':6}
        for dataset in combine:
            dataset['Title']= dataset['Title'].map(title_mapping)
            dataset['Title']= dataset['Title'].fillna(0) # Unknown
        this.train = this.train
        this.test = this.test
        return this
# variable x=3 스칼라
# array [element=(varable)]
# matrix  [[vector=(array)]] 