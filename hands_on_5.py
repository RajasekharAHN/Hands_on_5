# -*- coding: utf-8 -*-
"""Hands_on_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
   https://colab.research.google.com/drive/1DmJT06vnhn5fG-XSa80ezVGI5d9r2CDO#scrollTo=91X61K5zTVjX
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def build_min_heap(self, array):
        self.heap = array
        n = len(self.heap)
        for i in range(n // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def pop(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root

if __name__ == "__main__":
    min_heap = MinHeap()

    arr = list(map(int, input("Enter a list of integers: ").split()))

    min_heap.build_min_heap(arr)

    print("Root node removed:", min_heap.pop())
    print("Heap after removal:", min_heap.heap)

