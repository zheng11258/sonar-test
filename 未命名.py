from typing import List

class Solution:
    def treeOfInfiniteSouls(self, gem: List[int], p: int, target: int) -> int:
        n = len(gem)
        if n == 0:
            return 0
        
        # 叶子节点：0代表宝石（存储索引），内部节点：(左, 右)代表子树
        # 生成所有n个叶子的满二叉树结构（结构唯一标识：子树元组）
        structures = self.generate_full_binary_trees(n)
        total = 0
        
        # 遍历每一种树结构
        for struct in structures:
            # 收集该结构的叶子位置数量（一定等于n）
            leaf_positions = self.count_leaves(struct)
            assert leaf_positions == n
            
            # 枚举宝石的全排列（不同索引=不同方案）
            import itertools
            for perm in itertools.permutations(gem):
                # 模拟遍历，计算数字串 mod p
                mod = self.compute_mod(struct, perm, p)
                if mod == target:
                    total += 1
        return total
    
    def generate_full_binary_trees(self, n: int) -> list:
        """生成n个叶子的所有满二叉树结构（递归生成）"""
        # 记忆化缓存
        memo = {}
        
        def build(k):
            if k in memo:
                return memo[k]
            if k == 1:
                # 单个叶子节点，用0标记
                res = [0]
                memo[k] = res
                return res
            res = []
            # 满二叉树：左子树i个叶子，右子树k-i个叶子，i>=1
            for i in range(1, k):
                j = k - i
                left_trees = build(i)
                right_trees = build(j)
                # 组合左右子树
                for l in left_trees:
                    for r in right_trees:
                        res.append((l, r))
            memo[k] = res
            return res
        
        return build(n)
    
    def count_leaves(self, struct) -> int:
        """统计树结构的叶子数量"""
        if struct == 0:
            return 1
        return self.count_leaves(struct[0]) + self.count_leaves(struct[1])
    
    def compute_mod(self, struct, gem_perm, p: int) -> int:
        """模拟遍历过程，动态计算数字串 mod p 的值"""
        mod = 0
        idx = 0  # 宝石排列的索引
        
        def dfs(node):
            nonlocal mod, idx
            # 首次到达节点：记录1
            mod = (mod * 10 + 1) % p
            
            if node == 0:
                # 叶子节点：额外记录宝石数值
                val = gem_perm[idx]
                idx += 1
                s = str(val)
                for c in s:
                    mod = (mod * 10 + int(c)) % p
                # 叶子无子女，记录9
                mod = (mod * 10 + 9) % p
                return
            
            # 内部节点：先左后右
            dfs(node[0])
            dfs(node[1])
            # 子女遍历完，记录9
            mod = (mod * 10 + 9) % p
        
        dfs(struct)
        return mod