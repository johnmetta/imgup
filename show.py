import sys
import numpy as np
import matplotlib.pyplot as plt
import mpldatacursor
from skimage import io

if __name__ == "__main__":
    data = io.imread(sys.argv[1])

    fig, ax = plt.subplots()
    ax.imshow(data, interpolation='none', extent=[0, 1.5*np.pi, 0, np.pi])

    mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'),
                             formatter='i, j = {i}, {j}\nz = {z:.02g}'.format)
    plt.show()
