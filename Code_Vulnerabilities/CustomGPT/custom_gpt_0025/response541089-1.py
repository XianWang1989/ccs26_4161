
import numpy as np
import tensorflow as tf

# Sample data: assume you have a list of sentences.
sentences = [
    "the cat sits on the mat",
    "the dog barks at the cat",
]

# Create a vocabulary and mapping of words to indices
words = set(" ".join(sentences).split())
word_to_index = {word: idx for idx, word in enumerate(words)}
index_to_word = {idx: word for word, idx in word_to_index.items()}

# Prepare training data
def generate_cbow_data(sentences, window_size=1):
    train_inputs = []
    train_labels = []

    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words)):
            # Define context window
            context = []
            for j in range(-window_size, window_size + 1):
                if j != 0 and 0 <= i + j < len(words):
                    context.append(word_to_index[words[i + j]])
            train_inputs.append(context)
            train_labels.append(word_to_index[words[i]])

    return np.array(train_inputs), np.array(train_labels)

train_inputs, train_labels = generate_cbow_data(sentences)

# Define the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)
        self.fc = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        embedded = self.embeddings(inputs)
        return self.fc(tf.reduce_mean(embedded, axis=1))

# Parameters
vocab_size = len(word_to_index)
embedding_dim = 32

# Create the model
model = CBOWModel(vocab_size, embedding_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# To get word embeddings
word_embeddings = model.embeddings.weights[0].numpy()

print("Word embeddings:\n", word_embeddings)
