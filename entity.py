
class Entity:
    # entity 속성을 담당 entity+service = object
    # 같은 컨셉을 공유하는 클래스의 집합...
    # 모델에 AI 개념이 없으면 web 에서 말하는 모델이고 
    # AI 개념이 존재하면 인공지능 model이 된다.
    def __init__(self, context, fname, train, test, id, label):
        self._context = context #_는 default 접근의미, __2개는 private 접근의미
        self._fname= fname
        self._train= train
        self._test =test
        self._id =id
        self._label =label 
        # 나머지는 완성하세요
    # get, set 를 만듭니다.
    @property
    def context(self) -> str:
        return self._context
    @context.setter
    def context(self,context):
        self._cotext = context
    # fname get, set
    @property
    def fname(self) -> str:
        return self._fname
    @fname.setter
    def fname(self,fname):
        self._fname = fname
    # train get, set
    @property
    def train(self) -> str:
        return self._train
    @train.setter
    def train(self, train):
        self._train = train
    # test get, set
    @property
    def test(self) -> str:
        return self._test
    @test.setter
    def test(self, test):
        self._test = test
    # id get, set
    @property
    def id(self) -> str:
        return self._id
    @id.setter
    def id(self, id):
        self._id = id
    # label get, set
    @property
    def label(self) -> str:
        return self._label
    @label.setter
    def label(self, label):
        self._label = label