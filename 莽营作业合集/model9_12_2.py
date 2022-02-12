from model9_12_1 import UserPower

class AdminPower(UserPower):

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.adminer = Privileges()
        '''
        1.super()来初始化父类要求后面的形参得和父类的形参相同
        2.self.adminer = Privileges()是用来将实例作为属性即创建一个新的类来
          创造的新类作为其属性进行调用
        '''

    def print_hello_admin(self):
        print(f"Hello{self.FirstName}{self.LastName}! welcome to the python world!")


class Privileges:

    def __init__(self, pop_admin_power=0):
        self.privileges = []
        self.PopAdminPower = pop_admin_power
        """
        1.定义self.privileges元数的初始值是一个列表
        2.因为要继承AdminPower类的属性得赋初值给形参
        所以需要给他赋一个初值，因为后面要继续使用并且
        要给它赋值所以其初值是什么都可以
        """

    def admin_name(self, admin_power):
        self.privileges.append(admin_power)
        '''
        将给的实参通过形参赋值给self.privileges
        因为self.privileges实列表所以用append
        来添加实参的元素

        '''

    def admin_name01(self):
        print(self.privileges)
        '''
        对列表进行打印
        '''

    def admin_name03(self):
        while True:
            self.PopAdminPower = self.privileges.pop()
            print(f'你可以执行这些权利{self.PopAdminPower}')
            '''
             对已经生成的列表的每一个元素进行弹出
            并将这些元数进行与字符串进行打印
            '''
