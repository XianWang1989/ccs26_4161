
import numpy as np
import tensorflow as tf

# Sample data: Let's assume words are mapped to integers
# Here we have a small vocabulary of 5 words
vocab_size = 5
window_size = 2

# Sample training data in the format (context, target)
# For a given target word, we're considering its context words
train_samples = [
    ([1, 2], 3),  # context words: [1, 2], target word: 3
    ([2, 3], 4),  # context words: [2, 3], target word: 4
    ([1, 2], 2)   # context words: [1, 2], target word: 2
]

# Prepare inputs and labels
train_inputs = []
train_labels = []

for context, target in train_samples:
    train_inputs.append(context)
    train_labels.append(target)

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)

    def call(self, inputs):
        # Get embeddings for context words
        context_embeddings = self.embeddings(inputs)
        # Average the context embeddings
        return tf.reduce_mean(context_embeddings, axis=1)

# Parameters
embedding_dim = 8
model = CBOWModel(vocab_size, embedding_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# To see the embeddings
embeddings = model.embeddings.weights[0].numpy()
print("Learned embeddings:\n", embeddings)
