
import tensorflow as tf
import numpy as np

# Sample corpus
sentences = ["the cat sat on the mat", "the dog sat on the log"]
words = " ".join(sentences).split()
vocab = set(words)
word_to_index = {word: i for i, word in enumerate(vocab)}
index_to_word = {i: word for i, word in enumerate(vocab)}

# Parameters
embedding_dim = 100
vocab_size = len(vocab)
window_size = 2  # Context window size
num_samples = 10000  # Number of training samples

# Generate training data
train_inputs = []
train_labels = []

for i in range(len(words)):
    context = []
    # Collect context words within the window size
    for j in range(-window_size, window_size + 1):
        if j != 0 and 0 <= i + j < len(words):
            context.append(word_to_index[words[i + j]])
    # Use current word as target
    target = word_to_index[words[i]]
    train_inputs.extend(context)
    train_labels.extend([target] * len(context))

# One-hot encoding the labels
train_labels = tf.keras.utils.to_categorical(train_labels, num_classes=vocab_size)

# CBOW Model
class CBOWModel(tf.keras.Model):
    def __init__(self):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=1)

    def call(self, x):
        x = self.embeddings(x)
        return tf.reduce_mean(x, axis=1)

# Training
model = CBOWModel()
model.compile(optimizer='adam', loss='categorical_crossentropy')

# Prepare inputs as batches
train_inputs = np.array(train_inputs).reshape(-1, 1)  # Reshape for model input
model.fit(train_inputs, train_labels, epochs=10, batch_size=32)

# Retrieve embeddings
word_embeddings = model.embeddings.weights[0].numpy()

# Example: Output the embedding of the word "cat"
print(index_to_word[2], "embedding:", word_embeddings[2])
