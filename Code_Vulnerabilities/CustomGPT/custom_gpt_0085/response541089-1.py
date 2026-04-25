
import tensorflow as tf
import numpy as np

# Sample data (this should be your preprocessed data)
sentences = [["the", "dog", "barked"], ["the", "cat", "meowed"], ["the", "bird", "sang"]]
word_dict = {word: idx for idx, word in enumerate(set(sum(sentences, [])))}
reverse_word_dict = {idx: word for word, idx in word_dict.items()}
data = [[word_dict[word] for word in sentence] for sentence in sentences]

# CBOW parameters
window_size = 1
vocab_size = len(word_dict)
embedding_size = 10

# Create training data: context -> target
train_inputs, train_labels = [], []
for sentence in data:
    for i in range(window_size, len(sentence) - window_size):
        context = sentence[i - window_size:i] + sentence[i + 1:i + window_size + 1]
        target = sentence[i]
        train_inputs.append(context)
        train_labels.append(target)

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Build the model
inputs = tf.placeholder(tf.int32, shape=[None, 2 * window_size])
labels = tf.placeholder(tf.int32, shape=[None])

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
embed = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, inputs), axis=1)

# Output layer
weights = tf.Variable(tf.truncated_normal([embedding_size, vocab_size]))
biases = tf.Variable(tf.zeros([vocab_size]))
logits = tf.matmul(embed, weights) + biases

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits))
optimizer = tf.train.AdagradOptimizer(learning_rate=0.1).minimize(loss)

# Training process
num_epochs = 100
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(num_epochs):
        _, current_loss = sess.run([optimizer, loss], feed_dict={inputs: train_inputs, labels: train_labels})
        print(f'Epoch: {epoch}, Loss: {current_loss}')

# Save the embeddings
trained_embeddings = sess.run(embeddings)
