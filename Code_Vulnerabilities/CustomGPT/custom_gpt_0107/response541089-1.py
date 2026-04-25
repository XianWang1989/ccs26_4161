
import tensorflow as tf
import numpy as np

# Sample data: context and target word
context_words = [[0, 1, 2], [0, 2, 3]]  # Example context (words around the target)
target_words = [[1], [2]]                # Corresponding target words

# Parameters
vocab_size = 4  # Size of the vocabulary
embedding_dim = 2  # Dimension of the embedding

# Build the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        embedded = self.embedding(inputs)
        # Average the embeddings for the context words
        average = tf.reduce_mean(embedded, axis=1)
        return self.dense(average)

# Create an instance of the model
model = CBOWModel(vocab_size, embedding_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Prepare data for training
X_train = np.array(context_words)
y_train = np.array(target_words)

# Train the model
model.fit(X_train, y_train, epochs=100)
