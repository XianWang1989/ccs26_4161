
import tensorflow as tf
import numpy as np

# Sample data preparation
def generate_data(corpus, window_size):
    train_inputs, train_labels = [], []
    for sentence in corpus:
        words = sentence.split()
        for i, word in enumerate(words):
            context_words = [words[j] for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)) if j != i]
            for context in context_words:
                train_inputs.append(context)
                train_labels.append(word)
    return train_inputs, train_labels

# Parameters
window_size = 2
corpus = ["the quick brown fox jumps", "over the lazy dog"]
train_inputs, train_labels = generate_data(corpus, window_size)

# Create vocabulary
vocab = list(set(train_inputs + train_labels))
vocab_size = len(vocab)
word_to_id = {word: i for i, word in enumerate(vocab)}

# Encode input and labels
encoded_inputs = np.array([word_to_id[word] for word in train_inputs])
encoded_labels = np.array([word_to_id[word] for word in train_labels])

# Build the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embed = tf.keras.layers.Embedding(vocab_size, embedding_dim)

    def call(self, inputs):
        embeddings = self.embed(inputs)
        return tf.reduce_mean(embeddings, axis=1)

# Hyperparameters
embedding_dim = 100
model = CBOWModel(vocab_size, embedding_dim)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(encoded_inputs, encoded_labels, epochs=50)

# Example: Getting embeddings for a word
word_embedding = model.embed(word_to_id['quick']).numpy()
print(word_embedding)
