import sys
import math

class Node:
  def __init__(self, data):
    self.data = data
    self.child = [None for _ in range(10)]
    self.check = False

class Trie:
  def __init__(self):
    self.root = Node('')
  
  def insert(self, phone):
    tmp = self.root
    for i in phone:
      if tmp.child[i] is not None:
        tmp = tmp.child[i]
      else:
        new = Node(i)
        tmp.child[i] = new
        tmp = new
    tmp.check = True
  
  def consistency(self, phone):
    tmp = self.root
    for i in range(len(phone)):
      # 다른 문자열을 포함하고 있을 경우
      if tmp.check:
        return False
      tmp = tmp.child[phone[i]]
    return True

t = int(input())
for _ in range(t):
  n = int(input())
  phoneNumbers = []
  trie = Trie()

  for _ in range(n):
    phone = list(map(int, input()))
    trie.insert(phone)
    phoneNumbers.append(phone)
  result = True

  for number in phoneNumbers:
    result *= trie.consistency(number)
  
  if result:
    print("YES")
  else:
    print("NO")
