
import tensorflow as tf
import numpy as np
from collections import Counter

# Sample data
data = "the cat sat on the mat"
data = data.split()

# Create vocabulary and mappings
vocab = Counter(data)
word_to_id = {word: i for i, (word, _) in enumerate(vocab.items())}
id_to_word = {i: word for word, i in word_to_id.items()}

# CBOW parameters
window_size = 2
num_words = len(vocab)

# Prepare training data
train_inputs = []
train_labels = []

for i in range(window_size, len(data) - window_size):
    context = data[i-window_size:i] + data[i+1:i+window_size+1]
    target = data[i]
    train_inputs.append([word_to_id[word] for word in context])
    train_labels.append(word_to_id[target])

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Create TensorFlow model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.fc = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        embedded = self.embedding(inputs)
        average = tf.reduce_mean(embedded, axis=1)
        return self.fc(average)

# Initialize and compile model
embedding_dim = 16
model = CBOWModel(num_words, embedding_dim)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)
