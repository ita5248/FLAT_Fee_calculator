def reading_previous_values_2():
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
    all_values = []
    with open("fees2.txt", "r") as fee_file:
        for line in fee_file:
            all_values.append(line[:-1].split(';'))
    return all_values
