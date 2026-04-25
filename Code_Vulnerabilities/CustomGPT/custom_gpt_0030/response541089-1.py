
import numpy as np
import tensorflow as tf

# Sample data: list of sentences
sentences = [["the", "cat", "sat", "on", "the", "mat"],
             ["the", "dog", "sat", "on", "the", "rug"]]

# Create a vocabulary and mapping
vocab = set(word for sentence in sentences for word in sentence)
word_to_id = {word: idx for idx, word in enumerate(vocab)}
id_to_word = {idx: word for word, idx in word_to_id.items()}

# Parameters
embedding_dim = 100
window_size = 2  # Context window
num_samples = 1000  # Number of training samples

# Prepare training data for CBOW
def generate_cbow_data(sentences, window_size):
    inputs = []
    labels = []
    for sentence in sentences:
        sentence_ids = [word_to_id[word] for word in sentence]
        for i in range(len(sentence_ids)):
            context = []
            for j in range(-window_size, window_size + 1):
                if j == 0 or i + j < 0 or i + j >= len(sentence_ids):
                    continue
                context.append(sentence_ids[i + j])
            inputs.append(context)
            labels.append(sentence_ids[i])
    return np.array(inputs), np.array(labels)

train_inputs, train_labels = generate_cbow_data(sentences, window_size)

# Create the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        x = self.embedding(inputs)
        x = tf.reduce_mean(x, axis=1)  # Average embeddings
        return self.dense(x)

# Instantiate and compile the model
model = CBOWModel(vocab_size=len(vocab), embedding_dim=embedding_dim)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=10, batch_size=32)

# Example to get embeddings
word_embeddings = model.embedding(tf.range(len(vocab))).numpy()
