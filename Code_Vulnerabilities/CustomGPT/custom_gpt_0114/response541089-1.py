
import tensorflow as tf
import numpy as np

# Sample data
# Let's assume you have these predefined
train_data = [...]  # Your input data (context words)
train_labels = [...]  # Your target data (target word)

# Parameters
vocab_size = 10000  # Size of vocabulary
embedding_dim = 128  # Dimension of the embedding vectors
batch_size = 64  # Number of training examples per batch
num_steps = 10000  # Number of training steps

# Create TensorFlow graph
graph = tf.Graph()
with graph.as_default():
    # Variables
    embeddings = tf.Variable(tf.random.uniform([vocab_size, embedding_dim], -1.0, 1.0))
    inputs = tf.placeholder(tf.int32, shape=[batch_size])
    labels = tf.placeholder(tf.int32, shape=[batch_size, 1])

    # Look up embeddings for inputs
    embed = tf.nn.embedding_lookup(embeddings, inputs)

    # Train logits
    logit = tf.layers.dense(embed, vocab_size)

    # Loss function and optimizer
    loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logit, labels=tf.reshape(labels, [-1]))
    optimizer = tf.train.AdagradOptimizer(learning_rate=0.1).minimize(loss)

# Training the model
with tf.Session(graph=graph) as session:
    tf.global_variables_initializer().run()

    for step in range(num_steps):
        # Fetch your training batch (reversed inputs and labels for CBOW)
        input_batch, label_batch = fetch_batch()  # Define how to fetch a batch

        feed_dict = {inputs: input_batch, labels: label_batch}
        _, l = session.run([optimizer, loss], feed_dict=feed_dict)

        if step % 1000 == 0:
            print(f'Loss at step {step}: {l}')

# Remember to save your embeddings after training
