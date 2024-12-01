import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import scipy.stats as stats
data = [168,168,166,170,164,167,168,170,175,168,165,166,168,178,167,166,167,168,170,175,174,167,168,168,170,172,167,174,168,167,168,169,176,170,176,167,168,172,166,168,164,167,168,168,170,177,172,168,170,168]
def stem_and_leaf(data):
    # Sắp xếp dữ liệu
    data_sorted = sorted(data)
    
    # Tách thân và lá
    stems = [x // 10 for x in data_sorted]
    leaves = [x % 10 for x in data_sorted]
    
    # Tạo biểu đồ thân và lá
    stem_leaf_dict = {}
    for stem, leaf in zip(stems, leaves):
        if stem not in stem_leaf_dict:
            stem_leaf_dict[stem] = []
        stem_leaf_dict[stem].append(leaf)
    
    # In ra biểu đồ
    for stem, leaf_list in stem_leaf_dict.items():
        print(f"{stem} | {' '.join(map(str, leaf_list))}")

stem_and_leaf(data)

frequency_table = pd.Series(data).value_counts().sort_index()
print(frequency_table)

# Vẽ biểu đồ cột
plt.figure(figsize=(8, 5))
sns.histplot(data, bins=range(min(data), max(data) + 1), kde=False)
plt.xlabel("Chiều cao (cm)")
plt.ylabel("Tần số")
plt.title("Biểu đồ tần số chiều cao")
plt.show()
mean = np.mean(data)
std_dev = np.std(data, ddof=1)  # độ lệch chuẩn hiệu chỉnh
median = np.median(data)

print(f"Trung bình mẫu: {mean}")
print(f"Độ lệch chuẩn mẫu: {std_dev}")
print(f"Trung vị mẫu: {median}")
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = q3 - q1

res = stats.probplot(data, dist="norm")

# Vẽ biểu đồ với chiều cao nằm trên trục x
plt.figure(figsize=(8, 6))
plt.scatter(res[0][1], res[0][0], label="Dữ liệu", color="blue")  # Đổi x và y
plt.plot(res[1][1] + res[1][0] * res[0][0], res[0][0], 'r-', label="Phân phối chuẩn", color="red")  # Đổi x và y
plt.ylabel("Phân vị lý thuyết (Theoretical Quantiles)")
plt.xlabel("Chiều cao thực tế (Observed Values)")
plt.title("Biểu đồ xác suất chuẩn (Chiều cao theo chiều ngang)")
plt.legend()
plt.show()

