#添加学员函数内部需要创建学员对象，故先导入student模块
import student
class studentmanager():
    def __init__(self):
        #存储数据所用的列表
        self.student_list=[]
    #-，程序入口函数，启动程序后执行的函数
    def run(self):
        #1.加载学员信息
        self.load_student()
        while True:
            #2.显示功能菜单
            self.show_menu()
            #3.用户输入功能序号
            menu_num=int(input('请输入你需要的功能序号：'))
            #4.根据用户输入的功能序号执行不同的功能
            if menu_num==1:
                #添加学员
                self.add_student()
            elif menu_num==2:
                #删除学员
                self.del_student()
            elif menu_num==3:
                #修改学员信息
                self.modify_student()
            elif menu_num==4:
                #查询学员信息
                self.search_student()
            elif menu_num==5:
                #显示所有学员信息
                self.show_student()
            elif menu_num==6:
                #保存学员信息
                self.save_student()
            elif menu_num==7:
                #退出系统
                break
    #二，系统功能函数
    #2.1显示功能菜单--打印序号的功能对应关系--静态
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')
    #2.2添加学员
    def add_student(self):
        name=input('请输入你的姓名')
        gender=input('请输入你的性别')
        tel=input('请输入你的手机号')
        stu=student.Student(name,gender,tel)
        self.student_list.append(stu)
    #2.3删除学员
    def del_student(self):
        #用户输入目标学员姓名
        del_name=input('请输入要删除的学员姓名：')
        #如果用户输入的目标学员存在则删除，否则提示学员不存在
        for i in self.student_list:
            if i.name==del_name:
                self.student_list.remove(i)
                break
        else:
            print('查无此人')

    #2.4修改学员信息
    def modify_student(self):
        #用户输入目标学员姓名
        modify_name=input('请输入要修改的学员的姓名')
        #如果用户输入的目标学员存在则修改姓名，性别，手机号等数据，字符提示不存在
        for i in self.student_list:
            if i.name==modify_name:
                i.name=input('请输入学员姓名')
                i.gender=input('请输入学员性别')
                i.tel=input('请输入学员手机号')
                print(f'修改该学员成功，姓名：{i.name},性别{i.gender},手机号{i.tel}')
                break
        else:
            print('查无此人')
    #2.5查询学员信息
    def search_student(self):
        #用户输入目标学员姓名
        search_name=input('请输入要查询的学员的姓名')
        #如果用户输入的目标学员存在，则打印学员信息，否则提示学员不存在
        for i in self.student_list:
            if i.name==search_name:
                print(f'姓名{i.name}，性别{i.gender}，手机号{i.tel}')
                break
        else:
            print('查无此人')
    #2.6显示所有学员信息
    def show_student(self):
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')
    #2.7保存学员信息
    def save_student(self):
        #1.打开文件
        f=open('student.data','w',encoding='utf_8')
        #2.文件写入学员数据
        #注意1：文件写入的数据不能是学员对象的内存地址，需要把学员数据转换为列表字典数据再做存储
        new_list=[i.__dict__ for i in self.student_list]
        #[{'name':'aa','gender':'nv','tel':'111'}]
        print(new_list)

        #文件内数据要求为字符串类型，故需要转数据类型为字符串才能文件写入数据
        f.write(str(new_list))

        f.close()
    #2.8加载学员信息
    def load_student(self):
        #尝试以‘r’模式打开数据文件，文件不存在则提示用户：文件存在则读取数据
        try:
            f=open('student.data','r',encoding='utf_8')
        except:
            f=open('student.data','w',encoding='utf_8')
        else:
            #1.读取数据
            data=f.read()
            #2.文件中读取的数据都是字符串且字符串镍币为字典数据，故需要转换数据类型再转换字典为对象后存储到学员列表
            new_List=eval(data)
            self.student_list=[student.Student(i['name'],i['gender'],i['tel']) for i in new_List]
        finally:
            f.close()