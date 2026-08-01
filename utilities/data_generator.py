import random


class DataGenerator:

    LAST_NAME = f"QA{random.randint(1000,9999)}"

    @staticmethod
    def first_name():
        return "Maria"

    @staticmethod
    def middle_name():
        return "A"

    @staticmethod
    def last_name():
        return DataGenerator.LAST_NAME