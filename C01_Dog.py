class Dog:

    def __init__(self, name, age):
        self.name = name

        self.age = age


    def bark(self):
        print(f"{self.name} says Woof!")


# Create a Dog object

my_dog = Dog("Buddy", 2)

# Access attributes

print(my_dog.name)  # Output: Buddy

print(my_dog.age)  # Output: 2

# Call methods

my_dog.bark()  # Output: Buddy says Woof!