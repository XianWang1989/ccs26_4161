
import numpy as np
import tensorflow as tf

# Example parameters
vocab_size = 10000  # Size of the vocabulary
embedding_size = 128  # Dimension of the embedding
window_size = 2  # Context window size

# Sample training data (context words and target words)
context_words = [[1, 2], [2, 3], [3, 4]]  # Example context (input)
target_words = [0, 1, 2]  # Example target (output)

# Define the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_size)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, context):
        embedded = self.embeddings(context)
        # Average the embeddings for the CBOW context
        averaged = tf.reduce_mean(embedded, axis=1)
        return self.dense(averaged)

# Instantiate the model
model = CBOWModel(vocab_size, embedding_size)

# Compile the model with loss function and optimizer
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Prepare the data for training
context_words = np.array(context_words)  # Shape (num_samples, window_size)
target_words = np.array(target_words)  # Shape (num_samples,)

# Train the model
model.fit(context_words, target_words, epochs=100)

# Example output
context_input = np.array([[1, 2]])
predicted_probs = model.predict(context_input)
predicted_word = np.argmax(predicted_probs)
print(f"Predicted word index: {predicted_word}")
