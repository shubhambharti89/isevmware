import openpyxl as xl


def Read_Onboard_Sheet(File_Name,index):
    wb= xl.load_workbook(File_Name)
    sheet = wb["ISE"]
    return sheet

def numberofvm(sheet):

    rows = sheet.max_row
    vmcount = rows-1

    return vmcount

def gethostname(sheet,vmcount):

    rows = vmcount+2
    column = 1
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list
        static_variable.append(sheet.cell(row=i, column=column).value)
    return static_variable

def getesxiname(sheet,vmcount):

    rows = vmcount + 2
    column = 3
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list
        static_variable.append(sheet.cell(row=i, column=column).value)
    return static_variable

def getdsname(sheet,vmcount):

    rows = vmcount + 2
    column = 5
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list
        static_variable.append(sheet.cell(row=i, column=column).value)
    return static_variable

def getdcname(sheet, vmcount):

    rows = vmcount + 2
    column = 6
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list
        static_variable.append(sheet.cell(row=i, column=column).value)
    return static_variable

def getcpu(sheet, vmcount):

    cpu = [6,8,8,8,12,12]
    rows = vmcount + 2
    column = 2
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list

        if sheet.cell(row=i, column=column).value == 3515:
            static_variable.append(cpu[0])
        if sheet.cell(row=i, column=column).value == 3555:
            static_variable.append(cpu[1])
        if sheet.cell(row=i, column=column).value == 3595:
            static_variable.append(cpu[2])
        if sheet.cell(row=i, column=column).value == 3615:
            static_variable.append(cpu[3])
        if sheet.cell(row=i, column=column).value == 3655:
            static_variable.append(cpu[4])
        if sheet.cell(row=i, column=column).value == 3695:
            static_variable.append(cpu[5])

    return static_variable

def getmemory(sheet, vmcount):

    memory = [16000, 32000, 64000, 32000, 96000, 256000]
    rows = vmcount + 2
    column = 2
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list

        if sheet.cell(row=i, column=column).value == 3515:
            static_variable.append(memory[0])
        if sheet.cell(row=i, column=column).value == 3555:
            static_variable.append(memory[1])
        if sheet.cell(row=i, column=column).value == 3595:
            static_variable.append(memory[2])
        if sheet.cell(row=i, column=column).value == 3615:
            static_variable.append(memory[3])
        if sheet.cell(row=i, column=column).value == 3655:
            static_variable.append(memory[4])
        if sheet.cell(row=i, column=column).value == 3695:
            static_variable.append(memory[5])

    return static_variable

def getdisk(vmcount):
    disk = [200, 200, 2400, 2400, 600, 600]
    rows = vmcount + 2
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list
        static_variable.append(disk[i-2])
    return static_variable

def getguestver(sheet, vmcount):

    memory = ["vmx-13", "vmx-14", "vmx-15", "vmx-17"]
    rows = vmcount + 2
    column = 4
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list

        if sheet.cell(row=i, column=column).value == 6.5:
            static_variable.append(memory[0])
        if sheet.cell(row=i, column=column).value == 6.7:
            static_variable.append(memory[1])
        if sheet.cell(row=i, column=column).value == 6.8:
            static_variable.append(memory[2])
        if sheet.cell(row=i, column=column).value == 7.0:
            static_variable.append(memory[3])

    return static_variable

def getisods(sheet):

    column = 7
    row = 2
    static_variable = sheet.cell(row=row, column=column).value

    return static_variable

def getisofile(sheet):
    column = 8
    row = 2
    static_variable = sheet.cell(row=row, column=column).value

    return static_variable

def getnetwork1(sheet,vmcount):
    rows = vmcount + 2
    column = 9
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list
        static_variable.append(sheet.cell(row=i, column=column).value)
    return static_variable

def getnetwork2(sheet,vmcount):
    rows = vmcount + 2
    column = 10
    static_variable = []
    for i in range(2, rows):
        # reading cell value from source excel file and put it in a list
        static_variable.append(sheet.cell(row=i, column=column).value)
    return static_variable
