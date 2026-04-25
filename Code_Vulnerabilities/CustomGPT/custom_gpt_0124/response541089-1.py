
import numpy as np
import tensorflow as tf

# Parameters
vocab_size = 5000   # Size of the vocabulary
embedding_size = 128  # Size of the embedding vector
window_size = 2     # Context window size
num_sampled = 64    # Number of negative samples
learning_rate = 0.01

# Create the model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_size)
        self.w_b = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Average the embeddings of the context words
        embedded = self.embeddings(inputs)
        context_vector = tf.reduce_mean(embedded, axis=1)
        return self.w_b(context_vector)

# Example data: input is context words, output is target word
train_inputs = np.array([[0, 1, 2], [1, 2, 3]])  # Example context words
train_labels = np.array([[3], [4]])  # Corresponding target words

# Create and compile the model
model = CBOWModel(vocab_size, embedding_size)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=10)

# Example prediction
example_context = np.array([[0, 1, 2]])
predicted_word = model.predict(example_context)
print(predicted_word)
