"""
Calci
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from functools import partial


class Calculator(toga.App):

    def startup(self):
        box1=toga.Box()
        box2=toga.Box()
        box3=toga.Box()
        box4=toga.Box()
        box5=toga.Box()
        box6=toga.Box()

        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.input=toga.TextInput()
        self.input.style.width=300

        number7=toga.Button('7',on_press=partial(self.enterdata,number='7'))
        number7.style.padding_top=20

        number8=toga.Button('8',on_press=partial(self.enterdata,number='8'))
        number8.style.padding_top=20

        number9=toga.Button('9',on_press=partial(self.enterdata,number='9'))
        number9.style.padding_top=20

        operation_multiply=toga.Button('*',on_press=partial(self.enterdata,number='*'))
        operation_multiply.style.padding_top=20



        number4=toga.Button('4',on_press=partial(self.enterdata,number='4'))
        
        number5=toga.Button('5',on_press=partial(self.enterdata,number='5'))
        
        number6=toga.Button('6',on_press=partial(self.enterdata,number='6'))
        
        operation_subtract=toga.Button('-',on_press=partial(self.enterdata,number='-'))


        number1=toga.Button('1',on_press=partial(self.enterdata,number='1'))
        
        number2=toga.Button('2',on_press=partial(self.enterdata,number='2'))
        
        number3=toga.Button('3',on_press=partial(self.enterdata,number='3'))
        
        operation_add=toga.Button('+',on_press=partial(self.enterdata,number='+'))


        decimal=toga.Button('.',on_press=partial(self.enterdata,number='.'))
        
        number0=toga.Button('0',on_press=partial(self.enterdata,number='0'))
        
        clear=toga.Button('C',on_press=partial(self.enterdata,number='C'))
        
        operation_divide=toga.Button('/',on_press=partial(self.enterdata,number='/'))


        button_calculate=toga.Button('Calculate',on_press=self.calculate)
        button_calculate.style.width=300
        button_calculate.style.padding_top=20


        box1.add(self.input)

        box2.add(number7)
        box2.add(number8)
        box2.add(number9)
        box2.add(operation_multiply)

        box3.add(number4)
        box3.add(number5)
        box3.add(number6)
        box3.add(operation_subtract)

        box4.add(number1)
        box4.add(number2)
        box4.add(number3)
        box4.add(operation_add)

        box5.add(decimal)
        box5.add(number0)
        box5.add(clear)
        box5.add(operation_divide)

        box6.add(button_calculate)

        

        main_box.add(box1)
        main_box.add(box2)
        main_box.add(box3)
        main_box.add(box4)
        main_box.add(box5)
        main_box.add(box6)


        
        
    

        
        

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()



    def enterdata(self,widget,number):
        if(number=='C'):
            self.input.value=""
        else:
            self.input.value=self.input.value+number
    def calculate(self,widget):
        output=eval(self.input.value)
        self.main_window.info_dialog("Result",str(output))   


def main():
    return Calculator()
