import random


class DataGenerator:

    FIRST_NAME = "Maria"

    MIDDLE_NAME = "A"

    LAST_NAME = f"QA{random.randint(1000,9999)}"

    @staticmethod
    def first_name():
        return DataGenerator.FIRST_NAME

    @staticmethod
    def middle_name():
        return DataGenerator.MIDDLE_NAME

    @staticmethod
    def last_name():
        return DataGenerator.LAST_NAME