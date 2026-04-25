
import tensorflow as tf
import numpy as np

# Sample data
# Let's assume we have sentences and we create dummy word indices
sentences = [['the', 'dog', 'barked'], ['the', 'cat', 'meowed']]
word_to_index = {word: i for i, word in enumerate(set(word for sentence in sentences for word in sentence))}

# Prepare training data for CBOW
def prepare_cbow_data(sentences, word_to_index, window_size=1):
    train_inputs = []
    train_labels = []

    for sentence in sentences:
        indices = [word_to_index[word] for word in sentence]
        for i in range(window_size, len(indices) - window_size):
            context = indices[i-window_size:i] + indices[i+1:i+window_size+1]
            target = indices[i]
            train_inputs.append(context)
            train_labels.append(target)
    return np.array(train_inputs), np.array(train_labels)

train_inputs, train_labels = prepare_cbow_data(sentences, word_to_index)

# Define parameters
vocab_size = len(word_to_index)
embedding_dim = 10

# Build CBOW model
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=2 * 1),  # 2 * window_size
    tf.keras.layers.Lambda(tf.reduce_mean),  # Average the embeddings
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
# Let's say we want to predict the target given the context
context_example = np.array([[word_to_index['the'], word_to_index['dog']]])
predicted = model.predict(context_example)
print("Predicted word probabilities:", predicted)
