
import tensorflow as tf
import numpy as np

# Sample data: context and target word
context = [[1, 2], [2, 3]]  # Example context words (input)
target = [0, 1]              # Example target words (label)

# Parameters
vocab_size = 4  # Size of vocabulary
embedding_size = 2  # Dimensionality of embeddings

# Define the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_size)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, context_words):
        # Average the embeddings of context words
        embedded = self.embeddings(context_words)
        avg_embedded = tf.reduce_mean(embedded, axis=1)  # Average pooling
        output = self.dense(avg_embedded)
        return output

# Create the model
model = CBOWModel(vocab_size, embedding_size)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(np.array(context), np.array(target), epochs=10)
