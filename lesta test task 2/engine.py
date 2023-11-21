class Engine2D: # класс Engine2D 
    def __init__(self): # инициализация 
        self.canvas = [] # список примитивов
        self.color = "black" # black - цвет по стандарту
    
    def add_figures(self, *figures): # добавление фигур на холст
        for figure in figures:
            self.canvas.append(figure)

    def draw(self): 
        Engine2D.set_color(self, self.color)
        for figure in self.canvas: # нарисовать все фигуры
            figure.draw() 
        self.canvas = [] # очистка

    def set_color(self, color = "black"): # изменение цвета для всех фигур и движка
        Shape.color = color
        self.color = color


class Shape: # базовый класс "фигура"
    color = "" # изначально цвет не указывается
    
    def __init__(self):
        pass

    def draw_figure(self, str): # стандартная функция для отрисовки любой фигуры (с/без указанием цвета)
        if self.color != "":
            print(str + "\nColor: {}".format(self.color))
        else:
            print(str)

class Circle(Shape): # класс круга
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self):
        self.draw_figure(f"Drawing Circle: with center {self.center} and radius {self.radius}")

class Triangle(Shape): # класс треугольника
    def __init__(self, vertices):
        self.vertices = vertices

    def draw(self):
        self.draw_figure(f"Drawing Triangle: with vertices {self.vertices}")

class Rectangle(Shape): # класс прямоугольника
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def draw(self):
        self.draw_figure(f"Drawing Rectangle: with top left vertice {self.top_left}, width {self.width} and height {self.height}")


# engine = Engine2D()

# circle = Circle((2, 3), 6)
# triangle = Triangle([(1, 1), (1, 2), (2, 1)])
# rectangle = Rectangle((2, 3), 4, 2)
# engine.set_color('white')
# circle.draw()
# engine.add_figures(circle, triangle, rectangle)
# engine.set_color('black')
# triangle.draw()
# engine.set_color('red')
# engine.draw() 