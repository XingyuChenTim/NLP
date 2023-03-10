import torch
import numpy as np
import matplotlib.pyplot as plt

test_tensor = torch.LongTensor([5, 7])
test_np_array = np.array([5.3,5.8])
plt.scatter(test_tensor[0], test_tensor[1])
plt.annotate("I am a Tensor", test_tensor + 0.05)
plt.scatter(test_np_array[0], test_np_array[1])
plt.annotate("I am an np array", test_np_array + 0.05)
plt.xticks([4, 5, 6])
plt.yticks([5, 6, 7, 8])
plt.show()