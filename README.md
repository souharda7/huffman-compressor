# 📦 Universal Huffman File Compressor

A full-stack web application built with Python and Streamlit that performs lossless data compression using the Huffman Encoding algorithm. 

Unlike basic text compressors, this tool operates at the **byte-level (8-bit)**, meaning it can ingest, analyze, and compress *any* uncompressed raw file type by building an optimal prefix code tree based on the frequency of raw byte values.

## ✨ Features

* **Universal Byte-Level Compression:** Reads files as raw byte arrays, allowing for the compression of highly redundant data files (Log files, raw `.bmp` images, large unminified codebases, etc.).
* **Lossless Decompression:** 100% accurate file reconstruction using custom-generated JSON metadata dictionaries.
* **Interactive Web Interface:** A clean, dual-tab UI built with Streamlit for seamless file uploading, processing, and downloading.
* **Real-Time Analytics:** Calculates and displays original size, compressed size, and total space saved.
* **Metadata Handling:** Automatically manages padding bits and binary mapping structures required for standard file compression workflows.

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **Frontend/Framework:** Streamlit
* **Algorithms:** Huffman Coding, Binary Tree Traversal, Min-Heaps (`heapq`)
* **Deployment:** Streamlit Community Cloud

## 🚀 How to Run Locally

To run this project on your local machine, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/huffman-compressor.git](https://github.com/your-username/huffman-compressor.git)
cd huffman-compressor
```
2. Set up a virtual environment (Recommended)
Mac/Linux:

Bash
python -m venv venv
source venv/bin/activate
Windows:

Bash
python -m venv venv
venv\Scripts\activate
3. Install dependencies
Bash
pip install -r requirements.txt
4. Launch the application
Bash
streamlit run app.py
📖 Usage Guide
Compressing a File
Navigate to the Compress tab.

Upload any uncompressed file.

The app will generate an optimal Huffman tree and encode the file.

Download the compressed.bin (the compressed payload) and the metadata.json (the lookup table required for reconstruction).

Decompressing a File
Navigate to the Decompress tab.

Upload both the compressed.bin and metadata.json files generated during the compression phase.

The app will reconstruct the original file bit-by-bit.

Download the restored file, which will automatically retain its original extension.
