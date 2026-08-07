# main.py
# 机器学习基础：分类问题 (Classification) 练习
# 目标：加载经典鸢尾花 (Iris) 数据集，训练逻辑回归 (Logistic Regression) 分类器，并评估分类指标。

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def run_classification_demo():
    print("--- 经典机器学习：鸢尾花三分类演示 ---")
    
    # 1. 加载鸢尾花数据集 (包含 150 个样本，4 个特征，3 个类别)
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names
    
    print("特征名称:", feature_names)
    print("类别名称:", target_names)
    
    # 2. 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    print(f"训练集样本数: {X_train.shape[0]}, 测试集样本数: {X_test.shape[0]}")
    
    # 3. 创建逻辑回归模型并训练 (增加 max_iter 确保收敛)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    
    # 4. 在测试集上进行预测
    y_pred = model.predict(X_test)
    
    # 5. 评估分类结果
    # 准确率 (Accuracy)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n测试集准确率 (Accuracy): {accuracy:.4f}")
    
    # 详细的分类报告 (包含 Precision, Recall, F1-Score)
    print("\n--- 详细分类报告 ---")
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # 混淆矩阵 (Confusion Matrix)
    print("--- 混淆矩阵 ---")
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    run_classification_demo()
