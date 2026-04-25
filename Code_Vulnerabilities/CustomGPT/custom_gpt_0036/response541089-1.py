
import numpy as np
import tensorflow as tf

# Sample data
words = ['I', 'love', 'to', 'learn', 'Python']
word2idx = {word: i for i, word in enumerate(words)}

# Parameters
window_size = 2  # context window size
vocab_size = len(word2idx)

# Generate training data for CBOW
def generate_cbow_data(sentence, window_size):
    training_data = []
    for i, word in enumerate(sentence):
        start = max(0, i - window_size)
        end = min(len(sentence), i + window_size + 1)
        context = []
        for j in range(start, end):
            if j != i:  # Avoid adding the target word itself
                context.append(word2idx[sentence[j]])
        target = word2idx[word]
        training_data.append((context, target))
    return training_data

training_data = generate_cbow_data(words, window_size)

# Convert to TensorFlow Tensors
train_inputs = []
train_labels = []

for context, target in training_data:
    train_inputs.append(context)
    train_labels.append(target)

train_inputs = tf.keras.preprocessing.sequence.pad_sequences(train_inputs)
train_labels = np.array(train_labels)

# Build the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=10, input_length=train_inputs.shape[1]),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Predict example
example_context = np.array([[word2idx['I'], word2idx['love']]])  # Context: 'I' and 'love'
predicted_word_index = model.predict(example_context).argmax()
predicted_word = [word for word, index in word2idx.items() if index == predicted_word_index][0]
print(f"Predicted word for context ['I', 'love']: {predicted_word}")
