
import tensorflow as tf
import numpy as np

# Sample data (example sentences)
sentences = ["word1 word2 word3", "word2 word3 word4"]  # Example word sequences
word_list = list(set(" ".join(sentences).split()))  # Unique words
word_to_id = {word: i for i, word in enumerate(word_list)}
id_to_word = {i: word for i, word in enumerate(word_list)}

# Hyperparameters
embedding_dim = 10
context_size = 1  # number of context words (1-word context)

# Prepare training data for CBOW
def create_dataset(sentences, context_size):
    data = []
    for sentence in sentences:
        words = sentence.split()
        for i in range(context_size, len(words) - context_size):
            context = [words[i - context_size], words[i + context_size]]
            target = words[i]
            data.append((context, target))
    return data

dataset = create_dataset(sentences, context_size)
train_inputs, train_labels = [], []

for context, target in dataset:
    train_inputs.append([word_to_id[word] for word in context])
    train_labels.append(word_to_id[target])

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define the CBOW model
class CBOW(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOW, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)
        self.dense = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        # Get the embeddings for context words
        embedded_inputs = self.embeddings(inputs)
        # Average the embeddings
        context_vector = tf.reduce_mean(embedded_inputs, axis=1)
        # Predict the target word
        logits = self.dense(context_vector)
        return logits

# Instantiate the model
vocab_size = len(word_list)
model = CBOW(vocab_size=vocab_size, embedding_dim=embedding_dim)

# Compile the model
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example of obtaining word vectors
word_vectors = model.embeddings(tf.range(vocab_size))  # Get embeddings for all words
print("Word Vectors: ", word_vectors.numpy())
