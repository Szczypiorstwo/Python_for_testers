# Sprawdz komentarze umieszczone przez IDE. Popraw plik tak by by zgodny ze standardem PEP.


import os, sys

class demoClass():
    def __init__(self):
        pass

    def foo(self):
        print("foobar")

class TextEditor:
    def __init__(this, text):
        this.text = text


def myFunction():
    print("BAR")


class TextEditor:

    def __init__(self, text):
		self.text = text


myVar = 10

MY_CONST_PI = 3.14159265359

myObject = demoClass()
myObject.foo()

print(myVar)
myFunction()

editor = TextEditor("Do-re-mi-fa-so-la-si-do")


def foo():
    pass


gross_wages = 0;
dividends = 0;
qualified_dividends = 0;
ira_deduction = 0;
student_loan_interest = 0;
taxable_interest = 0

income = (gross_wages + taxable_interest + (dividends - qualified_dividends) - ira_deduction - student_loan_interest + 99999)

with open('/path/to/some/file/you/want/to/read') as file_1, open('/path/to/some/file/being/written', 'w') as file_2, open('/path/to/some/file/being/binary', 'b') as file_3:
    file_2.write(file_1.read())

os.environ
sys.argv
