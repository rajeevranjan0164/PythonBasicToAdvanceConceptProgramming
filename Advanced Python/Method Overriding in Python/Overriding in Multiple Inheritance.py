class Teacher:
    def introduce(self):
        print("I am a Teacher")

class Writer:
    def write(self):
        print("Writing an article")

class Author(Teacher, Writer):
    def introduce(self):
        print("I am an Author")

obj = Author()
obj.introduce()
obj.write()