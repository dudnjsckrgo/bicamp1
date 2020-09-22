from dataclasses import dataclass

@dataclass
class Entity:
    # entity 속성을 담당 entity+service = object
    # 같은 컨셉을 공유하는 클래스의 집합...
    # 모델에 AI 개념이 없으면 web 에서 말하는 모델이고 
    # AI 개념이 존재하면 인공지능 model이 된다.
    
    context :str = '/Users/dudnj/bitcamp/SbaProjects/titanic/data/'
    fname : str = ''
    train: object = None
    test : object = None
    id : str = ''
    label: str = ''

