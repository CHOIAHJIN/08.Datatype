class Room :
    def __init__(self,l,s,k,m,y) :
        self.room_location= l
        self.room_size = s
        self.room_kind = k
        self.room_price = m
        self.room_year = y
    def print_info(self):
        print(
            "빌딩 위치 : "self.room_location,
            "건물 평수 : "self.room_size,
            "건물 종류 : "self.room_kind,
            "건물 가격 : "self.room_price,
            "건물 년수 : "self.room_year)

my_room = Room("강남", " 50평", " 아파트", " 100억", " 1년")
