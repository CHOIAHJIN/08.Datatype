class 회원가입 :
    def __init__(self, name, age, num) :
        self.회원가입_name = name
        self.회원가입_age = age
        self.회원가입_num = num
    def info(self):
        print("입력하신 이름은 " + self.회원가입_name+"이며, 나이는 " + self.회원가입_age, "그리고 연락처는 " + self.회원가입_num + "입니다.")

회원=회원가입("최아진", "24", "010-8790-8594")
회원.info()