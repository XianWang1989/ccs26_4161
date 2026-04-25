
import numpy as np
import tensorflow as tf

# Sample training data
# Each word will be represented as an index
# For example: "the quick brown fox jumps"
#                       0      1    2   3    4
train_inputs = np.array([1, 2, 3])  # Context words
train_labels = np.array([0])         # Target word (the word to predict)

# Parameters
vocabulary_size = 4
embedding_size = 2  # Size of the embedding vector

# Create the model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embed_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embed_size)

    def call(self, inputs):
        embed = self.embeddings(inputs)
        return tf.reduce_mean(embed, axis=1)  # Average of context words

# Create CBOW model
model = CBOWModel(vocabulary_size, embedding_size)
model.build((None, 3))  # Input shape (batch_size, number_of_context_words)

# Define loss and optimizer
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()

# Training step
@tf.function
def train_step(inputs, labels):
    with tf.GradientTape() as tape:
        predictions = model(inputs)
        loss = loss_object(labels, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss

# Example training loop
for epoch in range(100):
    loss = train_step(train_inputs.reshape(1, -1), train_labels)
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.numpy()}')

# The CBOW model can now be used to predict target words based on context words.
