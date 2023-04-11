from enum import Enum


class DeclaredUnit(str, Enum):
    liter = "liter"
    kilogram = "kilogram"
    cubic_meter = "cubic meter"
    kilowatt_hour = "kilowatt hour"
    megajoule = "megajoule"
    ton_kilometer = "ton kilometer"
    square_meter = "square meter"
