distance_to_target = float(input('Enter distance in KM: '))
current_position = 0
step = 0.4
total_steps = 0
while current_position < distance_to_target * 1000:
    current_position += step
    total_steps += 1

print(f'{total_steps} steps')