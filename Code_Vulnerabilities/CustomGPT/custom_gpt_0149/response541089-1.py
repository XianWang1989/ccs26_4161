
import tensorflow as tf
import numpy as np

# Sample data: context and target words
words = ["the", "cat", "sat", "on", "the", "mat"]
word_to_id = {word: i for i, word in enumerate(set(words))}
id_to_word = {i: word for word, i in word_to_id.items()}

# Preparing training data for CBOW
window_size = 1
train_inputs = []
train_labels = []

for i in range(window_size, len(words) - window_size):
    context = []
    for j in range(-window_size, window_size + 1):
        if j != 0:
            context.append(word_to_id[words[i + j]])
    train_inputs.append(context)
    train_labels.append(word_to_id[words[i]])

# Convert inputs and labels to a one-hot encoding format
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Build the CBOW model
vocab_size = len(word_to_id)

# Placeholder definitions
X = tf.placeholder(tf.int32, shape=[None, window_size * 2])
Y = tf.placeholder(tf.int32, shape=[None])

# Embedding for input words
W = tf.Variable(tf.random_uniform([vocab_size, 10], -1.0, 1.0))  # 10-dimensional vectors
embedding = tf.nn.embedding_lookup(W, X)

# Average embeddings for context
average_embedding = tf.reduce_mean(embedding, axis=1)

# Output layer
W_output = tf.Variable(tf.random_uniform([10, vocab_size], -1.0, 1.0))
b_output = tf.Variable(tf.zeros([vocab_size]))

# Logits and loss
logits = tf.matmul(average_embedding, W_output) + b_output
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=Y, logits=logits))

# Training operation
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# Training the model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(1000):
        _, loss_val = sess.run([train_op, loss], feed_dict={X: train_inputs, Y: train_labels})
        if epoch % 100 == 0:
            print(f'Epoch: {epoch}, Loss: {loss_val}')

    # Get the learned embeddings
    trained_embeddings = sess.run(W)

print("Training complete. Embeddings:")
print(trained_embeddings)
