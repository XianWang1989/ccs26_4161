
import numpy as np
import tensorflow as tf

# Sample data: context words and the target word
context_window = 2
words = ["the", "dog", "barked", "loudly"]
target_word = "barked"

# Create a word index
word_index = {word: i for i, word in enumerate(words)}

# Prepare training inputs and labels for CBOW
train_inputs = []
train_labels = []
for i in range(context_window, len(words) - context_window):
    context = []
    for j in range(-context_window, context_window + 1):
        if j != 0:
            context.append(word_index[words[i + j]])
    train_inputs.append(context)
    train_labels.append(word_index[words[i]])

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define the CBOW model
vocab_size = len(words)
embedding_size = 16  # Size of the embedding vector

# Build the graph
inputs = tf.placeholder(tf.int32, shape=[None, context_window * 2])
labels = tf.placeholder(tf.int32, shape=[None])

embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
input_embeddings = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, inputs), axis=1)

logits = tf.layers.dense(input_embeddings, vocab_size)
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits))

optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

# Training the model
num_epochs = 1000
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(num_epochs):
        _, loss_value = sess.run([optimizer, loss], feed_dict={inputs: train_inputs, labels: train_labels})
        if epoch % 100 == 0:
            print(f'Epoch: {epoch}, Loss: {loss_value}')

    # Retrieve and print final embeddings
    final_embeddings = sess.run(embeddings)
    print("Final word embeddings:\n", final_embeddings)
