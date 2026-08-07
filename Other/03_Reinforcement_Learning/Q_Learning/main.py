# main.py
# 强化学习基础：Q-Learning 算法练习
#
# 目标：在一个自制的 1D 网格世界（Grid World）中训练一个 Agent 学习如何寻找宝藏。
# 网格环境：[S, 0, 0, 0, 0, G]  (S: 起点 index 0, G: 宝藏/终点 index 5)
# 动作：0 (向左), 1 (向右)

import numpy as np
import time
import random

# 环境参数
N_STATES = 6    # 网格长度
ACTIONS = [0, 1] # 0: left, 1: right
EPSILON = 0.9   # 贪婪度 (epsilon-greedy)，90% 的概率选择最优动作，10% 探索
ALPHA = 0.1     # 学习率 (learning rate)
GAMMA = 0.9     # 折扣因子 (discount factor)，决定了未来奖励的重要性
MAX_EPISODES = 15 # 训练的轮数

def build_q_table(n_states, n_actions):
    # 初始化 Q-Table 为全 0，形状为 (状态数, 动作数)
    return np.zeros((n_states, n_actions))

def choose_action(state, q_table):
    # Epsilon-Greedy 动作选择策略
    state_actions = q_table[state, :]
    # 探索：随机选择动作
    if (random.random() > EPSILON) or (np.all(state_actions == 0)):
        action = random.choice(ACTIONS)
    else:
        # 开发：选择当前状态下 Q 值最大的动作
        action = np.argmax(state_actions)
    return action

def get_env_feedback(state, action):
    # 环境交互逻辑
    # 输入当前状态和动作，返回下一个状态和即时奖励
    if action == 1:  # move right
        if state == N_STATES - 2:  # 达到终点前一格，下一步到达终点 G
            next_state = 'terminal'
            reward = 1.0
        else:
            next_state = state + 1
            reward = 0.0
    else:  # move left
        reward = 0.0
        if state == 0:
            next_state = state  # 撞墙，留在原地
        else:
            next_state = state - 1
    return next_state, reward

def update_env_display(state, episode, step_counter):
    # 打印环境当前状态（可视化网格）
    env_list = ['-'] * (N_STATES - 1) + ['G']
    if state != 'terminal':
        env_list[state] = 'A' # A 代表 Agent
        interaction = ''.join(env_list)
        print(f"\rEpisode {episode+1}: {interaction} (Steps: {step_counter})", end="")
        time.sleep(0.1)
    else:
        interaction = ''.join(env_list)
        print(f"\rEpisode {episode+1}: {interaction} (Steps: {step_counter}) -> SUCCESS!", end="")
        print()
        time.sleep(0.3)

def rl_loop():
    q_table = build_q_table(N_STATES, len(ACTIONS))
    print("开始 Q-Learning 强化学习训练...")
    
    for episode in range(MAX_EPISODES):
        step_counter = 0
        state = 0 # 每一轮都从起点 (index 0) 开始
        is_terminated = False
        update_env_display(state, episode, step_counter)
        
        while not is_terminated:
            # 1. 选择动作
            action = choose_action(state, q_table)
            # 2. 与环境交互获取反馈
            next_state, reward = get_env_feedback(state, action)
            
            # 3. 更新 Q-Table (贝尔曼方程核心公式)
            q_predict = q_table[state, action]
            if next_state != 'terminal':
                # 状态未结束，计算估计的未来最大 Q 值
                q_target = reward + GAMMA * np.max(q_table[next_state, :])
            else:
                # 达到终点，没有未来的状态了
                q_target = reward
                is_terminated = True
                
            # 更新公式：Q(s,a) = Q(s,a) + alpha * [Q_target - Q(s,a)]
            q_table[state, action] += ALPHA * (q_target - q_predict)
            
            # 4. 状态转移
            state = next_state
            step_counter += 1
            update_env_display(state, episode, step_counter)
            
    print("\n训练完成！最终学习到的 Q-Table：")
    print("状态(位置) | 向左(Action 0) | 向右(Action 1)")
    for i in range(N_STATES - 1):
        print(f" 位置 {i}  |  {q_table[i, 0]:.4f}      |  {q_table[i, 1]:.4f}")
    print("\n说明：随着训练，往右走的 Q 值会逐渐增大，直至成为最优策略。")

if __name__ == "__main__":
    rl_loop()
