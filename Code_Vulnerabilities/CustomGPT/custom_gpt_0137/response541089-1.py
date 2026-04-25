
import tensorflow as tf
import numpy as np

# Sample data for the CBOW model
# Input: Context words, Output: Target word
train_inputs = np.array([[1, 2, 3], [4, 5, 6]])  # Example: context words (3 words context)
train_labels = np.array([[0], [2]])               # Example: target words

# Hyperparameters
vocab_size = 10
embedding_dim = 8
learning_rate = 0.01

# Building the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Average the embeddings of the context words
        embedded = self.embeddings(inputs)
        averaged = tf.reduce_mean(embedded, axis=1)
        return self.dense(averaged)

# Instantiate the model, define optimizer and loss function
model = CBOWModel(vocab_size, embedding_dim)
optimizer = tf.keras.optimizers.Adam(learning_rate)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()

# Training the model
model.compile(optimizer=optimizer, loss=loss_fn)

# Train the model with CBOW data
model.fit(train_inputs, train_labels, epochs=100)
