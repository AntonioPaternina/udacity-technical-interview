# taken from http://love-python.blogspot.com.co/2013/10/iterative-binary-search-in-python.html

def binary_search_iterative(li, left, right, key):
  while True:
    if left > right:
      return -1
    mid = (left + right) / 2
    if li[mid] == key:
      return mid
    if li[mid] > key:
      right = mid - 1
    else:
      left = mid + 1

if __name__ == "__main__":
  li = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
  left = 0
  right = len(li)
  for key in  [8, 6, 1, 12, 7]:
    index = binary_search_iterative(li, left, right, key)
    print key, index
