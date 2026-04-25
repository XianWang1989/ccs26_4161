
import numpy as np
import tensorflow as tf

# Sample data: input words (context) and output words (target)
train_inputs = np.array([[0, 1, 2], [1, 2, 3]])  # Replace with your context data
train_labels = np.array([[2], [3]])              # Replace with your target data

# Parameters
vocabulary_size = 4  # Size of your vocabulary
embedding_dimension = 2  # Dimensions for word embeddings

# CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocabulary_size, embedding_dimension):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocabulary_size, embedding_dimension, input_length=3)

    def call(self, inputs):
        x = self.embeddings(inputs)
        x = tf.reduce_mean(x, axis=1)  # Average context word embeddings
        return x

# Create the model
model = CBOWModel(vocabulary_size, embedding_dimension)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(train_inputs, train_labels, epochs=10)

# Example of getting the word embeddings
word_embeddings = model.embeddings.weights[0].numpy()
print("Word Embeddings:\n", word_embeddings)
