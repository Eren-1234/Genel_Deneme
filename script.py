import csv

data_block_values = {
    'Data_block_1_int_pompa': 123,
    'Data_block_1_int_vana': 456,
    'Data_block_1_real_havuz': 78.9,
    'Data_block_1_vana_man': True,
    'Data_block_1_vana_start': False
}

with open('data_block_values.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Tag Name', 'Value'])
    for key, value in data_block_values.items():
        writer.writerow([key, value])
