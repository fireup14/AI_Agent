import numpy as np


print("第一步：手写 Embedding 查表")
embedding_matrix = np.random.randn(5, 3)
word_ids = [0, 3, 4]
vectors = embedding_matrix[word_ids]
print(vectors)

print("第二步：验证 One-hot 乘法等价性")
one_hot = np.zeros(5)
one_hot[3] = 1
vector_a = one_hot @ embedding_matrix
vector_b = embedding_matrix[3]
print(vector_b, vector_a)
print(np.allclose(vector_a, vector_b))

print("第三步：记录每一步的张量形状")
print(embedding_matrix.shape)
print(one_hot.shape)
print(vector_a.shape)


