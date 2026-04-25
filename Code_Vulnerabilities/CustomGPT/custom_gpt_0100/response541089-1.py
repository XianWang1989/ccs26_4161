
import numpy as np
import tensorflow as tf

# Sample data (context words and target word)
context_words = np.array([[1, 2], [3, 4], [5, 6]]) # Example context (two words for each example)
target_words = np.array([0, 1, 1]) # Example target words

# Define vocabulary size and embedding dimensions
vocab_size = 10
embedding_dim = 8

# Create the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Average the embeddings of context words
        x = self.embeddings(inputs)
        x = tf.reduce_mean(x, axis=1)  # Average over context words
        return self.dense(x)

# Instantiate the model
model = CBOWModel(vocab_size, embedding_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(context_words, target_words, epochs=100, verbose=1)
