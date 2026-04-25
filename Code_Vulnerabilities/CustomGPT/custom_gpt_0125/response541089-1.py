
import tensorflow as tf
import numpy as np

# Parameters
vocab_size = 10000
embedding_dim = 128
window_size = 2

# Input data
train_inputs = np.array([[1, 2], [3, 4], [5, 6]])
train_labels = np.array([[0], [1], [2]])

# CBOW Model
class CBOWModel(tf.keras.Model):
    def __init__(self):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, x):
        x = self.embeddings(x)
        x = tf.reduce_mean(x, axis=1)  # Average the embeddings
        return self.dense(x)

# Training the model
model = CBOWModel()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(train_inputs, train_labels, epochs=10)
