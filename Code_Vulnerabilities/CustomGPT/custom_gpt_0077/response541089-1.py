
import numpy as np
import tensorflow as tf

# Example data
context = [["the", "cat"], ["the", "dog"]]  # Example context words
targets = ["sits", "barks"]  # Corresponding target words

# Create a simple vocabulary
vocab = set(word for sentence in context + targets for word in sentence)
word_to_id = {word: i for i, word in enumerate(vocab)}
id_to_word = {i: word for word, i in word_to_id.items()}

# Prepare training data
train_inputs = np.array([[word_to_id[word] for word in sentence] for sentence in context])
train_labels = np.array([word_to_id[target] for target in targets])

# Reshape for CBOW: average context words
train_inputs = np.mean(train_inputs, axis=1)  # Average context words for each target

# Define model parameters
embedding_size = 128  # Size of embedding vectors.
learning_rate = 0.001

# Create the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_size)

        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        embedded = self.embeddings(inputs)
        output = self.dense(embedded)
        return output

# Instantiate and compile the model
model = CBOWModel(vocab_size=len(vocab), embedding_size=embedding_size)
model.compile(loss='sparse_categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate))

# Train the model
model.fit(train_inputs, train_labels, epochs=1000)  # Adjust epochs as needed
