import pytest
from engine import Engine2D, Circle, Triangle, Rectangle

@pytest.fixture # фикстура для Engine2D
def engine():
    return Engine2D()

def test_circle_draw(capfd): # проверка draw в классе Circle

    circle = Circle((0, 0), 1)
    circle.draw() 

    out, err = capfd.readouterr() 
    assert out == "Drawing Circle: with center (0, 0) and radius 1\n"

def test_triangle_draw(capfd): # проверка draw в классе Triangle

    triangle = Triangle([(1, 1), (1, 2), (2, 1)])

    triangle.draw() 

    out, err = capfd.readouterr() 
    assert out == "Drawing Triangle: with vertices [(1, 1), (1, 2), (2, 1)]\n"

def test_rectangle_draw(capfd): # проверка draw в классе Rectangle

    rectangle = Rectangle((4, 4), 5, 3)

    rectangle.draw() 

    out, err = capfd.readouterr() 
    assert out == "Drawing Rectangle: with top left vertice (4, 4), width 5 and height 3\n"

def test_engine_def(engine): # проверка на принадлежность и дефолтного цвета для движка
    assert isinstance(engine, Engine2D)
    assert engine.color == "black"

def test_engine_draw(engine, capfd): # проверяем метод draw для движка
    
    circle = Circle((2, 3), 6)
    triangle = Triangle([(1, 1), (1, 2), (2, 1)])
    rectangle = Rectangle((2, 3), 4, 2)

    engine.add_figures(circle, triangle, rectangle)
    engine.set_color('red')

    engine.draw() 

    out, err = capfd.readouterr() 
    assert out == 'Drawing Circle: with center (2, 3) and radius 6\nColor: red\nDrawing Triangle: with vertices [(1, 1), (1, 2), (2, 1)]\nColor: red\nDrawing Rectangle: with top left vertice (2, 3), width 4 and height 2\nColor: red\n'
    

def test_set_color(engine): # проверяем метод set_color

    engine.set_color("blue")
    assert engine.color == "blue"
    
def test_add_figure(engine): # проверяем метод add_figures на одной фигуре

    rectangle = Rectangle((4, 4), 5, 3)

    engine.add_figures(rectangle)

    assert engine.canvas == [rectangle]

def test_add_figures(engine): # проверяем метод add_figures на нескольких фигурах
    
    circle = Circle((0, 0), 1)
    triangle = Triangle([(1, 1), (1, 2), (2, 1)])
    triangle2 = Triangle([(2, 2), (4, 4), (1, 8)])

    engine.add_figures(circle, triangle, triangle2)

    assert engine.canvas == [circle, triangle, triangle2]

def test_empty_canvas(engine): # проверяем очистку холста (canvas)

    rectangle = Rectangle((4, 4), 5, 3)
    engine.add_figures(rectangle)
    engine.draw()
    assert engine.canvas == []

def test_change_figure_color(engine, capfd): # проверяем смену цвета и отрисовку у одной фигуры
    
    engine.set_color("red")
    rectangle = Rectangle((4, 4), 5, 3)
    rectangle.draw()

    out, err = capfd.readouterr() 
    assert out == "Drawing Rectangle: with top left vertice (4, 4), width 5 and height 3\nColor: red\n"

if __name__ == "__main__":
    pytest.main()

