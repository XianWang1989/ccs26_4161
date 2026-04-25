
import tensorflow as tf
import numpy as np
from collections import Counter
from nltk.tokenize import word_tokenize

# Sample data
text = "I love to learn about machine learning and deep learning."
tokens = word_tokenize(text.lower())
word_count = Counter(tokens)

# Create a vocabulary and word-to-id mapping
vocab = list(word_count.keys())
word_to_id = {word: i for i, word in enumerate(vocab)}
id_to_word = {i: word for i, word in enumerate(vocab)}

# Parameters
window_size = 2
vocab_size = len(vocab)
embedding_dim = 64

# Generate training data for CBOW
def generate_cbow_data(tokens, window_size):
    X = []
    y = []
    for i in range(window_size, len(tokens) - window_size):
        context = []
        for j in range(-window_size, window_size + 1):
            if j != 0:
                context.append(word_to_id[tokens[i + j]])
        X.append(context)
        y.append(word_to_id[tokens[i]])
    return np.array(X), np.array(y)

X, y = generate_cbow_data(tokens, window_size)

# Build the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100)

# Example of how to get word embeddings
embeddings = model.layers[0].get_weights()[0]
print("Word embeddings shape:", embeddings.shape)
