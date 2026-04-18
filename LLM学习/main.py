from collections import Counter


def build_bpe_vocab(texts, vocab_size=50):
    """
    简化BPE：只统计pair频率，不修改原文
    """
    # 初始化词表：每个字符独立
    vocab = set(char for text in texts for char in text)

    # 合并历史记录
    merges = []

    def get_pairs(text):
        """获取所有相邻pair"""
        return [(text[i], text[i + 1]) for i in range(len(text) - 1)]

    # 迭代合并
    while len(vocab) < vocab_size:
        # 统计所有pair的频率
        pairs = Counter()
        for text in texts:
            # 用当前词表来分词
            tokens = list(text)
            for pair in get_pairs(''.join(tokens)):
                pairs[pair] += 1

        if not pairs:
            break

        # 找最高频的pair
        best_pair = max(pairs, key=pairs.get)

        # 记录合并规则
        merges.append(best_pair)

        # 更新词表
        new_token = ''.join(best_pair)
        vocab.add(new_token)

        # 简单替换（用新token替代旧pair，只替换一次）
        new_texts = []
        for text in texts:
            new_text = text
            # 只替换第一个出现的位置
            pair_str = ''.join(best_pair)
            if pair_str in new_text:
                new_text = new_text.replace(pair_str, new_token, 1)
            new_texts.append(new_text)
        texts = new_texts

        print(f"合并: {best_pair} -> '{new_token}', 词表大小: {len(vocab)}")

        # 防止无限循环
        if len(vocab) >= vocab_size:
            break
        return vocab, merges


# 测试
texts = [
    "学习学习学习机器学习深度学习",
    "机器机器机器机器机器",
    "深度深度深度深度"
]

vocab, merges = build_bpe_vocab(texts, vocab_size=20)
print("\n最终词表:", vocab)
print("合并规则:", merges)