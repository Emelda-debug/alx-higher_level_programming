#!/usr/bin/python3
""" creating class BASE """
import json
import csv
import turtle

class Base:
""" class Base with private class attribute  __nb_objects = 0 and class constructor def __init__(self, id=None)"""

__nb_objects = 0

def __init__(self, id=None):
    """ Initialise a new Base
    Args:
    id: int base ID
    """
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects

@staticmethod
def to_json_string(list_dictionaries):
    """ returns the JSON string representation of list_dictionaries:
    Args:
    list_dictionaries: is a list of dictionaries
    """
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)

@classmethod
def save_to_file(cls, list_objs):
    """  writes the JSON string representation of list_objs to a file:
    Args:
    list_objs:  list of instances who inherits of Base
    """
    filename = cls.__name__ + ".json"
    with open(filename, "w") as jsonfile:
        if list_objs is None:
            jsonfile.write("[]")

        else:
            list_dicts = [o.to_dictionary() for o in list_objs]
            jsonfile.write(Base.to_json_string(list_dicts))

@staticmethod
def from_json_string(json_string):
    """ returns the list of the JSON string representation json_string
    Args:
    json_string: is a string representing a list of dictionaries
    """
    if json_string is None:
        return []
    return json.loads(json_string)

@classmethod
def create(cls, **dictionary):
    """ returns an instance with all attributes already set:
    Args:
    ** dictionary: double pointer to a dictionary
    """
    if dictionary and dictionary != {}:
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
            new.update(**dictionary)
            return new

@classmethod
def load_from_file(cls):
    """ Return classes instantiated from a file of JSON strings
    Reads from `<cls.__name__>.json`.
    Returns:
    empty list if the file does not exist
    Otherwise a list of instantiated classes
    """
    filename = str(cls.__name__) + ".json"
    try:
        with open(filename, "r") as jsonfile:
            list_dicts = Base.from_json_string(jsonfile.read())
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

@classmethod
def save_to_file_csv(cls, list_objs):
    """ Write CSV serialization of a list of objects to a file
    Args:
    list_objs: A list of inherited Base instances
    """
    filename = cls.__name__ + ".csv"
    with open(filename, "w", newline="") as csvfile:
        if list_objs is None or list_objs == []:
            csvfile.write("[]")
        else:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

@classmethod
def load_from_file_csv(cls):
    """ Return classes instantiated from a CSV file
    Reads from `<cls.__name__>.csv`
    Returns:
    empty list if the file does not exist
    Otherwise a list of instantiated classes
    """
    filename = cls.__name__ + ".csv"
    try:
        with open(filename, "r", newline="") as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                        for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
            except IOError:
                return []

@staticmethod
def draw(list_rectangles, list_squares):
    """ Draw rectangkes and Squares using the turtle module
    Args:
    list_rectangles: A list of Rectangle objects to draw
    list_squares: A list of Square objects to draw
    """
    turt = turtle.Turtle()
    turt.screen.bgcolor("#ffffff")
    turt.pensize(3)
    turt.shape("turtle")

    turt.color("#000000")
    for rect in list_rectangles:
        turt.showturtle()
        turt.up()
        turt.goto(rect.x, rect.y)
        turt.down()
        for x in range(2):
           turt.forward(rect.width)
           turt.left(90)
           turt.forward(rect.height)
           turt.left(90)
           turt.hideturtle()

        turt.color("#b5e3d8")
        for s in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
           for x in range(2):
               turt.forward(s.width)
               turt.left(90)
               turt.forward(sq.height)
               turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()








