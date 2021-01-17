class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        idx_sorted = len(arr)-1
        for tar in range(len(arr), 0, -1):
            for idx, val in enumerate(arr):
                if tar == val:
                    if idx > 0 or idx_sorted > 0:
                        result.append(idx+1)
                        arr = list(reversed(arr[:idx+1])) + arr[idx+1:]
                        result.append(idx_sorted+1)
                        arr = list(reversed(arr[:idx_sorted+1])) + arr[idx_sorted+1:]
                    idx_sorted -= 1
        return result