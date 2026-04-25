
import tensorflow as tf
import numpy as np

# Sample data: context (input words) and target (predicted word)
context_words = np.array([[0, 1, 2], [1, 2, 3]])  # Example context words
target_words = np.array([2, 3])  # Corresponding target words

# Parameters
vocab_size = 5
embedding_dim = 128

# CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        embedded = self.embeddings(inputs)
        # Use mean of embeddings for context predictions
        mean_embedded = tf.reduce_mean(embedded, axis=1)
        return self.dense(mean_embedded)

# Create the model
model = CBOWModel(vocab_size, embedding_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(context_words, target_words, epochs=100, verbose=1)
