
import tensorflow as tf
import numpy as np

# Sample data: context words and target word
context_words = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Example context words
target_words = [[0], [1], [2]]  # Corresponding target words (one-hot encoded)

# Constants
vocab_size = 10  # Example vocabulary size
embedding_size = 128  # Size of the embedding vector

# Create CBOW model
train_inputs = tf.keras.Input(shape=(None, vocab_size))
train_labels = tf.keras.Input(shape=(vocab_size,))

embeddings = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_size)(train_inputs)
average = tf.keras.layers.GlobalAveragePooling1D()(embeddings)
outputs = tf.keras.layers.Dense(vocab_size, activation='softmax')(average)

model = tf.keras.Model(inputs=train_inputs, outputs=outputs)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Convert your data to the correct format
# Example conversion to one-hot encoding before training
context_words_np = np.array(context_words)
target_words_np = np.array(target_words)

# Fit model (example)
model.fit(context_words_np, target_words_np, epochs=10)

# Note: This example assumes your context and target words are already prepared.
