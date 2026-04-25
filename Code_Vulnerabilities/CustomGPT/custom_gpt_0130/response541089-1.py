
import numpy as np
import tensorflow as tf

# Sample data
# Assume this is your input data where context words are represented
context_words = np.array([[1, 2], [3, 4], [5, 6]])  # Replace with your context word indices
target_words = np.array([[0], [1], [2]])  # Replace with target word indices

# Define parameters
vocab_size = 10  # Define the vocabulary size
embed_size = 5   # Dimensionality of word embeddings

# Define the model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embed_size):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embed_size)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Get embeddings for context words
        embedded = self.embedding(inputs)
        # Average embeddings across the context
        averaged = tf.reduce_mean(embedded, axis=1)
        # Predict the target word
        output = self.dense(averaged)
        return output

# Instantiate the model
model = CBOWModel(vocab_size, embed_size)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(context_words, target_words, epochs=10)

# Example prediction
test_context = np.array([[1, 2]])  # Example context
predicted_word = model.predict(test_context)
print(predicted_word)
