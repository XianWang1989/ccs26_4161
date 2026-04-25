
import numpy as np
import tensorflow as tf

# Sample data (replace it with your dataset)
sentences = [['the', 'cat', 'sat', 'on', 'the', 'mat']]
# Build vocabulary and vectorize the sentences
word_list = list(set([word for sentence in sentences for word in sentence]))
word_to_index = {word: i for i, word in enumerate(word_list)}
index_to_word = {i: word for i, word in enumerate(word_list)}

# Parameters
window_size = 2  # Context window size
embedding_dim = 100  # Dimension of the embedding vector
vocab_size = len(word_list)

# Prepare CBOW training data
train_inputs = []
train_labels = []

for sentence in sentences:
    for i, target in enumerate(sentence):
        context = []
        # Get context words
        for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
            if j != i:  # Exclude the target word
                context.append(word_to_index[sentence[j]])

        # Create training pairs
        train_inputs.append(context)  # Input will be the context
        train_labels.append(word_to_index[target])  # Label will be the target word

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=window_size * 2)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Calculate the embeddings
        x = self.embeddings(inputs)
        x = tf.reduce_mean(x, axis=1)
        return self.dense(x)

# Instantiate and compile the model
model = CBOWModel(vocab_size, embedding_dim)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# To use the model
# model.predict(some_context)
