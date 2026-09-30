# Keras、PyTorch、TensorFlow 与 Transformer

## 一句话结论

> Keras、PyTorch 和 TensorFlow 是帮助我们构建、训练及部署模型的软件工具；Transformer 是一种神经网络架构。

它们不能直接当作同一类对象进行比较。

## 类比理解

- **Transformer**：建筑结构。
- **BERT、GPT**：按照这种结构设计出的具体建筑或建筑家族。
- **PyTorch、TensorFlow**：施工设备和工程系统。
- **Keras**：更简洁、统一的高层施工界面。
- **Hugging Face Transformers**：现成设计图、预制组件和模型仓库。

## 名词定位

| 名称 | 类型 | 主要用途 |
| --- | --- | --- |
| NumPy | 数值计算库 | 数组和矩阵运算，适合学习基础计算 |
| scikit-learn | 机器学习库 | 传统机器学习与数据预处理 |
| PyTorch | 深度学习框架 | 张量、自动求导、神经网络训练与部署 |
| TensorFlow | 机器学习平台/框架 | 模型训练、数据管道和多环境部署 |
| Keras | 高层深度学习 API | 用简洁接口定义、训练和评估模型 |
| Transformer | 模型架构 | 通过注意力机制建模信息之间的关系 |
| BERT、GPT | 模型家族 | 基于 Transformer 进行理解或生成 |
| Hugging Face Transformers | 模型工具库 | 获取、使用和微调预训练模型 |

## 1. PyTorch

PyTorch 是完整的深度学习框架，主要提供：

- 多维张量和 GPU 运算；
- 自动求导；
- 神经网络层与损失函数；
- 优化器；
- 数据加载；
- 分布式训练和部署工具。

PyTorch 的代码通常与 Python 的执行过程比较接近，便于观察前向传播、损失计算、反向传播和参数更新，因此适合作为理解深度学习原理的主线工具。

## 2. TensorFlow

TensorFlow 同样是完整的机器学习与深度学习平台，覆盖：

- 张量计算；
- 自动求导；
- 模型训练；
- 数据处理；
- 分布式计算；
- 服务端、浏览器和移动端部署。

TensorFlow 并不等于 Keras。TensorFlow 是较完整的平台，而 Keras 提供更高层的建模接口。

## 3. Keras

Keras 强调简洁、一致和快速实验，常用概念包括：

- `Layer`：网络层；
- `Model`：由多个层构成的模型；
- `fit`：训练；
- `evaluate`：评估；
- `predict`：预测。

需要区分：

- `tf.keras`：TensorFlow 中的 Keras API；
- Keras 3：独立的多后端 Keras，可使用 TensorFlow、JAX 或 PyTorch 等后端。

因此，Keras 与 PyTorch 在当前生态中并不总是完全二选一。可以使用 Keras 的高层接口，同时使用 PyTorch 作为计算后端。

## 4. Transformer

Transformer 是一种模型架构，主要由以下机制构成：

- Embedding；
- 位置编码；
- Self-Attention；
- Multi-Head Attention；
- 前馈神经网络；
- 残差连接与归一化；
- Encoder 和/或 Decoder。

Transformer 可以使用不同工具实现：

```text
PyTorch ──────┐
TensorFlow ───┼──→ 构建并训练 Transformer
Keras ────────┘
```

## 5. BERT 与 GPT

二者都来自 Transformer，但使用方式不同。

### BERT

- 主要使用 Transformer Encoder。
- 训练时能够结合左右两侧上下文。
- 常用于分类、实体识别、文本理解和信息抽取。

### GPT

- 主要使用 Transformer Decoder 风格的因果注意力。
- 按照已有内容预测后续 token。
- 适合文本生成，并可通过大规模预训练形成通用能力。

这只是总体方向；现代模型可能加入更多训练目标、工具调用和多模态组件。

## 6. 推荐学习方式

### 第一阶段：少量 NumPy

目的不是用 NumPy 构建大型模型，而是亲手理解矩阵乘法、损失和参数更新。

### 第二阶段：以 PyTorch 为主线

逐步实现：

1. 线性回归；
2. 全连接网络；
3. CNN；
4. RNN、LSTM；
5. Attention；
6. 小型 Transformer。

### 第三阶段：使用 Keras 对照

使用 Keras 重写一个已经理解的 PyTorch 模型，观察高层 API 帮助省略了哪些训练细节。

### 第四阶段：使用 Hugging Face

在理解 Transformer 后，再加载和微调 BERT、GPT 等预训练模型，避免只会调用接口而不理解输入、输出和训练机制。

## 7. 选择工具时考虑什么

| 需求 | 更合适的起点 |
| --- | --- |
| 学习传统机器学习 | scikit-learn |
| 理解神经网络训练细节 | PyTorch |
| 快速完成模型原型 | Keras |
| TensorFlow 生产生态 | TensorFlow + Keras |
| 使用预训练 Transformer | Hugging Face + PyTorch/Keras/TensorFlow |

这里没有绝对的“最好”，只有是否符合当前学习目标与项目约束。

## 自测问题

- [ ] PyTorch 与 Transformer 分别属于什么层级？
- [ ] TensorFlow 与 Keras 为什么不是同义词？
- [ ] Keras 3 的“多后端”是什么意思？
- [ ] BERT 和 GPT 为什么都属于 Transformer 家族？
- [ ] 为什么建议先理解 Transformer，再大量使用 Hugging Face？

## 官方资料

- [Keras 3](https://keras.io/keras_3/)
- [TensorFlow Keras Guide](https://www.tensorflow.org/guide/keras)
- [PyTorch Autograd Mechanics](https://docs.pytorch.org/docs/main/notes/autograd.html)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

