from openpyxl import load_workbook


class ExcelReader:

    @staticmethod
    def read_login_data(file_path):

        workbook = load_workbook(file_path)

        sheet = workbook.active

        username = sheet["A2"].value
        password = sheet["B2"].value

        workbook.close()

        return username, password