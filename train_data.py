import numpy as np
import matplotlib.pyplot as plt

train_X = np.linspace(-1,1,100)
train_Y = 2*train_X + np.random.randn(*train_X.shape)*0.3
plt.plot(train_X,train_Y,"ro",label = "original data")
plt.legend()
plt.show()
