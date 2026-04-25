
import tensorflow as tf
import numpy as np

# Sample training data (context words and target words)
# Assume our vocabulary contains 5 words and we have a very simple dataset.
# Words are represented by integers; for example: "I" = 0, "love" = 1, "Dart" = 2, "and" = 3, "Flutter" = 4
context_words = [[0, 1, 3], [1, 2, 4]]  # Example context words for target words
target_words = [2, 4]  # Actual target words to predict

# Parameters
vocabulary_size = 5
embedding_dim = 2  # Dimensionality of the embedding vectors

# Define inputs and labels
train_inputs = tf.placeholder(tf.int32, shape=[None])   # Context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # One-hot encoded target words

# Create embeddings
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_dim], -1.0, 1.0))
input_embeddings = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average the context word embeddings
average_context = tf.reduce_mean(input_embeddings, axis=1)

# Output layer weights and biases
weights = tf.Variable(tf.random_normal([embedding_dim, vocabulary_size]))
biases = tf.Variable(tf.zeros([vocabulary_size]))

# Logits and prediction
logits = tf.matmul(average_context, weights) + biases
predictions = tf.nn.softmax(logits)

# Loss function and optimizer
cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.reshape(train_labels, [-1]))
loss = tf.reduce_mean(cross_entropy)
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

# Running the session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(1000):
        feed_dict = {train_inputs: np.array(context_words), train_labels: np.array(target_words).reshape(-1, 1)}
        _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)
        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {loss_value}')

# After training, you can use the embeddings for your desired application.
