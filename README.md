# Huffman Text Compressor

A full-stack web application built with Python and Streamlit that performs lossless text compression using the classic **Huffman Encoding** algorithm. 

This tool analyzes the frequency of characters in a given text, builds an optimal binary prefix tree, and encodes the data to significantly reduce its file size compared to standard 8-bit character encoding.

## Deployment link: [Huffman-Compressor](https://textcompress.streamlit.app/)

## Features

* **Text-Based Compression:** Paste raw text or upload a `.txt` file to instantly generate a compressed binary payload.
* **Lossless Decompression:** 100% accurate text reconstruction using custom-generated JSON metadata dictionaries.
* **Interactive Web Interface:** A clean, dual-tab UI built with Streamlit for seamless file uploading, processing, and downloading.
* **Real-Time Analytics:** Calculates and displays the original bit size, compressed bit size, and the total space saved as a percentage.
* **Under the Hood:** Automatically manages bit-padding and binary-to-byte array conversions required for standard file compression workflows.

## Technology Stack

* **Language:** Python 3.x
* **Frontend/Framework:** Streamlit
* **Algorithms:** Huffman Coding, Binary Tree Traversal, Min-Heaps (`heapq`)
* **Deployment:** Streamlit Community Cloud

## How to Run Locally

To run this project on your local machine, follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/huffman-compressor.git](https://github.com/your-username/huffman-compressor.git)
cd huffman-compressor
```

2. Set up a virtual environment (Recommended)
Mac/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
   
```bash
pip install -r requirements.txt
```

4. Launch the application

```bash
streamlit run app.py
```

# Usage Guide
## Compressing Text
Navigate to the Compress tab.

Type/paste your text, or upload a standard `.txt` file.

The app will generate an optimal Huffman tree and encode the text.

Download the `compressed.bin` (the compressed payload) and the metadata.json (the lookup table required for reconstruction).

## Decompressing a File
Navigate to the Decompress tab.

Upload both the `compressed.bin` and `metadata.json` files generated during the compression phase.

The app will reconstruct the original text bit-by-bit and display it on the screen.
