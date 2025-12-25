#адание 1
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}'
    
book = Book('Маленький принц', 'Антуан де Сент-Экзюпери', '1943')
print(book.get_info())
    
#Задание 2
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, new_radius):
        self.radius = new_radius

circle = Circle(3)
print('Текущий радиус:', circle.get_radius())
circle.set_radius(6)
print('Новый радиус:', circle.get_radius())