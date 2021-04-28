from tkinter import *
from collections import OrderedDict


def write_roman(num):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


def sum_supply():
    sum = 0
    for item in list_supply:
        try:
            sum += int(item.get())
            print(item.get())
        except:
            pass
    print()
    return sum


def sum_demand():
    sum = 0
    for item in list_demand:
        try:
            sum += int(item.get())
            print(item.get())
        except:
            pass
    print()
    return sum


def callback():
    global label_sum
    label_sum.config(text=f"{sum_supply()}/{sum_demand()}")


master = Tk()

num_of_sources = 1
num_of_destin = "A"

list_supply = []
list_demand = []


def createGrid(rows, columns):
    global label_sum
    global num_of_sources, num_of_destin
    textMatrix = []

    label = Label(master, font="Helvetica 33 bold", text="Destination")
    label.grid(row=0, column=0, columnspan=columns + 3, padx=5, pady=5)

    label = Label(master, font="Helvetica 33 bold", text="Source", wraplength=1)
    label.grid(row=0, column=0, rowspan=rows + 3, padx=5, pady=5)

    for r in range(1, rows + 2):
        for c in range(1, columns + 2):
            if c == 1 and r != 1:
                label = Label(master, font="Helvetica 25", text=write_roman(num_of_sources))
                label.grid(row=r, column=c, padx=5, pady=5)
                num_of_sources += 1
            if c != 1 and r == 1:
                label = Label(master, font="Helvetica 25", text=num_of_destin)
                label.grid(row=r, column=c, padx=5, pady=5)
                num_of_destin = chr(ord(num_of_destin) + 1)
            # if (r == 0 or c == 0) and not(r == 0 and c == 0):
            #     label = Label(master, font="Helvetica 44 bold", text="Test")
            #     label.grid(row=r, column=c, padx=5, pady=5)

    for r in range(2, rows + 2):
        textRow = []

        for c in range(2, columns + 2):
            variable = StringVar()

            entry = Entry(master, font="Helvetica 25", textvariable=variable, width=3)
            entry.grid(row=r, column=c, padx=5, pady=5)

            textRow.append(variable)

        textMatrix.append(textRow)

    for r in range(2, rows + 2):
        for c in range(columns + 2, columns + 3):
            variable = StringVar()

            entry = Entry(master, font="Helvetica 25", textvariable=variable, width=3, validate="focusout",
                          validatecommand=callback)
            entry.grid(row=r, column=c, padx=5, pady=5)
            list_supply.append(variable)

    for r in range(rows + 2, rows + 3):
        for c in range(2, columns + 2):
            variable = StringVar()

            entry = Entry(master, font="Helvetica 25", textvariable=variable, width=3, validate="focusout",
                          validatecommand=callback)
            entry.grid(row=r, column=c, padx=5, pady=5)
            list_demand.append(variable)

    label_sum = Label(master, font="Helvetica 25", text=f"{sum_supply()}/{sum_demand()}")
    label_sum.grid(row=rows + 2, column=columns + 2, padx=5, pady=5)

    return textMatrix


columns = int(input('Enter number of destinations: '))
rows = int(input('Enter number of sources: '))

num = StringVar()

text_matrix = createGrid(rows, columns)

# Test that we can set all the matrix entries independently

for r in range(rows):
    for c in range(columns):
        text_matrix[r][c].set(r * columns + c)

# for r in range(rows):
#     for c in range(columns):
#         print(text_matrix[r][c], end=" ")
#     print()

label_supply = Label(master, font="Helvetica 12", text="Supply: ")
label_supply.grid(row=1, column=columns + 2, padx=5, pady=5)
label_demand = Label(master, font="Helvetica 12", text="Demand: ")
label_demand.grid(row=rows + 2, column=1, padx=5, pady=5)

# columns + 3
Button(text="Calculate", command="#", font="Helvetica 18").grid(row=rows + 3, column=0, columnspan=columns + 3)

label_NWcorner = Label(master, font="Helvetica 18", text="Northwest Corner Cell: ")
label_NWcorner.grid(row=rows + 4, column=0, columnspan=int((columns + 3) / 2), padx=5, pady=5)

label_LeastCost = Label(master, font="Helvetica 18", text="Least Cost Cell: ")
label_LeastCost.grid(row=rows + 5, column=0, columnspan=int((columns + 3) / 2), padx=5, pady=5)

label_Vogels = Label(master, font="Helvetica 18", text="Vogels Approximation: ")
label_Vogels.grid(row=rows + 6, column=0, columnspan=int((columns + 3) / 2), padx=5, pady=5)

label_NWcorner_ans = Label(master, font="Helvetica 18", text="0")
label_NWcorner_ans.grid(row=rows + 4, column=int((columns + 3) / 2), columnspan=int((columns + 3) / 2), padx=5, pady=5)

label_LeastCost_ans = Label(master, font="Helvetica 18", text="0")
label_LeastCost_ans.grid(row=rows + 5, column=int((columns + 3) / 2), columnspan=int((columns + 3) / 2), padx=5, pady=5)

label_Vogels_ans = Label(master, font="Helvetica 18", text="0")
label_Vogels_ans.grid(row=rows + 6, column=int((columns + 3) / 2), columnspan=int((columns + 3) / 2), padx=5, pady=5)

master.mainloop()
