
import tensorflow as tf
import numpy as np

# Sample data for demonstration
sentences = [['the', 'dog', 'barks'], ['the', 'cat', 'meows']]
vocab = set(word for sentence in sentences for word in sentence)
word_to_id = {word: idx for idx, word in enumerate(vocab)}
id_to_word = {idx: word for word, idx in word_to_id.items()}

# Create training data for CBOW
window_size = 1
train_inputs = []
train_labels = []

for sentence in sentences:
    for i in range(window_size, len(sentence) - window_size):
        context = [word_to_id[sentence[i - window_size]], word_to_id[sentence[i + window_size]]]
        label = word_to_id[sentence[i]]

        train_inputs.append(context)
        train_labels.append(label)

train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define model parameters
vocab_size = len(vocab)
embed_size = 10

# Build the CBOW model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embed_size):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embed_size)
        self.fc = tf.keras.layers.Dense(vocab_size, activation='softmax')

    def call(self, inputs):
        # Average the embeddings for context words
        x = self.embeddings(inputs)
        x = tf.reduce_mean(x, axis=1)
        return self.fc(x)

# Instantiate and compile the model
model = CBOWModel(vocab_size, embed_size)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example usage
def predict(word):
    word_id = word_to_id[word]
    context = np.array([[word_id]]).reshape(1, -1)  # Reshape for the model
    predicted = model.predict(context)
    predicted_word_id = np.argmax(predicted)
    return id_to_word[predicted_word_id]

# Predict the next word given context
print(predict('the'))  # Example to predict based on context
