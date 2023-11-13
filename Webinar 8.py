# Webinar 8

# Task 1
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)

    def drop(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)

    def view_courses(self):
        return [course.name for course in self.enrolled_courses]

class Course:
    def __init__(self, name, course_code):
        self.name = name
        self.course_code = course_code

class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        return [student.name for student in self.students]

    def view_courses(self):
        return [course.name for course in self.courses]

# Testing the implementation
uni = University("Harvard")

maths = Course("Mathematics", "MATH101")
physics = Course("Physics", "PHYS101")

uni.add_course(maths)
uni.add_course(physics)

alice = Student("Alice", "S101")

uni.add_student(alice)

alice.enroll(maths)

print("Alice's courses:", alice.view_courses())  
print("Students in university:", uni.view_students())  
print("Courses in university:", uni.view_courses())  


# Task 2
class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.description} at ${self.price}"

class Warehouse:
    def __init__(self):
        self.stock = {}

    def add_product(self, product, quantity):
        product_key = product.name
        if product_key not in self.stock:
            self.stock[product_key] = {'product': product, 'quantity': 0}
        self.stock[product_key]['quantity'] += quantity

    def update_inventory(self, order):
        for product_name, quantity in order.items():
            if product_name in self.stock and self.stock[product_name]['quantity'] >= quantity:
                self.stock[product_name]['quantity'] -= quantity
            elif product_name in self.stock:
                print(f"Not enough {product_name} in stock.")
        self.display_stock()

    def display_stock(self):
        print("Warehouse Stock:")
        for product_key, info in self.stock.items():
            product, quantity = info['product'], info['quantity']
            print(f"{product}: {quantity} in stock")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        self.cart.remove_product(product, quantity)

    def show_cart(self):
        print(self.cart)

    def place_order(self, warehouse):
        order = self.cart.create_order()
        if order:  
            warehouse.update_inventory(order)
            self.cart.clear_cart()  
        else:
            print("Your cart is empty. Please add items to your cart before placing an order.")

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.name not in self.items:
            self.items[product.name] = {'product': product, 'quantity': 0}
        self.items[product.name]['quantity'] += quantity

    def remove_product(self, product, quantity):
        if product.name in self.items and self.items[product.name]['quantity'] >= quantity:
            self.items[product.name]['quantity'] -= quantity
            if self.items[product.name]['quantity'] == 0:
                del self.items[product.name]
        elif product.name in self.items:
            print(f"Not enough quantity of {product.name} to remove.")

    def create_order(self):
        order_items = {item['product'].name: item['quantity'] for item in self.items.values()}
        return order_items

    def clear_cart(self):
        self.items.clear()

    def __str__(self):
        cart_contents = "Shopping Cart:\n" + "\n".join([f"{item['product']} - Quantity: {item['quantity']}"
                                                         for item in self.items.values()])
        return cart_contents if cart_contents else "Your shopping cart is empty."

# Example usage:
product1 = Product("Laptop", "High-performance laptop", 999.99)
product2 = Product("Headphones", "Noise-canceling headphones", 149.99)

warehouse = Warehouse()
warehouse.add_product(product1, 10)
warehouse.add_product(product2, 20)

user1 = User("Alice", "alice@example.com")
user1.add_to_cart(product1, 2)
user1.add_to_cart(product2, 3)

warehouse.display_stock()
user1.show_cart()
user1.place_order(warehouse)
warehouse.display_stock()  

user1.show_cart() 


