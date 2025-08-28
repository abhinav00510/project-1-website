from abc import ABC,abstractmethod

# #dynamictyping

# class vscode:
#     def execute(self):
#         print("Compiling...")
#         print("Running...")

# class editor:
#     def execute(self):
#         print(4*5)
#         print(152)

# class laptop:
#     def code(self,ide):
#         ide.execute()



# ide = editor()
# lap = laptop()

# lap.code(ide)





# abstract class and method


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("bark...")

    def move(self):
        print("Move..")


a = Dog()
a.make_sound()
a.move()