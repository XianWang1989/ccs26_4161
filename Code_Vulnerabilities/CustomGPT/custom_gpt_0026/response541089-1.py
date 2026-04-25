
import tensorflow as tf
import numpy as np

# Sample data: a small corpus and preprocessing
sentences = ["the cat sat on the mat", "the dog sat on the log"]
words = [word for sentence in sentences for word in sentence.split()]
vocab = list(set(words))  # Create vocabulary
word_to_id = {word: i for i, word in enumerate(vocab)}

# Parameters
embedding_dim = 10
window_size = 2

# Prepare data for CBOW
def generate_cbow_data(sentences, window_size):
    train_data = []
    for sentence in sentences:
        words = sentence.split()
        for i in range(window_size, len(words) - window_size):
            context = []
            for j in range(i - window_size, i + window_size + 1):
                if j != i:  # Don't include the target word
                    context.append(word_to_id[words[j]])
            target = word_to_id[words[i]]
            train_data.append((context, target))
    return train_data

train_data = generate_cbow_data(sentences, window_size)

# Extract inputs and labels
train_inputs = [data[0] for data in train_data]
train_labels = [data[1] for data in train_data]

# TensorFlow Model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        embedded = self.embedding(inputs)
        avg_embedding = tf.reduce_mean(embedded, axis=1)
        output = self.dense(avg_embedding)
        return output

# Instantiate and compile model
vocab_size = len(vocab)
model = CBOWModel(vocab_size, embedding_dim)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Prepare data for training
train_inputs_array = np.array(train_inputs)
train_labels_array = np.array(train_labels)

# Train the model
model.fit(train_inputs_array, train_labels_array, epochs=100)

# Summary
model.summary()
