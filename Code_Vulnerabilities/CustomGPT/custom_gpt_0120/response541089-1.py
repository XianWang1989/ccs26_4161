
import tensorflow as tf
import numpy as np

# Sample data: context words and corresponding target words
train_inputs = np.array([[0, 1, 2, 3], [2, 3, 4, 5]])  # example context
train_labels = np.array([[2], [3]])  # example target corresponding to context

# Parameters
vocabulary_size = 6
embedding_size = 8
learning_rate = 0.01

# Define the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embed_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embed_size)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        x = self.embeddings(inputs)
        x = tf.reduce_mean(x, axis=1)  # Average the embeddings
        return self.dense(x)

# Instantiate and compile the model
model = CBOWModel(vocabulary_size, embedding_size)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), 
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
sample_context = np.array([[0, 1, 2, 3]])  # context for prediction
predicted = model.predict(sample_context)
print("Predicted logits for context:", predicted)
