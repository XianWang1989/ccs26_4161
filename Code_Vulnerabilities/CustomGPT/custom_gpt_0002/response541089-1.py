
import numpy as np
import tensorflow as tf

# Prepare data (example input and output)
train_inputs = np.array([[0, 1, 2, 3]]).T  # Context words
train_labels = np.array([[1], [2], [3], [4]])  # Target words

# Define the model
vocabulary_size = 5
embedding_size = 128

# Input and output layers
inputs = tf.keras.layers.Input(shape=(1,))
embeddings = tf.keras.layers.Embedding(vocabulary_size, embedding_size)(inputs)
output = tf.keras.layers.Dense(vocabulary_size, activation='softmax')(embeddings)

# Build and compile model
model = tf.keras.models.Model(inputs=inputs, outputs=output)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(train_inputs[:, 1], train_labels, epochs=100)
