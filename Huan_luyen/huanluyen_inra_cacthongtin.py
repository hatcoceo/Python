import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Embedding
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

# Dữ liệu tiêu đề và từ ngữ
titles = ["Thanh lý tủ bánh mì", "Tủ bán hàng nhôm kính", "Thanh lý bàn học nhựa loại tốt", 
          "Tủ bán nước cam ép, tủ bán trái cây","Tủ chén bát 1mét"]  # Tiêu đề thực tế

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(titles)

# Tạo đầu vào và đầu ra
sequences = tokenizer.texts_to_sequences(titles)

# Pad sequences trước khi chuyển đổi thành mảng NumPy
max_sequence_len = max([len(x) for x in sequences])
sequences = pad_sequences(sequences, maxlen=max_sequence_len, padding='pre')

# Chuyển đổi sequences thành mảng NumPy
sequences = np.array(sequences)

# Tạo X và y
X, y = sequences[:, :-1], sequences[:, -1]

# Chuyển đổi y thành categorical
y = to_categorical(y, num_classes=len(tokenizer.word_index) + 1)
#print(y)
# Xây dựng mô hình
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=50, input_length=max_sequence_len-1))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(len(tokenizer.word_index)+1, activation='softmax'))

# Compile mô hình
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Huấn luyện mô hình
# verbose = 1 có chạy chạy, = 0 là không chạy 
model.fit(X, y, epochs=200, verbose=1)

#Chuỗi đã được token hóa
#print(sequences)

# Lấy embedding của lớp đầu tiên
embeddings = model.layers[0].get_weights()[0]

# Đặt tùy chọn hiển thị để không bị cắt bớt
#np.set_printoptions(threshold=np.inf, linewidth=np.inf)

# In embedding
#print(embeddings)

# In ra các token và chỉ số tương ứng
#for word, index in tokenizer.word_index.items():
  #  print(f"'{word}': {index}")
  
# số lượng từ trong từ điển 
#print(f"Số lượng từ trong từ điển: {len(tokenizer.word_index)}")

#word = "tủ"  # thay bằng từ bạn muốn
#token_index = tokenizer.word_index[word]
#embedding_vector = embeddings[token_index]
#print(f"Embedding cho từ '{word}':\n{embedding_vector}")
for i, layer in enumerate(model.layers):
    weights = layer.get_weights()
    print(f"Lớp {i}: {layer.name}")
    print("Trọng số:", weights)

