class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def hello(self):
        return f'Hello {self.name} {self.surname}, it is nice to meet you!'

    def get_age(self):
        return self.__age

    def set_age(self, a):
        self.__age = a


person_1 = Person('Jane', 'Doe', 30)
print(person_1.hello())

person_2 = Person('Jake', 'Smith', 27)
print(person_2.hello())

class Work(Person):

    def __init__(self, name, surname, age, job, experience):
        super().__init__(name, surname, age)
        self.job = job
        self.experience = experience

    def welcome(self):
        # if experience < 2:
        #     return f'We are very happy that you decided to start your {self.job} career with us!'
        # else:
        return f'We are fascinated with your {self.experience} years of {self.job} experience. Welcome to our {self.job} Team!'


person_3 = Work('James', 'Brown', 33, 'Development', 7)
print(person_3.hello())
print(person_3.welcome())
print(f'{person_3.name} is {person_3._Person__age} y.o.')

person_4 = Work('Jules', 'McFloy', 22, 'Testing', 2)
print(person_4.hello())
print(person_4.welcome())
print(f'{person_4.name} is {person_4._Person__age} y.o.')