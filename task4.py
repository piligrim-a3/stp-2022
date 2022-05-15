import openpyxl



def main_account_screen():
    True

if __name__ == '__main__':
    excel_file = openpyxl.load_workbook('school.xlsx')
    sheet = excel_file['Отчёт']

    cells = sheet['A17':'A56']
    count = 1
    for cell in cells:
        print(cell)
        sheet[cell] = str(count)
        count += 1
    # save the file
    excel_file.save(filename="school_result.xlsx")


