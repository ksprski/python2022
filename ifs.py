import sys, random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def f_split(matr):
    matr = matr.split('\n')
    matr = [c.split(' ') for c in matr]
    matr = [[float(c) for c in r if c != ''] for r in matr]
    matr = [x for x in matr if x != []]
    return matr


f = open(sys.argv[1], 'r', encoding='utf8')
matr = f.read()
f.close()      

matr = f_split(matr)

fig, ax = plt.subplots()
if sys.argv[1] == "sierpinsky.txt":
        fig.suptitle('Ковер Серпинского')
elif sys.argv[1] == "tree.txt":
        fig.suptitle('Дерево')
elif sys.argv[1] == "fern.txt":
        fig.suptitle('Папоротник Барнсли')              
x, y = [0], [0]
ln, = plt.plot(x, y, 'bo', markersize=1)

def init():
        ax.set_xlim(-0.2, 1.2)
        ax.set_ylim(-0.2, 1)
        return ln,

def animate(j):
        l = len(matr[0])
        r = random.random()
        values = []
        for j in range(l):
                cur_sum = sum(matr[0][:j])
                values.append(cur_sum)
        all_values = values + [1]

        for i in range(1, l + 1):
                if r < all_values[i] and r > all_values[i - 1]:
                        index = i - 1

        cx = matr[1 + index]
        cy = matr[1 + index + l]
        x.append((x[-1]*cx[0] + y[-1]*cx[1] + cx[2]) )
        y.append((x[-1]*cy[0] + y[-1]*cy[1] + cy[2]) )
        ln.set_data(x, y)
        return ln,

ani = FuncAnimation(fig, animate, init_func=init, interval = 0.001)
plt.show()

#python3 ifs.py "fern.txt"
#python3 ifs.py "tree.txt"
#python3 ifs.py "sierpinsky.txt"