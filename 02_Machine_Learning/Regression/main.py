# main.py
# 机器学习基础：线性回归 (Linear Regression) 练习
# 目标：利用 scikit-learn 训练一个简单的线性回归模型，并评估其性能。

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def run_regression_demo():
    print("--- 经典机器学习：线性回归演示 ---")
    
    # 1. 模拟生成数据集
    # 假设特征 X 和目标值 y 的关系为: y = 3 * X + 4 + 随机噪点
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)
    
    # 2. 划分训练集和测试集 (80% 训练, 20% 测试)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"训练集大小: {X_train.shape[0]}, 测试集大小: {X_test.shape[0]}")
    
    # 3. 创建线性回归模型并拟合训练数据
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 输出模型学习到的参数 (权重 w 和偏置 b)
    print(f"模型学到的权重 (Slope, w): {model.coef_[0][0]:.4f} (期望接近 3.0)")
    print(f"模型学到的偏置 (Intercept, b): {model.intercept_[0]:.4f} (期望接近 4.0)")
    
    # 4. 在测试集上进行预测
    y_pred = model.predict(X_test)
    
    # 5. 评估模型性能
    # 均方误差 (MSE)
    mse = mean_squared_error(y_test, y_pred)
    # R² 分数 (决定系数，越接近 1 模型拟合越好)
    r2 = r2_score(y_test, y_pred)
    
    print(f"测试集均方误差 (MSE): {mse:.4f}")
    print(f"测试集决定系数 (R2 Score): {r2:.4f}")

if __name__ == "__main__":
    run_regression_demo()
