
import tensorflow as tf
import numpy as np
from collections import Counter
from sklearn.preprocessing import OneHotEncoder

# Sample corpus
corpus = [
    "I love to play football",
    "Football is a great sport",
    "I prefer playing basketball",
    "Basketball and football are fun"
]

# Tokenize the text
words = ' '.join(corpus).split()
word_counts = Counter(words)
vocab_size = len(word_counts)
word_to_id = {word: i for i, (word, _) in enumerate(word_counts.items())}
id_to_word = {i: word for word, i in word_to_id.items()}

# CBOW parameters
window_size = 2  # Number of context words
embedding_dim = 10  # Dimension of the embeddings

# Prepare training data
train_inputs = []
train_labels = []

for sentence in corpus:
    tokenized_sentence = sentence.split()
    for i, target_word in enumerate(tokenized_sentence):
        context_words = []
        # Get context words within the window size
        for j in range(max(0, i - window_size), min(len(tokenized_sentence), i + window_size + 1)):
            if j != i:  # Exclude the target word
                context_words.append(word_to_id[tokenized_sentence[j]])

        # Store context as inputs and target as label
        train_inputs.append(context_words)
        train_labels.append(word_to_id[target_word])

# One-hot encoding for labels
encoder = OneHotEncoder(sparse=False)
train_labels_onehot = encoder.fit_transform(np.array(train_labels).reshape(-1, 1))

# Build the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Prepare train inputs: needs to be shaped correctly (batch_size, window_size * 2)
X_train = np.array([np.pad(context, (0, 2*window_size - len(context)), 'constant') for context in train_inputs])

# Train the model
model.fit(X_train, np.array(train_labels_onehot), epochs=100)

# Example of how to use the trained model for predictions
def predict_word(context):
    context_ids = [word_to_id[word] for word in context if word in word_to_id]
    padded_context = np.pad(context_ids, (0, 2*window_size - len(context_ids)), 'constant').reshape(1, -1)
    prediction = model.predict(padded_context)
    predicted_word_id = np.argmax(prediction)
    return id_to_word[predicted_word_id]

# Usage
print(predict_word(["I", "love", "to", "play"]))  # Example context
