
import tensorflow as tf
import numpy as np

# Sample data: context (input) and target (label) words
# Assume we have a vocabulary of 10 words and a mapping for them
word_to_id = {f'word{i}': i for i in range(10)}
id_to_word = {i: f'word{i}' for i in range(10)}

# Example context (input) and target (label)
context = [word_to_id['word0'], word_to_id['word1']]
target = [word_to_id['word2']]

# Hyperparameters
embedding_dim = 8
vocab_size = len(word_to_id)

# Model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, context_words):
        embedded = self.embeddings(context_words)
        embedding_mean = tf.reduce_mean(embedded, axis=1)
        return self.dense(embedding_mean)

# Training Setup
model = CBOWModel(vocab_size, embedding_dim)
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam()

# Training Step
@tf.function
def train_step(context, target):
    with tf.GradientTape() as tape:
        predictions = model(context)
        loss = loss_object(target, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss

# Example training loop
context_input = np.array([[context]])  # Reshape for batch size
target_input = np.array(target)

for epoch in range(100):  # Number of training epochs
    loss = train_step(context_input, target_input)
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.numpy()}')

# The model is now trained for the CBOW task
