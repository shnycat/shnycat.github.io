import numpy as np
import matplotlib.pyplot as plt
import sys

def m_plot(expr, file_name='plot.svg', label=''):
    x = np.linspace(-6, 6, 1000)

    try:
        y = eval(expr)
    except Exception as e:
        print(f"Error in evaluating expression: {e}")
        return

    plt.plot(x, y)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(label or f'Plot of {expr}')

    plt.savefig(file_name, format='svg')

exp = sys.argv[1]
fn = sys.argv[2]
lbl = sys.argv[3]

m_plot(exp, fn, lbl)
