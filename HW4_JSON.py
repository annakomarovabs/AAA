import json


class ColorizeMixin:
    """Yellow color print"""

    def __repr__(self):
        return f'\033[1;{self.repr_color_code}m {self.title} | {self.price} ₽'


class Advert(ColorizeMixin):
    """Attributes of product"""
    repr_color_code = 33  # yellow

    def __init__(self, dict_):
        for key, value in dict_.items():
            if type(value) == dict:
                value = Advert(value)
            elif key == "class":
                self.__dict__["class_"] = value
            self.__dict__[key] = value
        if "price" in dict_.keys():
            if dict_["price"] < 0:
                raise ValueError("must be >= 0")
        else:
            self.__dict__["price"] = 0


if __name__ == "__main__":
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
    }"""

    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)
    print(lesson_ad.location.address)

    corgi_str = """{
      "title": "Вельш-корги",
      "price": 1000,
      "class": "dogs",
      "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
      }
    }"""

    corgi = json.loads(corgi_str)
    corgi_ad = Advert(corgi)
    print(corgi_ad.class_)

    print(lesson_ad)
    print(corgi_ad)
