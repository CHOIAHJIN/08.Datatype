# class Dog :
#     # class 이름은 첫글자 대문자
#     def __init__(self, name, breed) :
#         self.dog_name = name
#         self.dog_breed = breed
#         self.dog_sex = "남"
#
#     def bark(self):
#             print(self.dog_name + "가 짖습니다.")
#
# Dog("깜돌이", "믹스").bark()
# # print(Dog("깜돌이", "믹스").dog_sex)
#
# my_dog = Dog("깜돌이", "믹스")
# my_dog.bark()

class Text :
    def __init__(self, len, p, p2 ) :

        self.Text_len = len
        self.Text_p = p
        self.Text_p2 =p2

    def text(self,a):
        self.text_len = a
        l = len(self.text_len)
        if l <=len :
            result = (self.Text_p+"원입니다.")
            print(result)
        if l >len :
            result = (self.Text_p2+"원입니다.")
            print(result)

요금 = Text("50", "2", "5")
요금.text()