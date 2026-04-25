
import numpy as np
import tensorflow as tf

# Sample data: Assume this is your list of words
words = ['the', 'cat', 'sat', 'on', 'the', 'mat']
# Build a vocabulary and create word-to-index mappings
vocab = set(words)
vocab_size = len(vocab)
word_to_index = {word: i for i, word in enumerate(vocab)}
index_to_word = {i: word for i, word in enumerate(vocab)}

# Generate training data for CBOW
def generate_training_data(words, window_size=2):
    input_data = []
    target_data = []

    for i in range(window_size, len(words) - window_size):
        context = []
        for j in range(-window_size, window_size + 1):
            if j != 0:
                context.append(word_to_index[words[i + j]])
        input_data.append(context)
        target_data.append(word_to_index[words[i]])

    return np.array(input_data), np.array(target_data)

train_inputs, train_labels = generate_training_data(words)

# Define the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.fc = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        embedded = self.embeddings(inputs)
        # Average the embeddings, then pass through the dense layer
        output = tf.reduce_mean(embedded, axis=1)
        return self.fc(output)

# Set hyperparameters
embedding_dim = 10
model = CBOWModel(vocab_size, embedding_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example: Get the inferred word vectors
word_vectors = model.embeddings.weights[0].numpy()

# Print word vectors
for i, word in enumerate(vocab):
    print(f"Word: {word}, Vector: {word_vectors[i]}")
