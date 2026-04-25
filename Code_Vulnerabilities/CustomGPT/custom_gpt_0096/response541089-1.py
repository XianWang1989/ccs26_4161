
import tensorflow as tf
import numpy as np

# Sample data preparation (example)
# Suppose we have the following sentences
sentences = ["the cat sits on the mat", "the dog sits on the log"]
words = [word for sentence in sentences for word in sentence.split()]
word_set = set(words)
word_to_index = {word: index for index, word in enumerate(word_set)}
vocab_size = len(word_set)

# Function to create training data
def create_training_data(sentences, window_size=2):
    train_inputs = []
    train_labels = []
    for sentence in sentences:
        word_list = sentence.split()
        for i, word in enumerate(word_list):
            # Extract context words
            context = []
            for j in range(max(0, i-window_size), min(len(word_list), i+window_size+1)):
                if i != j:
                    context.append(word_to_index[word_list[j]])
            # The target word
            target = word_to_index[word]
            train_inputs.append(context)
            train_labels.append(target)
    return np.array(train_inputs), np.array(train_labels)

# Create training data
train_inputs, train_labels = create_training_data(sentences)

# Prepare the CBOW model using TensorFlow
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.fc = tf.keras.layers.Dense(vocab_size)

    def call(self, inputs):
        # Average the embeddings for context words
        x = self.embedding(inputs)
        x = tf.reduce_mean(x, axis=1)
        return self.fc(x)

# Parameters
embedding_dim = 8
model = CBOWModel(vocab_size, embedding_dim)

# Model compilation
model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

# Train the model
model.fit(train_inputs, train_labels, epochs=10)

# Example usage of model
context_vector = np.array([[word_to_index['the'], word_to_index['cat'], word_to_index['sits']]])
predicted_word = model.predict(context_vector)
print("Predicted word:", predicted_word)
