
import tensorflow as tf
import numpy as np

# Sample data
vocab_size = 10000  # Size of vocabulary
embedding_size = 128  # Dimension of embedding vectors
window_size = 2  # The size of context window

# Generate dummy data for training
# Input: context words (window)
train_inputs = np.array([[0, 1], [2, 3], [4, 5]])  # Example context word IDs
# Label: target word
train_labels = np.array([[2], [0], [4]])  # Example target word IDs

# Define the model
input_layer = tf.keras.layers.Input(shape=(window_size,))
embedding_layer = tf.keras.layers.Embedding(vocab_size, embedding_size)(input_layer)
output_layer = tf.keras.layers.Dense(vocab_size, activation='softmax')(tf.reduce_sum(embedding_layer, axis=1))

model = tf.keras.Model(inputs=input_layer, outputs=output_layer)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(train_inputs, train_labels, epochs=10)
