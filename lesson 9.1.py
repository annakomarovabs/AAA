from abc import ABS, abstractmethod


class ComputerColor(ABC):

    @abstractmethod
    def __repr__(self):
        return

    @abstractmethod
    def __mul__(self, c):
        return

    @abstractmethod
    def __rmul__(self, c):
        return


class Color(ComputerColor):
    end = '\033[0'
    start = '\033[1;38;2'
    mod = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f'{self.start};{self.red};{self.green};{self.blue}{self.mod}●{self.end}{self.mod}'

    def __repr__(self):
        return f'{self.start};{self.red};{self.green};{self.blue}{self.mod}●{self.end}{self.mod}'

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __add__(self, other):
        return Color(self.red + other.red, self.green + other.green, self.blue + other.blue)

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, c):
        cl = -256*(1-c)
        F = 259*(cl+255)/(255*(259-cl))
        L_red_new = int(F * (self.red - 128) + 128)
        L_green_new = int(F * (self.green - 128) + 128)
        L_blue_new = int(F * (self.blue - 128) + 128)
        new_color = Color(L_red_new, L_green_new, L_blue_new)
        return new_color

    def ___rmul__(self, c):
        return self.__mul__(c)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]

    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


class HSLColor:



if __name__ == '__main__':
    # task
    red = Color(255, 0, 0)
    print(red)
    # task 2
    c1 = Color(255, 0, 0)
    c2 = Color(255, 0, 0)
    c3 = Color(255, 1, 0)
    print(c1 == c2)
    print(c1 == c3)
    # task 3
    green = Color(0, 255, 0)
    print(red + green)
    # task 4
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(color_list)
    print(set(color_list))
    # task 5
    red = Color(255, 0, 0)
    print(red)
    print(red * 0.8)
