
import numpy as np
import tensorflow as tf

# Sample data for CBOW
train_inputs = np.array([[0, 1, 2], [1, 2, 3]])  # context words
train_labels = np.array([[3], [4]])  # target words

# Parameters
vocab_size = 5
embedding_dim = 64
num_sampled = 1  # Number of negative examples to sample

# Define the input placeholders
inputs = tf.placeholder(tf.int32, shape=[None, 3])  # Context size 3
labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target size 1

# Define the embeddings matrix
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))

# Look up embeddings for inputs
input_embeddings = tf.nn.embedding_lookup(embeddings, inputs)

# CBOW: average embedding for context words
average_embedding = tf.reduce_mean(input_embeddings, axis=1)

# Define the weights and biases for the output layer
weights = tf.Variable(tf.random_normal([vocab_size, embedding_dim]))
biases = tf.Variable(tf.zeros([vocab_size]))

# Compute logits
logits = tf.matmul(average_embedding, tf.transpose(weights)) + biases

# Loss function and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(labels)))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Training process
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(1000):
        _, l = sess.run([optimizer, loss], feed_dict={inputs: train_inputs, labels: train_labels})
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {l}")

    # To retrieve the trained word vectors
    trained_embeddings = sess.run(embeddings)
    print("Trained Embeddings:", trained_embeddings)
