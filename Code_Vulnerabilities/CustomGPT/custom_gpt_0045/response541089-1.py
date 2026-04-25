
import tensorflow as tf
import numpy as np

# Define parameters
vocab_size = 10000  # size of the vocabulary
embedding_size = 128  # dimensionality of the embedding
window_size = 3  # context window size
num_sampled = 64  # negative samples

# Input data - list of words as indices
train_inputs = np.array([1, 2, 3, 4])  # Example input word indices (context)
train_labels = np.array([0, 1, 2, 3])  # Target word (will reverse in CBOW)

# Create embeddings
embeddings = tf.Variable(tf.random.uniform([vocab_size, embedding_size], -1.0, 1.0))

# CBOW Model: We take the context words, average their embeddings, and try to predict the target word
def cbow_model(inputs):
    context_embeddings = tf.nn.embedding_lookup(embeddings, inputs)
    avg_context_embedding = tf.reduce_mean(context_embeddings, axis=0)
    return avg_context_embedding

# Define loss and optimizer
loss = tf.reduce_mean(tf.nn.sampled_softmax_loss(weights=embeddings,
                                                  biases=tf.zeros([vocab_size]),
                                                  labels=train_labels,
                                                  inputs=cbow_model(train_inputs),
                                                  num_sampled=num_sampled,
                                                  num_classes=vocab_size))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

# Training step (not fully implemented)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Simulate multiple training epochs
    for epoch in range(1000):
        _, current_loss = sess.run([optimizer, loss])
        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {current_loss}')
