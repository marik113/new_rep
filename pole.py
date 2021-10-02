import time

from class_pole import *

np = Pole(30, 30)
u1 = Unit(2)
np.add_unit(u1, 18, 13)
np.show()
u1.go_unit("right")
u1.go_unit("right")
u1.go_unit("right")
u1.go_unit("right")
time.sleep(3)
np.show()
input()
