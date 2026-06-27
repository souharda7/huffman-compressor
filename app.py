import streamlit as st
import json
import heapq

class Node :
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
def get_freq(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    return freq

def build_tree(freq):
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node (None, node1.freq + node2.freq)

        merged.left, merged.right = node1, node2
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def build_codes(root):
    if not root:
        return {}
    
    codes = {}

    def traverse(node, curr_code):
        if node.char is not None:
            codes[node.char] = curr_code if curr_code else "0"
            return
        if node.left:
            traverse(node.left, curr_code+"0")
        if node.right:
            traverse(node.right, curr_code+"1")
    
    traverse(root, "")
    return codes

def compress(text):
    if not text:
        return bytearray(), {}, 0
    
    freq = get_freq(text)
    root = build_tree(freq)
    codes = build_codes(root)

    encoded_text = "".join([codes[char] for char in text])
    padding = 8 - (len(encoded_text)%8)
    encoded_text += "0" * padding
    byte_array = bytearray()

    for i in range(0, len(encoded_text), 8):
        byte = encoded_text[i:i+8]
        byte_array.append(int(byte, 2)) # to base 2

    return byte_array, codes, padding

def decompress(compressed_bytes, code_map, padding):
    binary_string = ""

    for byte in compressed_bytes:
        binary_string += f"{byte:08b}"

    if padding > 0:
        binary_string = binary_string[:-padding]

    reverse_map = {v : k for k, v in code_map.items()}

    decoded_text = ""
    current_bits = ""

    for bit in binary_string:
        current_bits += bit
        if current_bits in reverse_map:
            decoded_text += reverse_map[current_bits]
            current_bits = ""

    return decoded_text


st.title("Huffman Text Compressor")

tab1, tab2 = st.tabs(["Compress", "Decompress"])

with tab1:
    st.header("Compress text")
    user_input = st.text_area("Enter text to compress : ", height=200)

    if user_input:
        compressed_bytes, code_map, padding = compress(user_input)

        orig_size = len(user_input)*8
        comp_size = len(compressed_bytes)*8

        ratio = (1 - (comp_size/orig_size))*100 if orig_size>0 else 0

        col1, col2, col3 = st.columns(3)
        col1.metric("Original Size", f"{orig_size} bits")
        col2.metric("Compressed Size", f"{comp_size} bits")
        col3.metric("Space Saved", f"{ratio:.2f}%")

        st.subheader("Generated Huffman Codes")
        st.json(code_map)

        st.download_button(
            label="Download Compressed File (.bin)", 
            data=bytes(compressed_bytes), 
            file_name="compressed.bin", 
            mime="application/octet-stream"
        )

        metadata = {
            "code-map" : code_map,
            "padding" : padding
        }

        st.download_button(
            label = "Download Metadata (.json)",
            data=json.dumps(metadata),
            file_name="metadata.json",
            mime="application/json"
        )

with tab2 :
    st.header("Decompress File")

    bin_file = st.file_uploader("Upload Compressed File (.bin)", type=["bin"])
    metadata_file = st.file_uploader("Upload Metadata File (.json)", type=["json"])

    if bin_file and metadata_file:
        compressed_bytes = bin_file.read()
        metadata = json.load(metadata_file)

        code_map = metadata["code_map"]
        padding = metadata["padding"]

        decompressed_text = decompress(compressed_bytes, code_map, padding)

        st.subheader("Decompressed Text")
        st.text_area("Result : ", value = decompressed_text, height=200, disabled=True)