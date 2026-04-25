
import numpy as np
import tensorflow as tf

# Sample data (context and target words)
context_words = [...]
target_words = [...]

# Parameters
vocab_size = len(vocab)  # Your vocabulary size
embedding_size = 128     # Size of the embedding vector
window_size = 2          # Size of context window

# Build the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_size)

    def call(self, context):
        # Average embeddings of context words
        embedded = self.embedding(context)
        return tf.reduce_mean(embedded, axis=1)

# Create the model
model = CBOWModel(vocab_size, embedding_size)

# Define the loss and optimizer
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()

# Training loop
def train(model, context_words, target_words, epochs=10):
    for epoch in range(epochs):
        for context, target in zip(context_words, target_words):
            with tf.GradientTape() as tape:
                predictions = model(context)
                loss = loss_fn(target, predictions)
            gradients = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(gradients, model.trainable_variables))
            print(f"Epoch {epoch+1}, Loss: {loss.numpy()}")

# Example call to train
# context_words should be a list of lists of indices representing context words
# target_words should be a list of indices representing target words
train(model, context_words, target_words)
