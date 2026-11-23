# LLM 学习总规划

> 从零基础到能跑 QLoRA 微调 + 做 Agent/RAG 应用。节奏按**名义 1 天 ≈ 实际 4 天**预估。

**起始日**：2026-08-03
**每日时长**：4 小时
**硬件**：NVIDIA RTX 4050 Laptop GPU（6GB 显存）→ 可做 4-bit 7B 推理 / Unsloth QLoRA 微调 1.5B-3B
**约束**：不碰超出显存的全参数预训练，概念理解即可

## 2026-11 优化说明

本 plan 2026-11-05 根据近一年 LLM 发展做了增量优化，关键改动：

- **模型选型升级**：微调目标从 Qwen2.5-1.5B / TinyLlama → **Qwen3-1.7B / Phi-4-mini / SmolLM3**（更强、更省显存）
- **工具链升级**：QLoRA → **Unsloth + QLoRA**（显存 < 4GB、速度 2-5×）
- **新增推理模型**：加入 o1 / DeepSeek-R1 路线（CoT 训练 / Process Reward / R1-Distill 蒸馏模型推理）
- **微调范式升级**：Day 43 从"RLHF 概念"升级为 **DPO + GRPO 原理 + DPO 实操**（GRPO 是 R1 核心，DPO 是当前偏好微调主流）
- **架构补齐**：加入 **MoE / MLA / GQA**（Qwen3.5、DeepSeek-V4、Llama 4 都用）
- **Agent 范式革新**：function calling → **MCP 协议**（2026 年全行业事实标准，Anthropic/OpenAI/Google 全线采用），新增"自写 MCP server"
- **压缩旧内容**：RNN/LSTM 从 2 天压到 1 天（只作历史背景），BERT 并入 nanoGPT 讨论

---

## 当前状态（2026-11-05）

| Day | 主题 | 状态 |
|---|---|---|
| 1 | 环境 + Python/NumPy 自测 | ✅ `266085d` |
| 2 | NumPy 深入 + numpy-100 前 15 题 | ✅ `75e871f` |
| 3 | 3B1B 线性代数 EP1-4 | ✅ `f3b5e26` |
| 4 | 3B1B 线性代数 EP5-8 | 🟡 **卡住 2 个半月，从这里恢复** |

**恢复建议**：Day 4 笔记骨架和 4 个代码文件已经建好，直接看 EP5 + 填笔记第一节 + 跑 `ep5_3d_transform.py`，一次 30-40 分钟就能破除惯性。

---

## 阶段 1：数学 & ML 基础（Day 4-12，剩 9 名义天 ≈ 36 实际天）

用 3B1B 系列打直觉，用 NumPy 手跑验证。

| Day | 主题 | 产出 |
|---|---|---|
| 4 | 3B1B 线代 EP5-8（3D 变换 / 行列式 / 逆与秩 / 非方阵） | 填完 `notes/day04.md` + 4 个 .py 跑通 |
| 5 | 3B1B 线代 EP9-11（点积 / 叉积 / 基变换） | 笔记 + 代码验证基变换矩阵 |
| 6 | 3B1B 线代 EP12-15（克拉默法则 / 特征值特征向量 / 抽象向量空间） | NumPy 求一个 3×3 矩阵的特征分解 |
| 7 | 3B1B 微积分 EP1-4（导数本质 / 幂法则 / 链式法则 / 隐函数） | 手推 sigmoid 和 ReLU 导数 |
| 8 | 3B1B 微积分 EP5-8（泰勒展开 / 多元 / 偏导 / 梯度） | 画一个二元函数的梯度场 |
| 9 | 概率基础（期望 / 方差 / 条件概率 / 贝叶斯公式） | NumPy 模拟三门问题、验证贝叶斯 |
| 10 | 常见分布（二项 / 正态 / 多项 / softmax 的数值稳定性） | 画 PDF/CDF；实现数值稳定的 softmax |
| 11 | 梯度下降手写（一元二次 → 二元 Himmelblau 函数） | 纯 NumPy 跑收敛、画轨迹 |
| 12 | ML 核心概念（loss / 过拟合 / 训练验证测试集） | sklearn 跑波士顿房价线性回归 |

**阶段里程碑**：能在白板上讲清"为什么训练神经网络需要线代和微积分"，并用纯 NumPy 从零实现一元线性回归（数据生成 → 梯度下降 → 可视化拟合曲线）。

---

## 阶段 2：PyTorch & 深度学习（Day 13-22，10 名义天 ≈ 40 实际天）

主参考：**李沐《动手学深度学习》PyTorch 版**（zh-v2.d2l.ai，中文免费）。

| Day | 主题 | 产出 |
|---|---|---|
| 13 | PyTorch 安装（CUDA 版）+ tensor 基础 | 验证 GPU 可用；tensor 创建/索引/运算 |
| 14 | autograd 原理（requires_grad / backward / 计算图） | 手写一元线性回归用 autograd 版 |
| 15 | 不用 nn.Module，纯 tensor + autograd 写一层网络 | 跑通反向传播 |
| 16 | nn.Module / nn.Linear / 损失 / 优化器 | 用框架重写 Day 15 |
| 17 | Dataset / DataLoader / 数据管道 | 加载 MNIST，看 batch 形状 |
| 18 | MLP 实战 MNIST | 测试集 > 97% |
| 19 | CNN 入门（conv2d / 池化 / BN） | 手算一个 3×3 卷积的输出 |
| 20 | CNN 实战 MNIST → CIFAR-10 | 对比 MLP 和 CNN 准确率 |
| 21 | RNN / LSTM 速览（仅作历史背景）+ seq2seq 范式 | 一页笔记说清 Transformer 为何取代 RNN |
| 22 | **机动日**：补 Day 13-21 的坑 / 做 Kaggle 入门小赛 | 任选一个空缺补齐 |

**阶段里程碑**：能从零（import torch 开始）写一个 CNN 在 CIFAR-10 上训练到 > 70% 准确率，解释清楚训练循环每一行在干什么。

---

## 阶段 3：Transformer & 现代 LLM 架构（Day 23-33，11 名义天 ≈ 44 实际天）

主参考：**Karpathy "Zero to Hero" 系列**（B 站有搬运）+ **nanoGPT 源码** + **DeepSeek-R1 / Llama 4 / Qwen3 技术报告选读**。

| Day | 主题 | 产出 |
|---|---|---|
| 23 | 分词（字符级 → BPE → tiktoken / Qwen3 tokenizer） | 手写一个最小 BPE |
| 24 | 词嵌入（nn.Embedding / Word2Vec 直觉） | 可视化一个训练好的 embedding |
| 25 | Attention 从零（scaled dot-product attention） | 手写 `attention(Q,K,V)` 函数 |
| 26 | Multi-head Attention → **GQA（分组查询注意力）** | 对比 MHA / MQA / GQA 的 KV cache 大小 |
| 27 | 位置编码（sinusoidal → **RoPE** 实操） | 用 RoPE 替换 nanoGPT 的位置编码 |
| 28 | Transformer Encoder 完整实现（含 BERT 范式对比） | 用 PyTorch 拼一个 Encoder |
| 29 | Transformer Decoder + causal mask | 跑通 decoder-only 的 forward |
| 30 | 精读 nanoGPT 源码（约 300 行） | 每一行都能解释 |
| 31 | 在莎士比亚 / 中文小语料上训练自己的 GPT | 能生成可读的文本片段 |
| 32 | **现代 LLM 架构全景**：RMSNorm / RoPE / GQA / SwiGLU / **MoE / MLA** | 一张对比图（Llama 4 / Qwen3 / DeepSeek-V4） |
| 33 | **推理模型原理**：CoT prompting → o1 / DeepSeek-R1 / Qwen3-Max-Thinking 的思路 | 读 R1 论文摘要 + 本地跑 **DeepSeek-R1-Distill-Qwen-1.5B** 看思考过程 |

**阶段里程碑**：能复现一个完整的 decoder-only Transformer（含训练循环），在小语料上训练出能生成合理文本的模型。看懂 nanoGPT 每一行。**能用一张图讲清 2026 年主流开源 LLM（Llama 4 / Qwen3 / DeepSeek-V4）的架构异同**，以及推理模型相比普通 chat 模型多了什么。

---

## 阶段 4：大模型训练与微调（Day 34-43，10 名义天 ≈ 40 实际天）

**显存约束**：全参数微调 7B 要 > 80GB，你跑不动。重点是 **Unsloth + QLoRA**（2026 年事实最优工具，4-bit 微调速度 2-5× 且显存 < 4GB）+ **DPO 偏好微调** + **GRPO 推理模型训练原理**。

| Day | 主题 | 产出 |
|---|---|---|
| 34 | Hugging Face transformers 入门（模型加载 / pipeline） | 本地跑 **Qwen3-1.7B** 推理 |
| 35 | HF datasets + tokenizers | 加载并处理一个指令数据集 |
| 36 | **预训练 vs SFT vs DPO vs RAG** 概念区分 | 一张图说清四者关系与何时用什么 |
| 37 | LoRA 原理（低秩分解 + 旁路） | 手推 LoRA 的参数量节省 |
| 38 | **Unsloth + LoRA** 第一次微调 | 微调 **Qwen3-0.6B** 做情感分类，显存 < 3GB |
| 39 | QLoRA 原理（4-bit NF4 量化 + LoRA） | 读 QLoRA 论文核心章节 |
| 40 | QLoRA 实战 part 1：数据准备 | 构造 500-1000 条指令数据（含 CoT 格式） |
| 41 | QLoRA 实战 part 2：训练 **Qwen3-1.7B** 或 **Phi-4-mini** | 训练完成、保存 adapter、合并权重 |
| 42 | 评测对比 + **DPO 偏好微调实操**（Unsloth DPO） | 10 条对照 + 1 次 DPO 跑通 |
| 43 | **GRPO 原理 + 推理模型蒸馏**（DeepSeek-R1 怎么练出来的） | 一页笔记说清 PPO / DPO / GRPO 差异 + 用 R1-Distill 跑一次思考过程 |

**阶段里程碑**：在自己电脑上完整跑通一次 **Unsloth QLoRA 微调**（Qwen3-1.7B 或 Phi-4-mini），微调前后行为有可观察的差异；**能解释 PPO / DPO / GRPO 三者的差异**，以及 DeepSeek-R1 通过 GRPO + RL 让小模型涌现推理能力的大致思路。能把每一步（数据 → tokenize → LoRA/QLoRA 配置 → 训练 → 合并 → 推理 → DPO）讲清楚。

---

## 阶段 5：应用、Agent 与部署（Day 44-55，12 名义天 ≈ 48 实际天）

**2026 年 Agent 事实标准是 MCP（Model Context Protocol，Anthropic 发起，全行业采用）**，本阶段用一半篇幅在 MCP 上。

| Day | 主题 | 产出 |
|---|---|---|
| 44 | 推理优化概念（KV cache / batching / flash attention / **vLLM vs SGLang vs llama.cpp** 对比） | 一页选型笔记 |
| 45 | llama.cpp / GGUF 量化本地跑 | 本地起 **Qwen3-8B-Q4** 推理服务 |
| 46 | Embedding 模型（**bge-m3 / Qwen3-Embedding**） | 跑一次 embedding，看向量形状 |
| 47 | 向量库（Chroma 或 FAISS 本地） | 存 100 段文本并检索 |
| 48 | RAG 完整链路（检索 → rerank → 拼 prompt → 生成） | 跑通一个最小 RAG demo |
| 49 | **MCP 协议入门**：对比历史上的 function calling，看懂 MCP 的 initialize / tools/list / tools/call | 用 Claude Desktop 或 Cursor 接一个现成 MCP server 跑通 |
| 50 | **自己写一个 MCP server**（Python SDK）：暴露本地文件搜索 / 笔记检索工具 | 一个能被 Claude Desktop 调用的本地 MCP server |
| 51 | **Agent 范式**：ReAct + 多 MCP server 协作 | 跑一个"文件搜索 + 网页搜索"两工具 agent |
| 52-55 | 项目实战（五选一） | 完整上线一个小项目 |

**项目候选**（选 1 个，4 天完成）：
1. **本地文档问答**（RAG）：喂 PDF/Markdown，用 Qwen3-8B 做问答
2. **代码助手**（SFT）：用自己的代码风格 QLoRA 微调一个 SmolLM3-3B
3. **领域分类器**（DPO）：QLoRA + DPO 做某个二分类任务
4. **学习助手 MCP server**（Agent）：把你的 `learning-plan.md` 和所有 `notes/dayXX.md` 做成一个 MCP server，让 Claude Code 能问"我 Day X 学了什么"——**这个最能展示 2026 年 Agent 范式，推荐**
5. **多模态小应用**：用 Qwen3-VL 做图片分类 / OCR / 简单视觉问答（如果显存够）

**阶段里程碑（也是整个计划的终点）**：一个你能在 GitHub README 展示的、能运行、有说明文档的 LLM 小项目，**优先选 MCP server 方向**——这是 2026 年 Agent 工程师的入场券。

---

## 时间总览

| 阶段 | 名义天数 | 实际天数（×4） | 累计实际天 |
|---|---|---|---|
| 阶段 1 剩余 | 9 | 36 | 36 |
| 阶段 2 | 10 | 40 | 76 |
| 阶段 3 | 11 | 44 | 120 |
| 阶段 4 | 10 | 40 | 160 |
| 阶段 5 | 12 | 48 | 208 |

**总计 ≈ 208 实际天 ≈ 7 个月**。如果从 2026-11-10 恢复 Day 4，预计 2027-06 前后完成阶段 5。

---

## 使用这份计划的规则

- **不追赶进度**：卡住就卡住，多花时间比跳过强。4:1 节奏本来就包含了卡壳时间。
- **每天收尾必 push**：仪式感 + 可视化。
- **笔记必写 why**：能从笔记重建知识的才算真学会。
- **代码必跑通**：看懂不等于会写，手打一遍。
- **每阶段结束回看里程碑**：没达到就停一两天补齐，不往下推。
- **这份 plan 每阶段结束允许修订一次**：新学完一个阶段，你对下一阶段的理解会变，别死守旧计划。
