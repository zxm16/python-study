class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f'打印{self.name}')

    def open_restaurant(self):
        print(f'打印{self.type}')

    def user_want(self):
        print(f'祁诗瑞想在{self.name}吃{self.type}')
