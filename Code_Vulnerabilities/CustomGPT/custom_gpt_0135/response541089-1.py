
import numpy as np
import tensorflow as tf

# Sample data
sentences = [
    "I love machine learning",
    "Machine learning is amazing",
]
# Preprocess data (tokenization)
tokenized_sentences = [sentence.split() for sentence in sentences]

# Build a vocabulary
word_counts = {}
for sentence in tokenized_sentences:
    for word in sentence:
        word_counts[word] = word_counts.get(word, 0) + 1

vocab = list(word_counts.keys())
word_to_id = {word: i for i, word in enumerate(vocab)}

# CBOW training data preparation
window_size = 2
train_inputs = []
train_labels = []

for sentence in tokenized_sentences:
    for i, target_word in enumerate(sentence):
        context = []
        for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
            if j != i:  # Exclude target word
                context.append(word_to_id[sentence[j]])

        # Prepare the CBOW input (context) and label (target word)
        train_inputs.append(context)
        train_labels.append(word_to_id[target_word])

# Convert to numpy arrays
train_inputs = tf.keras.preprocessing.sequence.pad_sequences(train_inputs, padding='post')
train_labels = np.array(train_labels)

# Create the CBOW model
vocab_size = len(vocab)
embedding_dim = 16

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=train_inputs.shape[1]),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example usage
def predict_word(context):
    context_ids = [word_to_id[word] for word in context]
    context_ids = tf.keras.preprocessing.sequence.pad_sequences([context_ids], padding='post', maxlen=train_inputs.shape[1])
    prediction = model.predict(context_ids)
    return vocab[np.argmax(prediction)]

# Predicting the word given a context
print(predict_word(['I', 'love']))  # Should predict a word in the context of "I love"
