def reading_previous_values():
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
    #fee_file = open("fees2.txt", "r")
    #input_fee_data = fee_file.readlines()[1:]  # line 0 is header
    values = []

    with open("fees2.txt", "r") as fee_file:
        for line in fee_file:
            values.append(line[:-1].split(';'))


    input_fee_pairs = []
    input_fee_values = []
    # self.how_many_entries = (len(input_fee_data))

    # for line in input_fee_data:
    #     input_fee_pairs.append(line.strip("\n").split(";"))
    #
    # for i, pairs in enumerate(input_fee_pairs):
    #     input_fee_values.append([])
    #     for pair in pairs:
    #         input_fee_values[i].append((pair.split(",")))

    print(values)
    # previous_values_list[0].set(input_fee_values[-1][0][1])
    # previous_values_list[1].set(input_fee_values[-1][1][1])
    # previous_values_list[2].set(input_fee_values[-1][2][1])
    # previous_values_list[3].set(input_fee_values[-1][3][1])
    # previous_values_list[4].set(input_fee_values[-1][4][1])
    # previous_values_list[5].set(input_fee_values[-1][5][1])
    # actual_cost_list[0].set(input_fee_values[-1][6][1])
    # actual_cost_list[1].set(input_fee_values[-1][7][1])
    # actual_cost_list[2].set(input_fee_values[-1][8][1])
    # actual_cost_list[3].set(input_fee_values[-1][9][1])
    # actual_cost_list[4].set(input_fee_values[-1][10][1])
    # actual_cost_list[5].set(input_fee_values[-1][11][1])

    return input_fee_values

reading_previous_values()
