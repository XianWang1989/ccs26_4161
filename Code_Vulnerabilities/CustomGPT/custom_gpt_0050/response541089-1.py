
import tensorflow as tf
import numpy as np

# Sample data
corpus = [
    "the cat sat on the mat",
    "the dog sat on the log"
]

# Preprocess the text
tokenized_sentences = [sentence.split() for sentence in corpus]
word_list = [word for sentence in tokenized_sentences for word in sentence]
vocab = set(word_list)
word2id = {word: idx for idx, word in enumerate(vocab)}
id2word = {idx: word for word, idx in word2id.items()}

# Parameters
window_size = 2
embedding_size = 5

# Prepare training data for CBOW
train_inputs = []
train_labels = []

for sentence in tokenized_sentences:
    for i, target in enumerate(sentence):
        context = []
        # Get context words within the window size
        for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
            if j != i:
                context.append(word2id[sentence[j]])
        train_inputs.append(context)
        train_labels.append(word2id[target])

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Build the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_size)
        self.dense = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Average the embeddings of context words
        x = tf.reduce_mean(self.embeddings(inputs), axis=1)
        return self.dense(x)

# Create and compile model
model = CBOWModel(len(vocab), embedding_size)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example to get embeddings
word_embeddings = model.embeddings(tf.range(len(vocab)))
