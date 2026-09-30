import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# read data
dataset = pd.read_csv("breast_cancer_data.csv")
# print(dataset)

# select X
X = dataset.iloc[:, :-1]
# print(X)

# select Y
Y = dataset['target']
# print(Y)

# train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# normalize
sc = MinMaxScaler(feature_range = (0,1))
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# sklearn create model
lr = LogisticRegression()
lr.fit(x_train, y_train)

# print model param
# print(f"w :  {lr.coef_} , b :  {lr.intercept_}")

# test the model with the test data
pre_result = lr.predict(x_test)
print(pre_result)

# 打印预测结果的概率
pre_result_proba = lr.predict_proba(x_test)
# print(np.array2string(pre_result_proba*100, formatter={'float_kind': lambda x: f"{x:.2f}%"}))


# change the threshold
pre_result_proba_n = pre_result_proba[:,1]
# print(pre_result_proba_n)

threshold = 0.3
result = []
result_name = []

for i in range(0,len(pre_result_proba_n)):
    if pre_result_proba_n[i] > threshold:
        result.append(1)
        result_name.append('恶性')
    else:
        result.append(0)
        result_name.append('良性')
# print(result)

# report the result
report = classification_report(y_test, result, labels=[0, 1], target_names=['良性肿瘤', '恶性肿瘤'])
print(report)