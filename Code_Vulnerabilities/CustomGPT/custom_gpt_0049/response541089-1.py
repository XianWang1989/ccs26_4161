
import tensorflow as tf
import numpy as np

# Example corpus
corpus = ["the cat sat on the mat",
          "the dog sat on the log"]

# Prepare data
def create_dataset(corpus, window_size):
    dataset = []
    for sentence in corpus:
        words = sentence.split()
        for i in range(len(words)):
            context = []
            target = words[i]
            for j in range(-window_size, window_size + 1):
                if j != 0 and 0 <= i + j < len(words):
                    context.append(words[i + j])
            dataset.append((context, target))
    return dataset

# Create CBOW dataset
window_size = 2
data = create_dataset(corpus, window_size)

# Build vocabulary
vocab = set(word for context, target in data for word in context) | set(target for context, target in data)
word_to_id = {word: i for i, word in enumerate(vocab)}
id_to_word = {i: word for word, i in word_to_id.items()}

# Parameters
embedding_size = 10
num_words = len(vocab)

# Create CBOW model
class CBOW(tf.keras.Model):
    def __init__(self, num_words, embedding_size):
        super(CBOW, self).__init__()
        self.embedding = tf.keras.layers.Embedding(num_words, embedding_size, input_length=2 * window_size)
        self.dense = tf.keras.layers.Dense(num_words, activation='softmax')

    def call(self, x):
        x = self.embedding(x)
        x = tf.reduce_mean(x, axis=1)
        return self.dense(x)

# Prepare training data
X, y = [], []
for context, target in data:
    X.append([word_to_id[word] for word in context])
    y.append(word_to_id[target])
X = np.array(X)
y = np.array(y)

# Create and compile model
model = CBOW(num_words, embedding_size)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train model
model.fit(X, y, epochs=100)

# Example prediction
example_context = ['the', 'cat']
context_ids = np.array([word_to_id[word] for word in example_context]).reshape(1, -1)
predicted = model.predict(context_ids)
predicted_word_id = np.argmax(predicted)
print(f"Predicted target for context {example_context}: {id_to_word[predicted_word_id]}")
