
import tensorflow as tf
import numpy as np

# Sample data (dummy example)
sentences = [["the", "cat", "sat", "on", "the", "mat"],
             ["the", "dog", "sat", "on", "the", "rug"]]

# Build vocabulary and create word-to-index mapping
vocab = set(word for sentence in sentences for word in sentence)
word_to_index = {word: i for i, word in enumerate(vocab)}
index_to_word = {i: word for word, i in word_to_index.items()}

# Hyperparameters
embedding_dim = 10
window_size = 2  # Context size for CBOW
num_samples = 1000
num_words = len(vocab)

# Prepare training data for CBOW
train_inputs = []
train_labels = []

for sentence in sentences:
    for i, word in enumerate(sentence):
        # Define the context (window of words around the target word)
        context = []
        for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
            if j != i:
                context.append(word_to_index[sentence[j]])
        train_inputs.append(context)
        train_labels.append(word_to_index[word])

# Creating the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=num_words, output_dim=embedding_dim, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(num_words, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Convert inputs and labels to numpy arrays
train_inputs = tf.keras.preprocessing.sequence.pad_sequences(train_inputs)
train_labels = np.array(train_labels)

# Train the model
model.fit(train_inputs, train_labels, epochs=100, verbose=1)
