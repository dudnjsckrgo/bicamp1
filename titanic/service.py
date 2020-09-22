from entity import Entity
import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '/Users/dudnj/bitcampt')
# PassengerId  고객ID,
# Survived 생존여부,
# Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
# Name,
# Sex,
# Age,
# SibSp 동반한 형제, 자매, 배우자,
# Parch 동반한 부모, 자식,
# Ticket 티켓번호,
# Fare 요금,
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
        return pd.read_csv(this.context + this.fname) # p.139 df=tensor

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
    
# variable x=3 스칼라
# array [element=(varable)]
# matrix  [[vector=(array)]] 