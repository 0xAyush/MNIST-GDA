import random
import numpy as np

def noise_gen(width,height,intensity):
    space = []
    for i in range(height):
        line = []
        for j in range(width):
            line.append(intensity*(random.random() - 0.5))
        space.append(line)
    return np.array(space)

def noisify(arr,width,height,intensity):
    new_arr = []
    for x in arr:
        ns = noise_gen(width,height,intensity)
        y = np.clip((x + ns),None,1)
        new_arr.append(y)
    return np.array(new_arr)

def noisify2(arr,width,height,intensity):
    new_arr = []
    for x in arr:
        space = []
        for i in range(width):
            line = []
            for j in range(height):
                if random.random() < intensity**4:
                    line.append(2*(random.random() - 0.5))
            space.append(line)
        space = np.array(space)
        y = np.clip((x + space),0,1)
        new_arr.append(y)
    return np.array(new_arr)