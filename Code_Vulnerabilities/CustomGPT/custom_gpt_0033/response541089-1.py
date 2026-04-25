
import tensorflow as tf
import numpy as np

# Sample data
train_inputs = np.array([[0, 1], [1, 2], [2, 3]])  # Context words (two words at a time)
train_labels = np.array([[1], [2], [3]])            # Target words

# Parameters
vocab_size = 4
embedding_size = 2

# Create the model
class CBOW(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOW, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_size)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Get embeddings for context words and average them
        embedded = self.embeddings(inputs)
        avg_embedded = tf.reduce_mean(embedded, axis=1)
        return self.dense(avg_embedded)

# Initialize the model
model = CBOW(vocab_size, embedding_size)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=1000)

# Example prediction
predictions = model.predict(np.array([[0, 1], [1, 2]]))
print(predictions)
