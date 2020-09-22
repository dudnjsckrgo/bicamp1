import sys
sys.path.insert(0, '/Users/dudnj/bitcampt')
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
    def preprocessing(self, train, test):
        service = self.service
        this = self.entity
        this.train = service.new_model(train) #payload
        this.test = service.new_model(test)
        return this

    def modeling(self,train, test):
        service = self.service
        this = self.preprocessing(train, test)
        print(f'훈련 컬럼: {this.train.columns}')
        this.label =service.create_label(this)
        this.train = service.create_train(this)
    def learing(self):  # evaluation과 합친다.
        pass
    def submit(self): # 파일로 저장
        pass
if __name__ =='__main__':
    ctrl = Controller()
    ctrl.modeling('train.csv', 'test.csv')