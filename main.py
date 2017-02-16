import tkinter as tk
from tkinter import ttk
import datetime

LARGE_FONT = ("Arial", "12")
NORMAL_FONT = ("Helvetica", "10")
SMALL_FONT = ("Arial", "8")


class Application(tk.Tk):

    def __init__(self):
        # inherit all attributes from Tk
        tk.Tk.__init__(self)
        # make title and icon
        tk.Tk.title(self, "Flat fee calculator")
        tk.Tk.iconbitmap(self, bitmap="flat_fee_icon_tr.ico")

        # in main window create root Frame in witch all frames will be shown later
        root = tk.Frame(self)
        # pack it, this is only one object in this window
        root.pack(side="top", fill="both")

        top_menu_bar = tk.Menu(self)
        self.config(menu=top_menu_bar)

        file_top_menu_bar = tk.Menu(top_menu_bar, tearoff=0)
        top_menu_bar.add_cascade(label="File", menu=file_top_menu_bar)
        file_top_menu_bar.add_separator()
        file_top_menu_bar.add_command(label="Quit", command=quit)

        edit_top_menu_bar = tk.Menu(top_menu_bar, tearoff=0)  # create edit menu in top menu bar
        top_menu_bar.add_cascade(label="Edit", menu=edit_top_menu_bar)  # adding edit menu to top menu bar
        change_cost_submenu = tk.Menu(edit_top_menu_bar, tearoff=0)   # create change cost menu  in edit menu
        edit_top_menu_bar.add_separator()
        edit_top_menu_bar.add_cascade(label="Change cost", menu=change_cost_submenu, underline=0)  # add change menu
        change_cost_submenu.add_command(label="Cold water", command=lambda: self.change_values(0))
        change_cost_submenu.add_command(label="Hot water", command=lambda: self.change_values(1))
        change_cost_submenu.add_command(label="Gas", command=lambda: self.change_values(2))
        change_cost_submenu.add_command(label="Gas const", command=lambda: self.change_values(3))
        change_cost_submenu.add_command(label="Energy", command=lambda: self.change_values(4))
        change_cost_submenu.add_command(label="Energy const", command=lambda: self.change_values(5))

        # create dictionary with frames, where key: value is PageClass: created_frame
        self.frames = {}

        # from all defined classes create frames with master as root and main_class as self,
        # with is this class - Application (self)
        # also, put it in the grid and add to dictionary
        for frame_class in (PageOne, PageTwo):
            frame = frame_class(root, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[frame_class] = frame

        # show the PageOne as fisrt thing to show on start
        self.show_frame(PageOne)

    # this is definition for showing the frame, we pass PageClass, then pick already
    # made class from dictionary and treat it with tkraise method
    def show_frame(self, frame_to_show):
        frame = self.frames[frame_to_show]
        frame.tkraise()

    def change_values(self, cost_index):
        popup = tk.Tk()
        popup.geometry("200x100")
        popup.wm_title("Cost change")
        label = ttk.Label(popup, text="Change value of: {}".format(self.frames[PageOne].unit_price_list[cost_index]))
        label.grid(row=0, column=0, sticky="WE")
        entry = tk.Entry(popup, width=10)
        entry.grid(row=1, column=0)
        button = ttk.Button(popup, text="Change", command=lambda: change_chosen_value())
        button.grid(row=2, column=0, sticky="WENS")

        def change_chosen_value():
            new_value = entry.get()
            self.frames[PageOne].actual_cost_list[cost_index].set(new_value)


class PageOne(tk.Frame):

    def __init__(self, master, main_class):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text='Page One', width=10)
        label.grid(row=0, column=0)
        button_style = ttk.Style()
        button_style.configure('button.TButton', foreground='green', font=NORMAL_FONT)
        button = ttk.Button(self, style='button.TButton', text='Go to Page Two', command=lambda: main_class.show_frame(PageTwo))
        button.grid(row=0, column=1)

        self.labels_page_one()
        self.reading_previous_values()
        self.setting_previous_values()

    def labels_page_one(self):

        # ##----------//      CREATING ICONS      //----------## #
        column_icons = 0
        row_icons = 3
        image_list = ['images_to_wge/cold_drop.png',
                      'images_to_wge/hot_drop.png',
                      'images_to_wge/cold_drop.png',
                      'images_to_wge/hot_drop.png',
                      'images_to_wge/gas.png',
                      'images_to_wge/energy.png']

        for image in image_list:
            icon = tk.PhotoImage(file=image).subsample(4, 4)
            label = ttk.Label(self, image=icon)
            label.image = icon  # keep a reference!
            label.grid(row=row_icons, column=column_icons, sticky='E')
            row_icons += 1
        # ##----------// ------------------------ //----------## #

        # ##----------// CREATING QUANTITY LABELS //----------## #
        column_quantity = 1
        row_quantity = 3
        label = ttk.Label(self, text="Quantity: ", font=LARGE_FONT)
        label.grid(row=2, column=column_quantity, sticky="E")

        quantity_list = [u"cold water bathroom [m\u00B3]: ",
                         u"hot water bathroom [m\u00B3]: ",
                         u"cold water kitchen [m\u00B3]: ",
                         u"hot water kitchen [m\u00B3]: ",
                         u"gas [m\u00B3]: ",
                         u"energy [kWh]: "]

        for text_to_show in quantity_list:
            label = ttk.Label(self, text=text_to_show, font=NORMAL_FONT)
            label.grid(row=row_quantity, column=column_quantity, sticky="E")
            row_quantity += 1
        # ##----------// //----------## #

        # ##----------// CREATING PREVIOUS LABELS //----------## #
        column_previous = 2
        row_previous = 3
        label_previous = ttk.Label(self, text="Previous: ", font=LARGE_FONT)
        label_previous.grid(row=2, column=column_previous, sticky="E")

        self.previous_values_list = []
        for i in range(6):
            self.previous_values_list.append(tk.DoubleVar())

        for value in self.previous_values_list:
            label = ttk.Label(self, textvariable=value, font=NORMAL_FONT)
            label.grid(row=row_previous, column=column_previous, sticky="")
            row_previous += 1
        # ##----------// //----------## #

        # ##----------// CREATING ACTUAL VALUES LABELS //----------## #
        column_actual = 3
        row_actual = 3
        label_actual = ttk.Label(self, text="Actual: ", font=LARGE_FONT)
        label_actual.grid(row=2, column=column_actual, sticky="E")

        self.actual_values_list = []
        for i in range(6):
            self.actual_values_list.append(tk.DoubleVar())

        for value in self.actual_values_list:
            entry = tk.Entry(self, textvariable=value, width=10)
            entry.grid(row=row_actual, column=column_actual, sticky="")
            row_actual += 1
        # ##----------// //----------## #

        # ##----------// CREATING DIFFERENCE LABELS //----------## #
        column_difference = 4
        row_difference = 3
        label_difference = ttk.Label(self, text="Difference: ", font=LARGE_FONT)
        label_difference.grid(row=2, column=column_difference, sticky="E")

        self.difference_values_list = []
        for i in range(6):
            self.difference_values_list.append(tk.DoubleVar())

        for value in self.difference_values_list:
            label = ttk.Label(self, textvariable=value, font=NORMAL_FONT)
            label.grid(row=row_difference, column=column_difference, sticky="")
            row_difference += 1
        # ##----------// //----------## #

        # ##----------// CREATING CALCULATIONS TEXT LABELS //----------## #
        column_calculations = 5
        row_calculations = 3
        self.label_calculations = ttk.Label(self, text="Calculations: ", font=LARGE_FONT)
        self.label_calculations.grid(row=2, column=column_calculations, sticky="")
        self.total_cost = ttk.Label(self, text="Total cost: ", font=LARGE_FONT)
        self.total_cost.grid(row=9, column=column_calculations, sticky="")

        self.calculation_text_list = []
        for i in range(6):
            self.calculation_text_list.append(tk.StringVar())

        for text_to_show in self.calculation_text_list:
            label = ttk.Label(self, textvariable=text_to_show, font=NORMAL_FONT, width=25, anchor="e")
            label.grid(row=row_calculations, column=column_calculations, sticky="e")
            row_calculations += 1
        # ##----------// //----------## #

        # ##----------// CREATING COST LABELS //----------## #
        column_cost = 6
        row_cost = 3
        label_cost = ttk.Label(self, text="Cost: ", font=LARGE_FONT)
        label_cost.grid(row=2, column=column_cost, sticky="nse")

        self.calculation_cost_value_list = []
        for i in range(7):
            self.calculation_cost_value_list.append(tk.DoubleVar())

        for text_to_show in self.calculation_cost_value_list:
            label = ttk.Label(self, textvariable=text_to_show, font=NORMAL_FONT)
            label.grid(row=row_cost, column=column_cost, sticky="")
            row_cost += 1
        # ##----------// //----------## #

        # ##----------// CREATING UNIT COST LABELS //----------## #
        column_unit_cost = 1
        row_unit_cost = 10
        label_cost_separator = ttk.Label(self, text="")
        label_cost_separator.grid(row=10, column=1, sticky="e")
        label_unit_price = ttk.Label(self, text="Unit cost: ", font=LARGE_FONT)
        label_unit_price.grid(row=11, column=1, sticky="e")
        self.unit_price_list = [u"cold water [m\u00B3]: ",
                           u"hot water [m\u00B3]: ",
                           u"gas [m\u00B3]: ",
                           "gas const: ",
                           "energy [kWh]: ",
                           "energy const: "]

        for text_to_show in self.unit_price_list:
            label = ttk.Label(self, text=text_to_show)
            label.grid(row=row_unit_cost, column=column_unit_cost, sticky="e")
            row_unit_cost += 1
        # ##----------// //----------## #

        # ##----------// CREATING ACTUAL COST LABELS //----------## #
        column_actual_cost = 2
        row_actual_cost = 10

        self.actual_cost_list = []
        for i in range(6):
            self.actual_cost_list.append(tk.DoubleVar())

        for value in self.actual_cost_list:
            label = ttk.Label(self, textvariable=value)
            label.grid(row=row_actual_cost, column=column_actual_cost, sticky="")
            row_actual_cost += 1
        # ##----------// //----------## #

        calculate_button = ttk.Button(self, text="Calculate", command=self.calculating_difference)
        calculate_button.grid(row=11, column=5, rowspan=2, sticky="WENS")
        save_button = ttk.Button(self, text="Save to file", command=self.string_saving_to_file)
        save_button.grid(row=13, column=6, rowspan=2, sticky="WENS")

    def reading_previous_values(self):
        """
        Loading from file
        Loads 11 pieces of data in following order:
        0 - date
        1 - current_cold_water_bathroom_m3
        2 - current_hot_water_bathroom_m3
        3 - current_cold_water_kitchen_m3
        4 - current_hot_water_kitchen_m3
        5 - current_gas_m3
        6 - current_energy_kwh
        7 - cold_water_m3
        8 - hot_water_m3
        9 - gas_m3
        10 - gas_const_fee
        11 - energy_kwh
        12 - energy_const_fee
        """
        self.all_values = []
        with open("fees2.csv", "r") as fee_file:
            last_line = fee_file.readlines()[-1]
            self.all_values = last_line.strip().split(';')
        return self.all_values

    def setting_previous_values(self):
        for i in range(6):
            self.previous_values_list[i].set((self.all_values[1:])[i])
            self.actual_cost_list[i].set((self.all_values[1:])[i+6])

    def calculating_difference(self):
        """
        1. calculate difference, which is float entry (actual) minus previous (already DoubleVar)
        2. nes we round calculated difference to 3 digit after coma
        3. assign rounded number to difference to display it
        """
        total_cost = 0
        for i in range(6):
            difference = self.actual_values_list[i].get() - self.previous_values_list[i].get()
            difference = round(difference, 3)
            self.difference_values_list[i].set(difference)
            if i == 0:
                self.calculation_text_list[i].set(str(difference)+" * "+str(self.actual_cost_list[0].get())+" = ")
                cost = round(difference*self.actual_cost_list[0].get(), 2)
                self.calculation_cost_value_list[i].set(cost)
            elif i == 1:
                self.calculation_text_list[i].set(str(difference) + " * (" + str(self.actual_cost_list[0].get())+ " + " + str(self.actual_cost_list[1].get()) + ") = ")
                cost = round(difference * (self.actual_cost_list[0].get()+self.actual_cost_list[1].get()), 2)
                self.calculation_cost_value_list[i].set(cost)
            elif i == 2:
                self.calculation_text_list[i].set(str(difference) + " * " + str(self.actual_cost_list[0].get()) + " = ")
                cost = round(difference * self.actual_cost_list[0].get(), 2)
                self.calculation_cost_value_list[i].set(cost)
            elif i == 3:
                self.calculation_text_list[i].set(str(difference) + " * (" + str(self.actual_cost_list[0].get()) + " + " + str(self.actual_cost_list[1].get()) + ") = ")
                cost = round(difference * (self.actual_cost_list[0].get()+self.actual_cost_list[1].get()), 2)
                self.calculation_cost_value_list[i].set(cost)
            elif i == 4:
                self.calculation_text_list[i].set(str(difference) + " * " + str(self.actual_cost_list[2].get()) + " + " + str(self.actual_cost_list[3].get()) + " = ")
                cost = round(difference * self.actual_cost_list[2].get() + self.actual_cost_list[3].get(), 2)
                self.calculation_cost_value_list[i].set(cost)
            elif i == 5:
                self.calculation_text_list[i].set(str(difference) + " * " + str(self.actual_cost_list[4].get()) + " + " + str(self.actual_cost_list[5].get()) + " = ")
                cost = round(difference * self.actual_cost_list[4].get() + self.actual_cost_list[5].get(), 2)
                self.calculation_cost_value_list[i].set(cost)
            total_cost += cost
        total_cost = round(total_cost, 2)
        self.calculation_cost_value_list[6].set(total_cost)

    def string_to_write_creating(self):
        string = '\n' + '.'.join(str(datetime.date.today()).split('-')[::-1]) + ' ; '

        for i in range(6):
            string += str(self.actual_values_list[i].get()) + ' ; '
        for i in range(6):
            string += str(self.actual_cost_list[i].get()) + ' ; '
        string = string[:-2]
        return string

    def string_saving_to_file(self):
        with open("fees2.csv", "a") as fee_file:
            fee_file.write(self.string_to_write_creating())
        self.reading_previous_values()
        self.setting_previous_values()





class PageTwo(tk.Frame):
    """
    For now, let's leave it empty
    """
    def __init__(self, master, main_class):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text='Page Two', width=50)
        label.pack()
        button = tk.Button(self, text='Go to Page One', command=lambda: main_class.show_frame(PageOne))
        button.pack()

if __name__ == '__main__':
    fee_calculator = Application()
    fee_calculator.mainloop()
