
number : int = 12
number_2 : float = 30.5
boolean_var = True
String_var = 'My String'

my_list = [1,2,3,4,5,'String',[1,2,3],100]
my_map = {
    'Key_1': 1,
    'Key_2': 2
}
my_map_2 = {
     'Key_3': 3,
     'Key_4': 4,
     'Key_5': 5
}

studentDb = {
     '01': {
          'name': 'Mufa',
          'age': 24,
          'hobi': ['Renang', 'Futsal']
     },
     '02': {
          'name': 'Zidan',
          'age': 22,
          'hobi': ['Game', 'Gym']
     },
}

def 

if __name__ == '__main__':
     #my_map.update(my_map_2)
     #print(my_map)
     #number = float(number)
     #print(number,'=>',type(number))
     #number_2 = int(number_2)
     #print(number_2,'=>',type(number_2))
     print(studentDb['01']['hobi'])
def say_hello(to='Mufa', receiver='Zidan'):
     print(f'Hello {to}, my friend, i am {receiver}.')

class students:
     def __init__(self, name=''):
          self.name = name
     
     def say_hello(self):
          print(f'Hello my name is {self.name}')
          
      

if __name__ == '__main__':

     student = students(name='Mufa')
     student.say_hello()
     student = students(name='Zidan')
     student.say_hello()

     

