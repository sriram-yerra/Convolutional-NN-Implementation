from tensorflow.keras import Sequential
from tensorflow.kera.layers import Conv2D, MaxPooling2D, Dense, Flatten

# Loading Dataset
X_train = np.loadtxt('train_input.csv', delimiter = ',')
Y_train = np.loadtxt('train_labels.csv', delimiter = ',')

X_test = np.loadtxt('test_input.csv', delimiter = ',')
Y_test = np.loadtxt('test_labels.csv', delimiter = ',')

print(X_train.shape)
print(Y_train.Y_test)
print(X_test.Y_test)
print(Y_test.Y_test)

