
import numpy as np
import tensorflow as tf

# Example training data
# train_inputs = [context words] and train_labels = [target word]
train_inputs = np.array([[0, 1, 2], [1, 2, 3]])  # Example context (CBOW)
train_labels = np.array([[2], [3]])              # Example target words

# Define model parameters
vocab_size = 4
embedding_size = 2

# Create the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_size, input_length=3),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model (you can adjust epochs as needed)
model.fit(train_inputs, train_labels, epochs=100)

# Example input to predict target word
test_context = np.array([[1, 2, 3]])
predicted_target = model.predict(test_context)
print("Predicted target word distribution:", predicted_target)
