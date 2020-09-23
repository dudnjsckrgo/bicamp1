
from entity import Entity
from service import Service



# 내부에서는 모듈의 객체를 인스턴스화해야 한다.
# 대문자는 클래스
# 소문자는 인스턴스= (객체)
# 라운드 브레이스가 있는 클래스는 생성자이다.
# 결론.. 객체지향(OOP)에서는 속성과 기능을 호출하는 구조로 
# 두가지 방식이 있는데
# (스태틱)클래스 객체
# (다이나믹) 인스턴스 객체

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
    
    def modeling(self,train, test):
        service = self.service
        this = self.preprocessing(train, test)
        print(f'훈련 컬럼: {this.train.columns}')
        this.label =service.create_label(this)
        this.train = service.create_train(this)
        return this
    
    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) #payload
        this.test = service.new_model(test)
        this.id = this.test['PassengerId'] #머신이에게는 이것이 question이 됩니다.
        
        this = service.drop_feature(this,'Cabin')
        this = service.drop_feature(this,'Ticket')
        
        this = service.drop_feature(this, 'PassengerId')
        this = service.embarked_norminal(this)
        print(f'드롭 후 변수 :\n{this.train.columns}')
        
        print(f'승선한 항구 정제 결과:\n{this.train.head()}')
       
        this = service.title_norminal(this)
        print(f'이름 정제 결과:\n{this.train.head()}')
        this = service.drop_feature(this, 'Name')
        
        this = service.fare_ordinal(this)
        print(f'요금 정제 결과:\n{this.train.head()}')
        this = service.fareBand_ordinal(this)
        print(f'요금2 정제 결과:\n{this.train.head()}')
        this = service.age_ordinal(this)
        print(f'나이 정제 결과:\n{this.train.head()}')
        this = service.sex_norminal(this)
        this = service.drop_feature(this,'Fare')
        print(f'성별 정제 결과:\n{this.train.head()}')
        print(f'#########  TEST 정제결과 ###############')
        print(f'{this.test.head()}')
        print(f'######## train na 체크 ##########')
        print(f'{this.train.isnull().sum()}')
        print(f'######## test na 체크 ##########')
        print(f'{this.test.isnull().sum()}')

        return this

    
    def learing(self,train,test):  # evaluation과 합친다.
        service = self.service
        this = self.modeling(train,test)
        print(f'결정 트리:{service.accuracy_by_dtree(this)}' )
        print(f'nb:{service.accuracy_by_nb(this)}')
        print(f'knn:{service.accuracy_by_knn(this)}')
        print(f'svm:{service.accuracy_by_svm(this)}')
        print(f'rforest:{service.accuracy_by_rforest(this)}')

    def submit(self): # 파일로 저장
        pass
if __name__ =='__main__':
    ctrl = Controller()
    ctrl.learing('train.csv', 'test.csv')
