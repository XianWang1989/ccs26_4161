
import tensorflow as tf
import numpy as np

# Assuming you have your vocabulary and the data ready
vocabulary_size = 10000  # Example vocabulary size
embedding_dim = 128      # Size of embedding vector
window_size = 2          # Number of context words

# Define placeholders for input data
train_inputs = tf.placeholder(tf.int32, shape=[None])  # This will be context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # This will be target words

# Define an embedding matrix
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_dim], -1.0, 1.0))

# Lookup the embeddings for the context words
input_embeddings = tf.nn.embedding_lookup(embeddings, train_inputs)

# Mean the context word embeddings
mean_input = tf.reduce_mean(input_embeddings, axis=1)

# Create weights and biases for output layer
output_weights = tf.Variable(tf.random_uniform([vocabulary_size, embedding_dim], -1.0, 1.0))
output_biases = tf.Variable(tf.zeros([vocabulary_size]))

# Compute logits and loss
logits = tf.matmul(mean_input, tf.transpose(output_weights)) + output_biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.reshape(train_labels, [-1]), logits=logits))

# Optimization step
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Train the model in a session
with tf.Session() as session:
    session.run(tf.global_variables_initializer())

    # Dummy input data (for example purposes)
    batch_inputs = np.array([1, 2, 3])  # These would be context word indices
    batch_labels = np.array([[1], [2], [3]])  # These would be target word indices

    # Perform a training step
    feed_dict = {train_inputs: batch_inputs, train_labels: batch_labels}
    _, training_loss = session.run([train_op, loss], feed_dict=feed_dict)

    print(f'Training Loss: {training_loss}')

# Note: This is a simplistic illustration and may need adjustments based on your actual data and preprocessing.
