
import tensorflow as tf
import numpy as np
import collections

# Sample corpus
corpus = "the quick brown fox jumped over the lazy dog"
words = corpus.split()

# Create word vocabulary and word index
word_counts = collections.Counter(words)
vocabulary = list(word_counts.keys())
vocab_size = len(vocabulary)
word_to_id = {word: idx for idx, word in enumerate(vocabulary)}

# Parameters
embedding_dim = 8
window_size = 2
num_samples = len(words) - window_size * 2

# Prepare training data for CBOW
train_inputs = []
train_labels = []

for i in range(window_size, len(words) - window_size):
    context = []
    for j in range(-window_size, window_size + 1):
        if j != 0:
            context.append(word_to_id[words[i + j]])
    train_inputs.append(context)
    train_labels.append(word_to_id[words[i]])

# Creating the CBOW model
inputs = tf.keras.Input(shape=(window_size * 2,))
embedding = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)(inputs)
average = tf.keras.layers.GlobalAveragePooling1D()(embedding)
outputs = tf.keras.layers.Dense(vocab_size, activation='softmax')(average)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Convert inputs and labels to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Evaluate the model (example)
print(model.predict(np.array([[word_to_id["the"], word_to_id["quick"], word_to_id["brown"], word_to_id["fox"]]])))
