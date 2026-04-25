
import numpy as np
import tensorflow as tf

# Sample data
sentences = [["the", "cat", "sat", "on", "the", "mat"],
             ["the", "dog", "sat", "on", "the", "rug"]]

# Build vocabulary
word_freq = {}
for sentence in sentences:
    for word in sentence:
        word_freq[word] = word_freq.get(word, 0) + 1
vocab = list(word_freq.keys())
word_to_index = {word: i for i, word in enumerate(vocab)}

# Parameters
window_size = 2
embedding_size = 5

# Prepare training data for CBOW
train_inputs = []
train_labels = []

for sentence in sentences:
    for i, word in enumerate(sentence):
        context_words = []
        for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
            if j != i:
                context_words.append(word_to_index[sentence[j]])
        train_inputs.append(context_words)
        train_labels.append(word_to_index[word])

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(vocab), output_dim=embedding_size, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(len(vocab), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example: Get the word embeddings
embeddings = model.layers[0].get_weights()[0]
print(embeddings)
