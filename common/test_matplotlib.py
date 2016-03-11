#################################################
# matplotlib use
# Author : gdanskamir
# Date   : 2016-02-18
# HomePage : http://www.cnblogs.com/gdanskamir
#################################################

from numpy import *
import matplotlib.pyplot as plt


x_label = [];
y_label = [];


i = 0.1;
while i <= 10:
    x_label.append(i);
    y_label.append(-1.0 * math.log(i) + i - 1);

    i = i + 0.001;

plt.figure()
plt.plot(x_label, y_label, label="$-ln(x)+x-1$", color="red");
plt.xlabel("x_label")
plt.ylabel("y_label")
plt.title("-ln(x)+x-1")
plt.xlim(-0.5, 10.5);
plt.legend();
plt.savefig('./test.png', format="png");


