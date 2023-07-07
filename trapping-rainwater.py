def trap_rainwater(blocks):
    n = len(blocks)
    left_max = [0] * n
    right_max = [0] * n
    trapped_water = 0
    
    # Find the maximum height of walls on the left side of each block
    left_max[0] = blocks[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], blocks[i])
    
    # Find the maximum height of walls on the right side of each block
    right_max[n-1] = blocks[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], blocks[i])
    
    # Calculate the trapped water for each block and add it to the total trapped water variable
    for i in range(n):
        water_above_block = min(left_max[i], right_max[i]) - blocks[i]
        if water_above_block > 0:
            trapped_water += water_above_block
    
    return trapped_water

print(trap_rainwater([6, 8, 8]))