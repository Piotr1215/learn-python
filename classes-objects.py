class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' says woof!'


def main():
    d = Dog('Fido')
    print(d.speak())
    f = open('learning.py', 'r')
    read = f.read()
    print(read.capitalize())
    f.close()


main()