
import tensorflow as tf
from tensorflow.keras.layers import Embedding, Dense, Flatten
from tensorflow.keras.models import Sequential
import numpy as np

# Sample data: Let's suppose we have a set of context-target pairs
# Context words are represented as indices
context_indices = np.array([[0, 1, 2], [1, 2, 3]])  # Replace with your actual context indices
target_indices = np.array([3, 4])  # Replace with your actual target indices

# Hyperparameters
vocab_size = 5
embedding_dim = 8

# Build CBOW model
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=3),  # input_length corresponds to the number of context words
    Flatten(),
    Dense(vocab_size, activation='softmax'),
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(context_indices, target_indices, epochs=100)

# The model is now set up for the CBOW approach.
