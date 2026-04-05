# 👁️ Chandra-OCR Scanner: IT-Focused AI Vision

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![OCR](https://img.shields.io/badge/OCR-Chandra-orange.svg)

Stop manually transcribing data from screenshots, hosting invoices, or terminal outputs. **Chandra-OCR Scanner** is the official **ComandoIT.com** implementation for high-precision text extraction using Deep Learning.

While traditional OCR tools struggle with complex layouts or monospaced fonts, this tool is specifically tuned for IT environments and technical documentation.

---

## 🚀 Key Features

* **Terminal Optimized:** Excellent at reading monospaced fonts from CLI captures.
* **Layout Intelligence:** Understands the structure of hosting dashboards and invoices.
* **Confidence Scoring:** Provides accuracy percentages for every extracted string.
* **Lightweight & Fast:** Runs locally without expensive cloud API dependencies.

---

## 🛠️ Installation

Set up your environment and install the core engine:

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install the arsenal
pip install chandra-ocr
