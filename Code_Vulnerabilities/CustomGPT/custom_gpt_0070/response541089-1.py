
import tensorflow as tf
import numpy as np

# Define parameters
vocab_size = 10000  # Adjust as needed
embedding_size = 128  # Size of the embedding vectors
window_size = 2  # Number of context words

# Define the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_size)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        x = tf.reduce_mean(self.embeddings(inputs), axis=1)
        return self.dense(x)

# Prepare training data
def generate_data(corpus, window_size):
    data = []
    for i in range(window_size, len(corpus) - window_size):
        context = corpus[i - window_size:i] + corpus[i + 1:i + window_size + 1]
        target = corpus[i]
        data.append((context, target))
    return data

# Example corpus
corpus = [1, 2, 3, 4, 5]  # Replace with your tokenized data
data = generate_data(corpus, window_size)

# Separate inputs and labels
train_inputs, train_labels = zip(*data)

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Model training
model = CBOWModel(vocab_size, embedding_size)
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

# Train the model
model.fit(train_inputs, train_labels, epochs=10)
