
import tensorflow as tf
import numpy as np

# Sample data and parameters
vocab_size = 10000  # Size of the vocabulary
embedding_dim = 128  # Dimension of the embedding vector
window_size = 2  # Context window size

# Create the model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)

    def call(self, context_words):
        embedded = self.embeddings(context_words)
        return tf.reduce_mean(embedded, axis=1)

# Prepare training data (input context and output target)
def generate_cbow_data(corpus, window_size):
    data = []
    for i in range(window_size, len(corpus) - window_size):
        context = corpus[i-window_size:i] + corpus[i+1:i+window_size+1]
        target = corpus[i]
        data.append((context, target))
    return data

# Example corpus
corpus = [1, 2, 3, 4, 5]  # Replace with actual word indices
training_data = generate_cbow_data(corpus, window_size)

# Convert data to tensors
train_inputs = np.array([context for context, _ in training_data])
train_labels = np.array([target for _, target in training_data])

# Define the model and compile it
model = CBOWModel(vocab_size, embedding_dim)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(train_inputs, train_labels, epochs=10)
