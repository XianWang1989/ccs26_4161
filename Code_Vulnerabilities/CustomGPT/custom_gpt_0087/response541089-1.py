
import tensorflow as tf
import numpy as np

# Sample data
words = ["I", "love", "to", "learn", "deep", "learning"]
window_size = 2

# Create vocabulary and word to index mapping
vocab = set(words)
word_to_index = {word: i for i, word in enumerate(vocab)}
index_to_word = {i: word for i, word in enumerate(vocab)}
vocab_size = len(vocab)

# Prepare training data for CBOW
train_inputs = []
train_labels = []
for i in range(window_size, len(words) - window_size):
    context = [words[i - window_size], words[i + window_size]]
    target = words[i]
    train_inputs.append([word_to_index[w] for w in context])
    train_labels.append(word_to_index[target])

# Convert to NumPy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define CBOW model
embedding_dim = 10

# Create the model
class CBOW_Model(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOW_Model, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        embedded = self.embedding(inputs)
        return self.dense(tf.reduce_mean(embedded, axis=1))

# Initialize and compile the model
model = CBOW_Model(vocab_size, embedding_dim)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)
