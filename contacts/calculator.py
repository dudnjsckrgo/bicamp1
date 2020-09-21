class Caculator:
    def __init__(self,num1,num2):
        self.num1 =num1
        self.num2 =num2
    def sum(self):
        return self.num1 +self.num2
    def sub(self):
        return self.num1 -self.num2
    def mul(self):
        return self.num1 *self.num2
    def div(self):
        return self.num1 /self.num2
if __name__ =="__main__":
    calc =Caculator(4,6)
    result = calc.sum()
    result2 = calc.sub()
    result3 = calc.mul()
    result4 = calc.div()

    print('덧셈결과 {}'.format(result))
    print('뺄셈결과 {}'.format(result2))
    print('곱셈결과 {}'.format(result3))
    print('나눗셈결과 {}'.format(result4))


    