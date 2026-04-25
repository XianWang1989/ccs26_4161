
import tensorflow as tf
import numpy as np

# Sample data: context words and target word
context_words = [['i', 'love'], ['love', 'coding'], ['coding', 'is', 'fun']]
target_words = [['python'], ['javascript'], ['tensorflow']]

# Vocabulary and mapping
vocab = {'i': 0, 'love': 1, 'coding': 2, 'is': 3, 'fun': 4, 'python': 5, 'javascript': 6, 'tensorflow': 7}
vocab_size = len(vocab)

# Prepare training data
train_inputs = []
train_labels = []
for context, target in zip(context_words, target_words):
    train_inputs.append([vocab[word] for word in context])
    train_labels.append([vocab[word] for word in target])

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define model parameters
embedding_size = 8  # Dimension of embedding vector
num_samples = len(train_inputs)

# Build CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_size)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, x):
        # Get embeddings for context words
        embeds = self.embeddings(x)
        # Average embeddings
        average_embed = tf.reduce_mean(embeds, axis=1)
        return self.dense(average_embed)

# Instantiate and compile the model
model = CBOWModel(vocab_size, embedding_size)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
predicted = model.predict(np.array([[vocab['i'], vocab['love']]]))
print(predicted)
