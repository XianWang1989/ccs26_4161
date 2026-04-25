
import tensorflow as tf
import numpy as np

# Sample data
sentences = [['the', 'dog', 'barked'], ['the', 'cat', 'meowed']]
vocab = list(set(word for sentence in sentences for word in sentence))
vocab_size = len(vocab)

# Create mapping from words to index
word_to_index = {word: i for i, word in enumerate(vocab)}

# Generate training data
def generate_cbow_data(sentences, window_size=1):
    train_inputs = []
    train_labels = []
    for sentence in sentences:
        indices = [word_to_index[word] for word in sentence]
        for i in range(len(indices)):
            context = []
            for j in range(max(0, i - window_size), min(len(indices), i + window_size + 1)):
                if j != i:  # Exclude the target word
                    context.append(indices[j])
            train_inputs.append(context)
            train_labels.append(indices[i])
    return np.array(train_inputs), np.array(train_labels)

train_inputs, train_labels = generate_cbow_data(sentences)

# Create the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=None)

    def call(self, inputs):
        # Average the embeddings for the context words
        emb = self.embedding(inputs)
        # Return the average of the context word embeddings
        return tf.reduce_mean(emb, axis=1)

# Hyperparameters
embedding_dim = 10
model = CBOWModel(vocab_size, embedding_dim)

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Access the embedding layer weights
embeddings = model.embedding.weights[0].numpy()
