
import tensorflow as tf
import numpy as np

# Sample data
context_words = [[0, 1, 2], [1, 2, 3]]  # Example context words (indices)
target_words = [3, 4]  # Example target words corresponding to the contexts

# Parameters
vocab_size = 5  # Size of your vocabulary
embedding_dim = 2  # Dimension of embedding

# Create TensorFlow model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)

    def call(self, context):
        # Average the embeddings of context words
        embedded = self.embeddings(context)
        return tf.reduce_mean(embedded, axis=1)

# Instantiate model
model = CBOWModel(vocab_size, embedding_dim)

# Define loss and optimizer
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()

# Training loop
for epoch in range(100):  # Number of epochs
    with tf.GradientTape() as tape:
        predictions = model(np.array(context_words))
        loss = loss_fn(np.array(target_words), predictions)

    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    print(f'Epoch {epoch}, Loss: {loss.numpy()}')
