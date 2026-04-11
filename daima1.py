rom typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
              n = len(grid)
        # [CONSTRAINT-健壮性] 处理 n < 2 的边界情况
        if n == 0:
            return 0
        if n == 1:
            # 单列无邻居，任何格子都不能得分
            return 0

        # [CONSTRAINT-副作用] 不修改原 grid，创建列前缀和数组（新列表）
        # 预处理每一列的前缀和，col_prefix[j][i] 表示第 j 列前 i 行的和（i 从 0 到 n）
        col_prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                col_prefix[j][i+1] = col_prefix[j][i] + grid[i][j]

        # DP 数组：dp[j][c] 表示处理完前 j 列（0..j），且第 j 列涂黑行数为 c 时的最大得分
        # 使用 -10**18 作为负无穷（因为元素绝对值可能很大，但 n<=200 时总和不超过 2e5*200? 安全起见用极小值）
        NEG_INF = -10**18
        # 维度：n 列，每列 n+1 种状态（0..n）
        dp = [[NEG_INF] * (n + 1) for _ in range(n)]

        # 初始化第一列：第一列本身没有左侧邻居，其右侧贡献将在与第二列转移时计算
        for c in range(n + 1):
            dp[0][c] = 0

        # [CONSTRAINT-正确性] 动态规划正确性说明：
        # 最优涂黑方案对应一个高度序列 k[0..n-1]。对于任意相邻列 (j-1, j)，
        # 得分由两部分组成：列 j 的白色格子因左侧黑色而得的分数，以及列 j-1 的白色格子因右侧黑色而得的分数。
        # DP 在转移时枚举 k[j-1]=prev 和 k[j]=cur，并累加这两个贡献，同时保留历史最优。
        # 由于每一对相邻列的贡献只依赖于这两列的高度，且无后效性，因此 DP 能正确求出全局最大值。

        # 逐列转移
        for j in range(1, n):
            for cur in range(n + 1):          # 当前列涂黑行数
                best = NEG_INF
                for prev in range(n + 1):     # 前一列涂黑行数
                    # 计算列 j 的左侧贡献（左侧列黑色使得当前列白色格子得分）
                    # 白色行 i >= cur，左侧黑色 i < prev  → i ∈ [cur, min(n-1, prev-1)]
                    left_start = cur
                    left_end = min(n - 1, prev - 1)
                    left_contrib = 0
                    if left_start <= left_end:
                        # 利用前缀和求第 j 列区间 [left_start, left_end] 的和
                        left_contrib = col_prefix[j][left_end + 1] - col_prefix[j][left_start]

                    # 计算列 j-1 的右侧贡献（当前列黑色使得左侧列白色格子得分）
                    # 左侧列白色行 i >= prev，右侧黑色 i < cur  → i ∈ [prev, min(n-1, cur-1)]
                    right_start = prev
                    right_end = min(n - 1, cur - 1)
                    right_contrib = 0
                    if right_start <= right_end:
                        right_contrib = col_prefix[j-1][right_end + 1] - col_prefix[j-1][right_start]

                    total = dp[j-1][prev] + left_contrib + right_contrib
                    if total > best:
                        best = total
                dp[j][cur] = best

        # 最后一列没有右侧邻居，但我们在转移中已经将其作为“前一列”计算了对左侧列的右侧贡献，
        # 且最后一列自身的左侧贡献已计入。因此答案即为最后一列各状态的最大值。
        answer = max(dp[n-1][c] for c in range(n + 1))
        return answer