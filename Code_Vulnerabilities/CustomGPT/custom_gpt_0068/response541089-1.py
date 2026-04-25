
import numpy as np
import tensorflow as tf

# Development of toy data; in practice, use your own vocabulary/context
vocabulary_size = 5  # Example vocabulary size
embeddings_size = 50  # Size of embedding vectors
num_steps = 10000  # Number of training iterations

# Example input and labels for CBOW (context is input, target is label)
# Suppose you're predicting 'target' from 'context1' and 'context2'
train_inputs = np.array([[0, 1]])  # Replace with the encoded words
train_labels = np.array([[0]])  # Replace with the one-hot encoded target word

# Placeholder for inputs and labels
input_placeholder = tf.placeholder(tf.int32, shape=[None, None])  # Shape for context words
label_placeholder = tf.placeholder(tf.int32, shape=[None, None])  # Shape for target words

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embeddings_size], -1.0, 1.0))
input_vectors = tf.nn.embedding_lookup(embeddings, input_placeholder)

# CBOW model: averaging the input vectors for the context words
mean_input = tf.reduce_mean(input_vectors, axis=1)

# Output layer with softmax
weights = tf.Variable(tf.random_uniform([embeddings_size, vocabulary_size], -1.0, 1.0))
biases = tf.Variable(tf.zeros([vocabulary_size]))
logits = tf.matmul(mean_input, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(label_placeholder)))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

# Training steps
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(num_steps):
        feed_dict = {input_placeholder: train_inputs, label_placeholder: train_labels}
        _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)
        if step % 1000 == 0:
            print(f'Step {step}, Loss: {loss_value}')

    # After training, you can use embeddings.eval() to get the learned word vectors.

