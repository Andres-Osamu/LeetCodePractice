from itertools import permutations

class Solution(object):
    def numTilePossibilities(self, tiles):
        # Generate permutations of lengths 1 to 3       
        permValues = []
        count = 0
        for r in range(1, len(tiles) + 1):
            perms = permutations(tiles, r)
            print(f"Permutations of length {r}:")
            for perm in perms:
                permValues.append(perm)
                count += 1

        print(count)
        product = list(set(permValues))
        print(len(product))

    # Define the objects

tiles = ['A', 'B', 'A']

obj = Solution()
obj.numTilePossibilities(tiles)

