
import tensorflow as tf
import numpy as np

# Sample data preparation
# X: list of context words indices (input)
# Y: list of target word indices (output)
context_words = [
    [0, 1, 2],  # context for target word 3
    [1, 2, 3],  # context for target word 4
]
target_words = [3, 4]  # corresponding target words

# Parameters
vocab_size = 5  # total number of unique words
embedding_dim = 10  # size of the embedding vector

# Build the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=3),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Convert input data to numpy arrays
X = np.array(context_words)  # input context
Y = np.array(target_words)    # target words

# Train the model
model.fit(X, Y, epochs=100)

# To predict a word given a context
sample_context = np.array([[1, 2, 3]])  # example context
predicted = model.predict(sample_context)
predicted_word_index = np.argmax(predicted, axis=1)

print(f"Predicted word index: {predicted_word_index[0]}")
