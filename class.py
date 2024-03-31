class Student :

    count = 0
    student = []

    def init(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math =math
        self.english = english
        self.science = science
        Student.count= Student.count+1
        Student.student.append(self)

    @classmethod
    def print(cls):
        print("학생 목록")
        print("이름 \t 총점 \t 평균")
        for student in cls.student:
            print(str(student))
        print("------------")
    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

    def get_sum(self):
        return self.korean +self.math + self.english +self.science
    def get_average(self):
        return self.get_sum()/4
    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum,self.get_average)
    
