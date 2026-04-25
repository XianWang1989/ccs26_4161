
import tensorflow as tf
import numpy as np

# Parameters
vocab_size = 10000  # Size of the vocabulary
embedding_dim = 128  # Dimensions of the embeddings
window_size = 2  # Context window size
num_samples = 1000  # Number of training examples

# Generate dummy data
# For simplicity, let's assume we have some pre-processed word indices.
train_inputs = np.random.randint(1, vocab_size, size=(num_samples, window_size))
train_labels = np.random.randint(1, vocab_size, size=(num_samples, 1))

# Create TensorFlow dataset
dataset = tf.data.Dataset.from_tensor_slices((train_inputs, train_labels)).batch(128)

# Model definition
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Average the embeddings of the context words
        embedded = self.embeddings(inputs)
        average_embedding = tf.reduce_mean(embedded, axis=1)
        return self.dense(average_embedding)

# Instantiate the model
model = CBOWModel(vocab_size, embedding_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(dataset, epochs=10)

# Example prediction
# The context words for a new input
example_context = np.array([[5, 9]])  # Replace with actual context word indices
predicted_word = model.predict(example_context)
print("Predicted word probabilities:", predicted_word)
