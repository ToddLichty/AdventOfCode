def read_input(file):
    with open(file) as f:
        lines = f.read()
    
    return str(lines)

program_input = read_input('./2019/data/day_8.in')

layers = []
for _ in range(0, int(len(program_input) / 150)):
    layers.append(program_input[_ * 150:(_+1) * 150])

num_zeros = 9999999999999999
min_zero_layer = ''

for layer in layers:
    if layer.count('0') < num_zeros:
        num_zeros = layer.count('0')
        min_zero_layer = layer


print(min_zero_layer.count('1') * min_zero_layer.count('2'))
    
