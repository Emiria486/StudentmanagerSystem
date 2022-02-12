class Student():
    def __init__(self,name,gender,tel):
        self.name=name
        self.gender=gender
        self.tel=tel
    def __str__(self):
        return f'学员姓名：{self.name}，学员性别：{self.gender}，学员手机号：{self.tel}'
