import sys
class MaxHeap:

  def __init__(self, max):
    self.max = max
    self.size = 0
    self.heap = [0] * (self.max + 1)
    self.heap[0] = sys.maxsize
    self.root = 1

  def parent(self, pos):
    return pos//2

  def left(self, pos):
    return pos*2

  def right(self, pos):
    return pos*2 + 1
  
  def isLeaf(self, pos):
    if pos >=self.size//2 and pos <= self.size:
      return True
    return False
  
  def swap(self, pos1, pos2):
    self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

  def maxHeapify(self, pos):
    if not self.isLeaf(pos):
      if self.heap[pos] < self.heap[self.left(pos)] or self.heap[pos] < self.heap[self.right(pos)]:
        if self.heap[self.left(pos)] > self.heap[self.right(pos)]:
          self.swap(pos, self.left(pos))
          self.maxHeapify(self.left(pos))
        else:
          self.swap(pos, self.right(pos))
          self.maxHeapify(self.right(pos))

  def insert(self, val):
    if self.size >= self.max:
      print("Heap is full")
      return
    self.size += 1
    self.heap[self.size] = val

    current = self.size
    while self.heap[current] > self.heap[self.parent(current)]:
      self.swap(current, self.parent(current))
      current = self.parent(current)
      
  def printHeap(self):
    if self.size == 0:
      print("Heap is empty")
      return
    for i in range(1, self.size//2 + 1):
      print("Parent:", self.heap[i], "| Left Child:", self.heap[2*i], "| Right Child:", self.heap[2*i + 1])
  
  def delete(self):
    if self.size == 0:
      print("Heap is empty")
      return None
    popped = self.heap[self.root]
    self.heap[self.root] = self.heap[self.size]
    self.size -= 1
    self.maxHeapify(self.root)
    return popped

  def get_max(self):
    if self.size == 0:
      print("Heap is empty")
      return None
    return self.heap[1]

size = int(input("Enter the size of the heap: "))
maxheap = MaxHeap(size)
maxheap.insert(32)
maxheap.insert(45)
maxheap.insert(22)
maxheap.insert(11)
maxheap.printHeap()
print(f"Max element: {maxheap.get_max()}")
maxheap.insert(49)
maxheap.insert(33)
maxheap.insert(19)
print(f"Deleteing the max element: {maxheap.delete()}")
maxheap.insert(26)
maxheap.insert(20)
maxheap.insert(40)
maxheap.printHeap()
print(f"Max element: {maxheap.get_max()}")