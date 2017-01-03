import tkinter as tk
from tkinter import ttk


LARGE_FONT = ("Arial", "12")
NORMAL_FONT = ("Arial", "10")
SMALL_FONT = ("Arial", "8")


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "Flat fee calculator")
        tk.Tk.iconbitmap(self, bitmap="flat_fee_icon_tr.ico")

        root = tk.Frame(self)                               # making main window caller root
        root.pack(side="top", fill="both", expand=True)     # packing main window, and that window will fill and expand
        root.grid_rowconfigure(0, weight=1)                 # configure grid of main window?
        root.grid_columnconfigure(0, weight=1)              # configure grid of main window?

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
        change_cost_submenu.add_command(label="Cold water", command=PageOne.change_values_window)
        change_cost_submenu.add_command(label="Hot water", command=quit)
        change_cost_submenu.add_command(label="Gas", command=quit)
        change_cost_submenu.add_command(label="Gas const", command=quit)
        change_cost_submenu.add_command(label="Energy", command=quit)
        change_cost_submenu.add_command(label="Enery const", command=quit)

        self.frames = {}                                    # dictionary with all frames in App

        for frame_class in (StartPage, PageOne):
            frame = frame_class(root, self)
            self.frames[frame_class] = frame           # adding frame start page to frames dict
            frame.grid(row=0, column=0, sticky="nsew")  # putting frame start page it on root grid

        self.show_frame(PageOne)                          # showing frame in method show_frame (give name in dict)

    def show_frame(self, frame_to_show):
        frame = self.frames[frame_to_show]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start page!", font="15", bg="red")
        label.pack()  # (fill="both", expand=True) fill on x or y and expand on while window
        button = ttk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button.pack()


class PageOne(tk.Frame):

    cost_names = ["cold_water_m3",
                  "hot_water_m3",
                  "gas_m3",
                  "gas_const_fee",
                  "energy_kwh",
                  "energy_const_fee"]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, relief="sunken")
        label_page_one = tk.Label(self, text="Page One!", bg="red", font=NORMAL_FONT)
        label_page_one.grid(row=0, column=1)  # (fill="both", expand=True) fill on x or y and expand on while window
        button_to_start_page = ttk.Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))
        button_to_start_page.grid(row=1, column=1)
        label_separator = ttk.Label(self, text="------------------", font=LARGE_FONT)
        label_separator.grid(row=2, column=1)

        self.labels_page_one()
        self.reading_previous_values()

        self.value_names = ["current_cold_water_bathroom_m3",
                            "current_hot_water_bathroom_m3",
                            "current_cold_water_kitchen_m3",
                            "current_hot_water_kitchen_m3",
                            "current_gas_m3",
                            "current_energy_kwh"]
        self.cost_names = ["cold_water_m3",
                           "hot_water_m3",
                           "gas_m3",
                           "gas_const_fee",
                           "energy_kwh",
                           "energy_const_fee"]

    @classmethod
    def change_values_window(cls):
        popup = tk.Tk()
        popup.wm_title("cos")
        label = ttk.Label(popup, text="Change value of: ")
        label.grid(row=0, column=0)
        entry = tk.Entry(popup, width=10)
        entry.grid(row=1, column=0)
        button = ttk.Button(popup, text="Print", command=lambda: print(PageOne.cost_names))
        button.grid(row=2, column=0)

    def labels_page_one(self):

        self.image_c_w = tk.PhotoImage(file="images_to_wge/cold_drop.png").subsample(4, 4)
        label_c_w_b = tk.Label(self, image=self.image_c_w)
        label_c_w_k = tk.Label(self, image=self.image_c_w)
        label_c_w_b.grid(row=4, column=0)
        label_c_w_k.grid(row=6, column=0)

        self.image_h_w = tk.PhotoImage(file="images_to_wge/hot_drop.png").subsample(4, 4)
        label_h_w_b = tk.Label(self, image=self.image_h_w)
        label_h_w_k = tk.Label(self, image=self.image_h_w)
        label_h_w_b.grid(row=5, column=0)
        label_h_w_k.grid(row=7, column=0)

        self.image_g = tk.PhotoImage(file="images_to_wge/gas.png").subsample(4, 4)
        label_g = tk.Label(self, image=self.image_g)
        label_g.grid(row=8, column=0)

        self.image_e = tk.PhotoImage(file="images_to_wge/energy.png").subsample(4, 4)
        label_e = tk.Label(self, image=self.image_e)
        label_e.grid(row=9, column=0)

        # ##----------// CREATING QUANTITY LABELS //----------## #
        column_quantity = 1
        label = ttk.Label(self, text="Quantity: ", font=LARGE_FONT)
        label.grid(row=3, column=column_quantity, sticky="e")
        quantity_list = [u"cold water bathroom [m\u00B3]: ",
                         u"hot water bathroom [m\u00B3]: ",
                         u"cold water kitchen [m\u00B3]: ",
                         u"hot water kitchen [m\u00B3]: ",
                         u"gas [m\u00B3]: ",
                         u"energy [kWh]: "]
        row = 4
        for text_to_show in quantity_list:
            label = ttk.Label(self, text=text_to_show, font=NORMAL_FONT)
            label.grid(row=row, column=column_quantity, sticky="e")
            row += 1
        # ##----------// //----------## #

        # ##----------// CREATING PREVIOUS LABELS //----------## #
        previous_column = 2
        label_previous = ttk.Label(self, text="Previous: ", font=LARGE_FONT)
        label_previous.grid(row=3, column=2, sticky="")
        self.previous_values_list = []
        for i in range(6):
            self.previous_values_list.append(tk.DoubleVar())
        row = 4
        for value in self.previous_values_list:
            label = ttk.Label(self, textvariable=value, font=NORMAL_FONT)
            label.grid(row=row, column=previous_column, sticky="")
            row += 1
        # ##----------// //----------## #

        # ##----------// CREATING ACTUAL VALUES LABELS //----------## #
        actual_column = 3
        label_actual = ttk.Label(self, text="Actual: ", font=LARGE_FONT)
        label_actual.grid(row=3, column=actual_column, sticky="nse")
        self.actual_values_list = []
        for i in range(6):
            self.actual_values_list.append(tk.DoubleVar())
        row = 4
        for value in self.actual_values_list:
            entry = tk.Entry(self, textvariable=value, width=10)
            entry.grid(row=row, column=actual_column, sticky="")
            row += 1
        # ##----------// //----------## #

        # ##----------// CREATING DIFFERENCE LABELS //----------## #
        difference_column = 4
        label_difference = ttk.Label(self, text="Difference: ", font=LARGE_FONT)
        label_difference.grid(row=3, column=difference_column, sticky="nse")
        self.difference_values_list = []
        for i in range(6):
            self.difference_values_list.append(tk.DoubleVar())

        row = 4
        for value in self.difference_values_list:
            label = ttk.Label(self, textvariable=value, font=NORMAL_FONT)
            label.grid(row=row, column=difference_column, sticky="")
            row += 1
        # ##----------// //----------## #

        # ##----------// CREATING CALCULATIONS TEXT LABELS //----------## #
        calculations_column = 5
        self.label_calculations = ttk.Label(self, text="Calculations: ", font=LARGE_FONT)
        self.label_calculations.grid(row=3, column=calculations_column, sticky="")
        self.total_cost = ttk.Label(self, text="Total cost: ", font=LARGE_FONT)
        self.total_cost.grid(row=10, column=calculations_column, sticky="")

        self.calculation_text_list = []
        for i in range(6):
            self.calculation_text_list.append(tk.StringVar())
        row = 4
        for text_to_show in self.calculation_text_list:
            label = ttk.Label(self, textvariable=text_to_show, font=NORMAL_FONT, width=25, anchor="e")
            label.grid(row=row, column=calculations_column, sticky="e")
            row += 1
        # ##----------// //----------## #

        # ##----------// CREATING COST LABELS //----------## #
        cost_column = 6
        label_cost = ttk.Label(self, text="Cost: ", font=LARGE_FONT)
        label_cost.grid(row=3, column=cost_column, sticky="nse")
        self.calculation_cost_value_list = []
        for i in range(7):
            self.calculation_cost_value_list.append(tk.DoubleVar())
        row = 4
        for text_to_show in self.calculation_cost_value_list:
            label = ttk.Label(self, textvariable=text_to_show, font=NORMAL_FONT)
            label.grid(row=row, column=cost_column, sticky="")
            row += 1
        # ##----------// //----------## #

        # ##----------// CREATING UNIT COST LABELS //----------## #
        column_unit_cost = 1
        label_cost_separator = ttk.Label(self, text="")
        label_cost_separator.grid(row=10, column=1, sticky="e")
        label_unit_price = ttk.Label(self, text="Unit cost: ", font=LARGE_FONT)
        label_unit_price.grid(row=11, column=1, sticky="e")
        unit_price_list = [u"cold water [m\u00B3]: ",
                           u"hot water [m\u00B3]: ",
                           u"gas [m\u00B3]: ",
                           "gas const: ",
                           "energy [kWh]: ",
                           "energy const: "]
        row = 12
        for text_to_show in unit_price_list:
            label = ttk.Label(self, text=text_to_show)
            label.grid(row=row, column=column_unit_cost, sticky="e")
            row += 1
        # ##----------// //----------## #

        # ##----------// CREATING ACTUAL COST LABELS //----------## #
        actual_cost_column = 2
        self.actual_cost_list = []
        for i in range(6):
            self.actual_cost_list.append(tk.DoubleVar())

        row = 12
        for value in self.actual_cost_list:
            label = ttk.Label(self, textvariable=value)
            label.grid(row=row, column=actual_cost_column, sticky="")
            row += 1
        # ##----------// //----------## #

        calculate_button = ttk.Button(self, text="Calculate", command=self.calculating_difference)
        calculate_button.grid(row=10, column=difference_column)
        save_button = ttk.Button(self, text="Save to file", command=self.sting_saving_to_file)
        save_button.grid(row=12, column=difference_column, rowspan=3, columnspan=3, sticky="W")

    def reading_previous_values(self):
        """
        Loading from file
        Loads 11 pieces of data in following order:
        0 - current_cold_water_bathroom_m3
        1 - current_hot_water_bathroom_m3
        2 - current_cold_water_kitchen_m3
        3 - current_hot_water_kitchen_m3
        4 - current_gas_m3
        5 - current_energy_kwh
        6 - cold_water_m3
        7 - hot_water_m3
        8 - gas_m3
        9 - gas_const_fee
        10 - energy_kwh
        11 - energy_const_fee
        """
        fee_file = open("fees.txt", "r")
        input_fee_data = fee_file.readlines()
        input_fee_pairs = []
        input_fee_values = []
        self.how_many_entries = (len(input_fee_data))

        for line in input_fee_data:
            input_fee_pairs.append(line.strip("\n").split(";"))

        for i, pairs in enumerate(input_fee_pairs):
            input_fee_values.append([])
            for pair in pairs:
                input_fee_values[i].append((pair.split(",")))
        fee_file.close()

        self.previous_values_list[0].set(input_fee_values[-1][0][1])
        self.previous_values_list[1].set(input_fee_values[-1][1][1])
        self.previous_values_list[2].set(input_fee_values[-1][2][1])
        self.previous_values_list[3].set(input_fee_values[-1][3][1])
        self.previous_values_list[4].set(input_fee_values[-1][4][1])
        self.previous_values_list[5].set(input_fee_values[-1][5][1])
        self.actual_cost_list[0].set(input_fee_values[-1][6][1])
        self.actual_cost_list[1].set(input_fee_values[-1][7][1])
        self.actual_cost_list[2].set(input_fee_values[-1][8][1])
        self.actual_cost_list[3].set(input_fee_values[-1][9][1])
        self.actual_cost_list[4].set(input_fee_values[-1][10][1])
        self.actual_cost_list[5].set(input_fee_values[-1][11][1])

        return input_fee_values

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
        string = ""
        for i in range(6):
            string += self.value_names[i] + "," + str(self.calculation_cost_value_list[i].get()) + ";"
        for i in range(6):
            string += self.cost_names[i] + "," + str(self.actual_cost_list[i].get()) + ";"
        string += "\n"
        return string

        """
        difference_cold_water_bathroom_m3_to_pass = self.actual_values_list[0].get() - self.previous_values_list[0].get()
        difference_cold_water_bathroom_m3_to_pass = round(difference_cold_water_bathroom_m3_to_pass, 3)
        self.difference_values_list[0].set(difference_cold_water_bathroom_m3_to_pass)

        difference_hot_water_bathroom_m3_to_pass = self.actual_values_list[1].get() - self.previous_values_list[1].get()
        difference_hot_water_bathroom_m3_to_pass = round(difference_hot_water_bathroom_m3_to_pass, 3)
        self.difference_values_list[1].set(difference_hot_water_bathroom_m3_to_pass)

        difference_cold_water_kitchen_m3_to_pass = self.actual_values_list[2].get() - self.previous_values_list[2].get()
        difference_cold_water_kitchen_m3_to_pass = round(difference_cold_water_kitchen_m3_to_pass, 3)
        self.difference_values_list[2].set(difference_cold_water_kitchen_m3_to_pass)

        difference_hot_water_kitchen_m3_to_pass = self.actual_values_list[3].get() - self.previous_values_list[3].get()
        difference_hot_water_kitchen_m3_to_pass = round(difference_hot_water_kitchen_m3_to_pass, 3)
        self.difference_values_list[3].set(difference_hot_water_kitchen_m3_to_pass)

        difference_gas_m3_to_pass = self.actual_values_list[4].get() - self.previous_values_list[4].get()
        difference_gas_m3_to_pass = round(difference_gas_m3_to_pass, 3)
        self.difference_values_list[4].set(difference_gas_m3_to_pass)

        difference_energy_kwh_value = self.actual_values_list[5].get() - self.previous_values_list[5].get()
        difference_energy_kwh_value = round(difference_energy_kwh_value, 3)
        self.difference_values_list[5].set(difference_energy_kwh_value)
        """

    def sting_saving_to_file(self):
        fee_file = open("fees.txt", "a")
        fee_file.write(self.string_to_write_creating())
        fee_file.close()
        self.reading_previous_values()

fee_calculator = Application()
fee_calculator.mainloop()

