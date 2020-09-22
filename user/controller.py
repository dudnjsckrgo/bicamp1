from user.entity import Entity
from user.service import Service


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()
    def preprocessing(self):
        pass
    def modeling(self):
        pass
    def learing(self):  # evaluation과 합친다.
        pass
    def submit(self): # 파일로 저장
        pass