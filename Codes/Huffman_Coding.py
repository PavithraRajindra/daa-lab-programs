## 3. Huffman Coding
import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def generate_huffman_codes(text: str) -> tuple[dict[str, str], dict[str, int]]:
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    frequency = Counter(text)
    heap = [Node(ch, freq) for ch, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    huffman_codes = {}
    def encode(node, code):
        if node:
            if node.char is not None:
                huffman_codes[node.char] = code
            encode(node.left, code + '0')
            encode(node.right, code + '1')
    encode(root, '')
    return huffman_codes, frequency

def test_generate_huffman_codes():
    text = "aabbbcccc"
    codes, freq = generate_huffman_codes(text)
    return codes, freq

print(test_generate_huffman_codes())