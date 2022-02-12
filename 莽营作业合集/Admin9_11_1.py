class UserPower:

    def __init__(self, firstname, lastname):
        self.FirstName = firstname
        self.LastName = lastname

    def write_hello_user(self):
        print(f"Hello{self.FirstName}{self.LastName}! welcome to the python world!")


class AdminPower(UserPower):

    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.adminer = Privileges()

    def print_hello_admin(self):
        print(f"Hello{self.FirstName}{self.LastName}! welcome to the python world!")


class Privileges:

    def __init__(self, pop_admin_power=0):
        self.privileges = []
        self.PopAdminPower = pop_admin_power

    def admin_name(self, admin_power):
        self.privileges.append(admin_power)

    def admin_name01(self):
        print(self.privileges)

    def admin_name03(self):
        while True:
            self.PopAdminPower = self.privileges.pop()
            print(f'你可以执行这些权利{self.PopAdminPower}')
