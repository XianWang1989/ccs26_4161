
import tensorflow as tf
import numpy as np

# Sample data
words = ["hello", "world", "this", "is", "word2vec"]
word_to_index = {word: i for i, word in enumerate(words)}
index_to_word = {i: word for i, word in enumerate(words)}

# Generate training data
def generate_cbow_data(words, window_size=2):
    training_data = []
    for i in range(window_size, len(words) - window_size):
        context = []
        for j in range(-window_size, window_size + 1):
            if j != 0:
                context.append(word_to_index[words[i + j]])
        target = word_to_index[words[i]]
        training_data.append((context, target))
    return training_data

train_data = generate_cbow_data(words)

# Parameters
vocab_size = len(words)
embedding_size = 2  # Size of the word vectors
batch_size = 1

# Build the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_size, input_length=2)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        embedded = self.embeddings(inputs)
        average = tf.reduce_mean(embedded, axis=1)
        return self.dense(average)

model = CBOWModel(vocab_size, embedding_size)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Prepare the training inputs and labels
train_inputs, train_labels = zip(*train_data)
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
predicted = model.predict(np.array([[1, 2]]))  # Example context of indices
print(index_to_word[np.argmax(predicted)])
