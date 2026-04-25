
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from collections import Counter

# Sample data
text = "Word2Vec is a popular technique for natural language processing."
words = text.lower().split()
word_counts = Counter(words)
vocab = {word: idx for idx, (word, _) in enumerate(word_counts.items())}
vocab_size = len(vocab)

# Prepare training data for CBOW
window_size = 2
train_data = []
for i in range(window_size, len(words) - window_size):
    context = []
    for j in range(-window_size, window_size + 1):
        if j != 0:
            context.append(vocab[words[i + j]])
    target = vocab[words[i]]
    train_data.append((context, target))

# Convert train_data to inputs and labels
train_inputs, train_labels = zip(*train_data)

# Pad sequences (conversion to the same length)
train_inputs = pad_sequences(train_inputs, padding='post')

# Build the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=128, input_length=window_size * 2),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, np.array(train_labels), epochs=100)

# Use the model
word_vec = model.layers[0].get_weights()[0]
print(word_vec)
