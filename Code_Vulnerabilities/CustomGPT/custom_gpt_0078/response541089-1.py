
import tensorflow as tf
import numpy as np

# Sample data (you would replace this with your actual data)
sentences = [["the", "dog", "barked"], ["the", "cat", "meowed"]]
vocab = {"the": 0, "dog": 1, "barked": 2, "cat": 3, "meowed": 4}
vocab_size = len(vocab)

# Create training inputs and labels
def create_cbow_data(sentences, window_size=1):
    train_inputs = []
    train_labels = []

    for sentence in sentences:
        for i in range(len(sentence)):
            context = []
            target = sentence[i]
            # Collecting context words
            for j in range(-window_size, window_size + 1):
                if j != 0 and 0 <= i + j < len(sentence):
                    context.append(vocab[sentence[i + j]])
            train_inputs.append([vocab[word] for word in context])
            train_labels.append(vocab[target])

    return np.array(train_inputs), np.array(train_labels)

train_inputs, train_labels = create_cbow_data(sentences)

# Build the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embed_dim):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embed_dim)
        self.fc = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        x = self.embedding(inputs)
        x = tf.reduce_mean(x, axis=1)  # Average the embeddings
        return self.fc(x)

# Parameters
embed_dim = 128
model = CBOWModel(vocab_size, embed_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)
