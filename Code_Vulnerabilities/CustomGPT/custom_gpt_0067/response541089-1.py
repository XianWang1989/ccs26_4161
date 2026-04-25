
import tensorflow as tf
import numpy as np

# Sample data
sentences = [['the', 'cat', 'sits'], ['on', 'the', 'mat']]
vocab = set(word for sentence in sentences for word in sentence)
word_to_id = {word: idx for idx, word in enumerate(vocab)}

# Create CBOW training data
window_size = 1
train_inputs = []
train_labels = []

for sentence in sentences:
    for i in range(len(sentence)):
        context = []
        for j in range(-window_size, window_size + 1):
            if j != 0 and 0 <= i + j < len(sentence):
                context.append(word_to_id[sentence[i + j]])
        train_inputs.append(context)
        train_labels.append(word_to_id[sentence[i]])

# Model parameters
vocab_size = len(vocab)
embedding_dim = 10

# Create placeholders
inputs = tf.placeholder(tf.int32, shape=[None, 2 * window_size])
labels = tf.placeholder(tf.int32, shape=[None])

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
input_embeds = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, inputs), axis=1)

# Output layer
logits = tf.layers.dense(input_embeds, vocab_size)
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits))

# Training operation
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Running the session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Example training loop (this should be replaced with epochs and batch handling)
    for epoch in range(100):
        _, loss_value = sess.run([train_op, loss], feed_dict={inputs: train_inputs, labels: train_labels})
        if epoch % 10 == 0:
            print(f'Epoch {epoch}, Loss: {loss_value}')
