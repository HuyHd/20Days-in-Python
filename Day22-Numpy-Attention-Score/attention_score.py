import numpy as np

# Giúp kết quả giống nhau trên mọi máy khi tạo random
np.random.seed(42)

# Bước 1: Tạo từ điển và mã hóa từ
vocab = {"Tôi": 0, "thích": 1, "học": 2, "AI": 3}

# Số lượng từ vựng
vocab_size = len(vocab)

# Kích thước vector embedding
embedding_dim = 4

# Khởi tạo ma trận embedding ngẫu nhiên
embedding_matrix = np.random.rand(vocab_size, embedding_dim)

# Chuỗi đầu vào được mã hóa thành các vector embedding
input_seq = np.array(
    [embedding_matrix[vocab[word]] for word in ["Tôi", "thích", "học", "AI"]]
)
print("Chuỗi đầu vào (đã mã hóa):\n", input_seq)

# Bước 2: Khởi tạo các ma trận trọng số cho Q, K, V
W_q = np.random.rand(embedding_dim, embedding_dim)
W_k = np.random.rand(embedding_dim, embedding_dim)
W_v = np.random.rand(embedding_dim, embedding_dim)

# Tính toán Q, K, V
Q = np.dot(input_seq, W_q)
K = np.dot(input_seq, W_k)
V = np.dot(input_seq, W_v)

print("Ma trận Query Q:\n", Q)
print("Ma trận Key K:\n", K)
print("Ma trận Value V:\n", V)

# Bước 3: Tính toán Attetion score
K_T = np.transpose(K)
scores = np.dot(Q, K_T)

# Chia cho căn bậc hai của kích thước chiều của vector key
d_k = embedding_dim
scores = scores / np.sqrt(d_k)

print("Điểm số:\n", scores)


# Bước 4: Áp dụng hàm softmax
def softmax(x):
    x_max = np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x - x_max)
    sum_exp_x = np.sum(exp_x, axis=-1, keepdims=True)
    return exp_x / sum_exp_x


attention_weights = softmax(scores)

print("Trọng số Attention :\n", attention_weights)

# Bước 5: Tính toán tổng có trọng số của các value
output = np.dot(attention_weights, V)

print("Đầu ra :\n", output)
