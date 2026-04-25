
import tensorflow as tf
import numpy as np

# Sample data
train_inputs = np.array([[0, 1, 2], [1, 2, 3]])  # Context words as input
train_labels = np.array([[2], [3]])  # Target words to predict

# Parameters
vocabulary_size = 4  # Number of unique words
embedding_size = 2   # Dimension of the embedding
batch_size = 2       # Number of samples per batch
num_steps = 10000    # Training steps

# Placeholders for input and output
inputs = tf.placeholder(tf.int32, shape=[batch_size, 3])  # 3 context words
labels = tf.placeholder(tf.int32, shape=[batch_size, 1])   # 1 target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
input_embeds = tf.nn.embedding_lookup(embeddings, inputs)

# Average the embeddings for context words
context_embeddings = tf.reduce_mean(input_embeds, axis=1)

# Output layer
weights = tf.Variable(tf.random_uniform([embedding_size, vocabulary_size], -1.0, 1.0))
biases = tf.Variable(tf.zeros([vocabulary_size]))

logits = tf.matmul(context_embeddings, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.reshape(labels, [-1]), logits=logits))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train_op = optimizer.minimize(loss)

# Training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(num_steps):
        _, current_loss = sess.run([train_op, loss], feed_dict={inputs: train_inputs, labels: train_labels})
        if step % 1000 == 0:
            print(f'Step {step}, Loss: {current_loss}')
