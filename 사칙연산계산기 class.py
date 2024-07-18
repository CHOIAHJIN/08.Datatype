class 사칙연산계산기 :
    def 더하기 (self, a, b) :
        result = a + b
        return result
    def 빼기 (self, a, b) :
        result = a - b
        return result
    def 곱하기 (self, a, b) :
        result = a * b
        return result
    def 나누기 (self, a, b):
        result = a / b
        return result

# 들여쓰기가 끝난 부분 : class가 아니다.
app = 사칙연산계산기()
print(app.나누기(4,5))