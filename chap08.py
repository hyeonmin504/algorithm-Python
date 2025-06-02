#클래스
#클래스 선언, 생성자, /self: this
# __함수 이름__ : 특수 메소드
class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
        print("{}번 학생".format(Student.count))
    pass
student = [
    Student("이름")
    ]
print(student[0].name)

#클래스 함수, cls: this
class ClassStudent:
    count = 0
    classStudent = []

    @classmethod
    def print(cls):
        print("=====================")
        print("이름\t이름")
        for ClassStudent in cls.classStudent:
            print(str(ClassStudent))
        print("=====================")

    def __init__(self,name):
        self.name = name
        ClassStudent.count += 1
        ClassStudent.classStudent.append(self)

    def get_name(self):
        return self.name

    def __str__(self):      #str를 함수의 매개변수로 호출하면 __str__함수가 자동으로 호출된다
        return "{}\t{}\t{}".format(
            self.name,
            self.get_name(),
            self.count)

ClassStudent("a")
ClassStudent("b")
ClassStudent("c")
ClassStudent("d")
ClassStudent.print()

#클래스 변수 만들기, Public 변수 접근
class classname:
    value = 123
classname.value

#private 변수 만들기 __변수이름 <- 함수 내부 private 변수
#getter setter
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_radius(self, radius):   #getter
        return self.__radius
    def set_radius(self, radius):   #setter
        self.__radius = radius
Circle(10)

#상속
class Parent:
    def __init__(self):
        self.value = "test"
        print("__init()__ method of Parent class is called")
    def test(self):
        print("Parent class test() method")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("__init()__ method of Child class is called")

child = Child()
child.test()
print(child.value)
