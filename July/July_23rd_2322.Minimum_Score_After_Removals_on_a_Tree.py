# link: https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/?envType=daily-question&envId=2025-07-24
# Thanks again to larry: https://www.youtube.com/watch?v=S370Vx9YPjg&t=1711s

# tags: Array Bit Manipulation Tree DFS 

# day: July 23rd

# Hard

class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        
        adj = defaultdict(list)

        # set up adj list
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        # is_ancestor[i][node] = is node i is ancestor of current node
        is_ancestor = [[False] * len(nums) for n in range(len(nums))]
        
        # first passthrough
        # dfs to make an ancestor list
        def dfs(node, parent, ancestors):
            # if at this current node, a is an ancestor of this node
            """
                a
               / \
             node ***
            """
            for a in ancestors:
                is_ancestor[a][node] = True
            
            # now search neighboring node from node
            for nei in adj[node]:
                # if this neighbor is not a parent, then node is an ancestor of nei
                if nei != parent:
                    ancestors.append(node)
                    # now search using this nei as the node and node as its parent
                    dfs(nei, node, ancestors)
                    # backtarck
                    ancestors.pop()
        
        dfs(0, -1, [])

        # xor_sums[i] = subtree cor sum at node i
        xor_sums = [None] * len(nums)

        # dfs to preprocess the total xor_sum from all
        def dfs2(node, parent):
            curr = nums[node]
            for nei in adj[node]:
                if nei != parent:
                    # get the total xor of all numbers in this subtree from nei
                    curr ^= dfs2(nei, node)
            xor_sums[node] = curr
            return curr
        
        dfs2(0, -1)

        total = xor_sums[0]
        res = float('inf')
        # try every pair of nodes as the subtree
        for a in range(1, len(nums)):
            for b in range(a + 1, len(nums)):
                # get the xor_sums of these subtrees starting from node a and b
                xor_a = xor_sums[a]
                xor_b = xor_sums[b]
                
                components = []
                # a is an ancestor of b
                if is_ancestor[a][b]:
                    # three components:
                    # xor_b, xor_a - xor_b, total - xor_a
                    components = [xor_b, xor_a ^ xor_b, total ^ xor_a]
                # if b is an ancestor of a
                elif is_ancestor[b][a]:
                    # three components:
                    # xor_a, xor_b - xor_a, total - xor_a
                    components = [xor_a, xor_b ^ xor_a, total ^ xor_b]
                # both are not ancestors of each other
                else:
                    # three components:
                    # xor_a, xor_b, total - xor_a - xor_b
                    components = [xor_a, xor_b, total ^ xor_a ^ xor_b]
                
                components.sort()
                delta = components[-1] - components[0]
                res = min(res, delta)
        return res