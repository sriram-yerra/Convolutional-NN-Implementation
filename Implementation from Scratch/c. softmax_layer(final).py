import numpy as numpy

class Softmax:

    def __init__(self, input_len, nodes):
        self.weights = np.random.randn(input_len, nodes)/input_len
        self.biases = np.zeros(nodes)

    def forward(self, input):
        # continue after compleling the NNFS Core Implementation..!