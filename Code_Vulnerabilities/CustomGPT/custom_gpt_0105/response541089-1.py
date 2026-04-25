
import tensorflow as tf
import numpy as np

# Sample data (words and their context)
window_size = 2
text = "word2vec is a great technique for word embeddings".split()
word2index = {word: i for i, word in enumerate(set(text))}
index2word = {i: word for word, i in word2index.items()}

# Generate training data
train_inputs = []
train_labels = []

for i in range(window_size, len(text) - window_size):
    context = []
    for j in range(i - window_size, i + window_size + 1):
        if j != i:  # Skip the target word
            context.append(word2index[text[j]])
    train_inputs.append(context)
    train_labels.append(word2index[text[i]])

# Convert input for TF model
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Build the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embed_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embed_dim)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        x = self.embeddings(inputs)
        x = tf.reduce_mean(x, axis=1)  # Average the embeddings
        return self.dense(x)

# Parameters
vocab_size = len(word2index)
embed_dim = 10

# Create and compile the model
model = CBOWModel(vocab_size, embed_dim)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)
