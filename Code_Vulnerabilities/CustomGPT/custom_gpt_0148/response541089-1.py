
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Embedding, Dense, Flatten
from tensorflow.keras.models import Sequential

# Define some parameters
vocab_size = 10000  # Size of your vocabulary
embedding_dim = 128  # Dimension of the embedding vector
window_size = 2  # Context window size

# Sample input data (context words) and labels (target word)
# Using random data for demonstration; replace with your data
context_words = np.random.randint(0, vocab_size, size=(1000, window_size * 2))
target_words = np.random.randint(0, vocab_size, size=(1000, 1))

# Build CBOW model
model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=window_size * 2))
model.add(Flatten())
model.add(Dense(vocab_size, activation='softmax'))

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(context_words, target_words, epochs=10, batch_size=32)

# Save the model
model.save('cbow_model.h5')
