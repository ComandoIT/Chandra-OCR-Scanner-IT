# 👁️ Chandra-OCR Scanner: IT-Focused AI Vision

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20macOS-lightgrey)](https://github.com)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)](https://github.com)

Stop manually transcribing data from screenshots, hosting invoices, or terminal outputs. **Chandra-OCR Scanner** is the official **ComandoIT.com** implementation for high-precision text extraction using Deep Learning.

While traditional OCR tools struggle with complex layouts or monospaced fonts, this tool is specifically tuned for IT environments and technical documentation.

---

## 🚀 Key Features

✅ **Terminal Optimized**
Excellence at reading monospaced fonts from CLI captures and code blocks.

✅ **Layout Intelligence**
Understands the structure of hosting dashboards, terminal outputs, and invoices with precision.

✅ **Confidence Scoring**
Provides accuracy percentages for every extracted string with detailed analytics.

✅ **GPU & CPU Support**
Automatic device detection with GPU acceleration (CUDA) or CPU fallback.

✅ **Multi-Language**
Supports 10+ languages including Spanish, English, Portuguese, Chinese, and more.

✅ **Lightweight & Fast**
Runs locally without expensive cloud API dependencies. Truly offline-capable.

✅ **Visual Analytics**
Beautiful charts showing confidence distribution, statistics, and processed images.

✅ **Easy GUI**
File picker dialog + language selector for non-CLI users.

---

## 🛠️ Installation

### Prerequisites
- **Python 3.8+**
- **Ollama** (optional, for advanced features)
- **CUDA Toolkit** (optional, for GPU acceleration)

### Step 1: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
# Install all required packages
pip install chandra-ocr[vllm] vllm torch pillow matplotlib numpy

# On Windows, you might need to install torch separately
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Step 3: Install Ollama (Optional)
If you want advanced AI-powered features:
- **Windows/macOS**: Download from [ollama.ai/download](https://ollama.ai/download)
- **Linux**: `curl https://ollama.ai/install.sh | sh`

### Step 4: Run the Scanner
```bash
python Chandra-OCR-Scanner-IT.py
```

---

## 📖 Usage

### Interactive Mode (Recommended)

1. **Run the script**
   ```bash
   python Chandra-OCR-Scanner-IT.py
   ```

2. **Select Processing Device**
   ```
   ⚙️  Selecciona el dispositivo para procesamiento:
     1. 🎮 GPU (RÁPIDO) - NVIDIA GeForce RTX 3060
     2. 💾 CPU/RAM (LENTO pero COMPATIBLE)
   ```
   - Choose **GPU** for 2-5x faster processing
   - Choose **CPU** for compatibility with any machine

3. **Confirm Language Detection**
   ```
   🌐 Chandra detecta automáticamente el idioma
   ¿Continuar? (s/n):
   ```

4. **Select Image**
   - GUI file picker opens
   - Select PNG, JPG, or other image formats

5. **View Results**
   - Extracted text displayed in console
   - Beautiful charts with confidence scores
   - Breakdown of accuracy levels (Excellent/Acceptable/Low)

### Example Output
```
🚀 Chandra OCR Scanner Avanzado
════════════════════════════════════════════════════════════════════════════════
© 2025 www.comandoit.com™

📦 Verificando dependencias Python...
✅ chandra-ocr[vllm]       OK
✅ vllm                     OK
✅ torch                    OK
✅ pillow                   OK
✅ matplotlib               OK
✅ numpy                    OK

🔄 Procesando: C:/Users/ideas/Downloads/escritura manual.png...
   Dispositivo: 🎮 GPU
   Método: vLLM

✅ Procesamiento completado

════════════════════════════════════════════════════════════════════════════════
📄 TEXTO EXTRAÍDO
════════════════════════════════════════════════════════════════════════════════

[Bloque 1] Confianza: 98.0%
Texto: Documento importante con escritura legible

[Bloque 2] Confianza: 96.5%
Texto: Contenido técnico extraído con precisión
```

---

## 📊 Visual Analytics Dashboard

After processing, you'll see a comprehensive 4-panel dashboard:

1. **Confidence by Block** (Horizontal Bar Chart)
   - Color-coded: Green (>80%), Yellow (60-80%), Red (<60%)
   - Shows confidence for each text block

2. **Confidence Distribution** (Histogram)
   - Visual distribution of accuracy across all blocks
   - Shows average confidence line

3. **Original Image**
   - Preview of the processed image

4. **Statistics Panel**
   - Total blocks detected
   - Average/Max/Min confidence
   - Count of blocks by confidence level

---

## ⚙️ Advanced Configuration

### Force CPU Processing (No GPU)
```bash
# Set environment variable before running
set CUDA_VISIBLE_DEVICES=
python Chandra-OCR-Scanner-IT.py
```

### Use Specific GPU
```bash
set CUDA_VISIBLE_DEVICES=0  # Use GPU 0
python Chandra-OCR-Scanner-IT.py
```

### Enable Ollama Integration
If Ollama is running locally:
```bash
ollama serve  # In separate terminal
python Chandra-OCR-Scanner-IT.py
```

---

## 🔧 Troubleshooting

### ❌ "chandra-ocr not found"
```bash
pip install chandra-ocr[vllm] --upgrade
```

### ❌ "CUDA out of memory"
- Use CPU mode instead of GPU
- Or reduce image resolution before processing

### ❌ "No module named 'torch'"
```bash
 pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### ❌ "File not found" error
- Use absolute paths for image files
- Check file permissions
- Ensure file is not corrupted

### ❌ "vLLM server not responding"
- Ensure vLLM is installed: `pip install vllm`
- Check available disk space for model cache
- Try CPU method instead

---

## 📋 Supported Formats

### Input Images
- ✅ PNG (.png)
- ✅ JPEG (.jpg, .jpeg)
- ✅ BMP (.bmp)
- ✅ TIFF (.tiff, .tif)
- ✅ WebP (.webp)

### Output Formats
- 📝 Console Output
- 📊 Matplotlib Graphs
- 📄 Markdown (.md)
- 🌐 HTML (.html)

---

## 🌍 Supported Languages

| Language | Code |
|----------|------|
| Español (Spanish) | es |
| English | en |
| Português (Portuguese) | pt |
| Français (French) | fr |
| Deutsch (German) | de |
| Italiano (Italian) | it |
| 中文 (Simplified Chinese) | ch_sim |
| 日本語 (Japanese) | ja |
| Русский (Russian) | ru |
| والعربية (Arabic) | ar |

---

## 💡 Use Cases

### IT & DevOps
- Extract text from terminal screenshots
- Parse configuration file contents
- Digitize server logs
- Read CLI output from automation

### Finance & Administration
- Process hosting invoices and receipts
- Extract data from financial reports
- Digitize handwritten documents
- OCR bank statements

### Documentation
- Convert scanned documents to text
- Extract text from PDF screenshots
- Build searchable document archives
- Preserve legacy documentation

### Quality Assurance
- Extract test results from screenshots
- Digitize QA reports
- Parse error logs from images
- Document test cases visually

---

## 📈 Performance Metrics

| Device | Speed | VRAM | RAM | Best For |
|--------|-------|------|-----|----------|
| **RTX 3060** | ~2-3 sec/image | 12GB | 8GB | Most users |
| **RTX 4090** | ~0.5-1 sec/image | 24GB | 16GB | High volume |
| **CPU (i7)** | ~15-30 sec/image | N/A | 16GB | Testing |
| **CPU (i5)** | ~30-60 sec/image | N/A | 8GB | Fallback |

---

## 🔐 Privacy & Security

✅ **100% Local Processing** - No data sent to external servers
✅ **No Cloud Dependencies** - Works completely offline
✅ **No Tracking** - Zero telemetry or analytics
✅ **Open Source** - Fully auditable code

Your data never leaves your machine. Everything runs locally.

---

## 🤝 Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**ComandoIT.com™**
IT Solutions & Automation Experts

- 🌐 Website: [www.comandoit.com](https://www.comandoit.com)
- 📧 Contact: [info@comandoit.com](mailto:info@comandoit.com)
- 🐙 GitHub: [@comandoit](https://github.com/comandoit)

---

## ⭐ Support

If you find this project helpful:

- ⭐ Star the repository
- 🐛 Report issues on GitHub
- 💬 Share your use cases
- 🔄 Contribute improvements

---

## 🙏 Acknowledgments

- **Chandra OCR** - Underlying OCR engine
- **vLLM** - Fast inference engine
- **PyTorch** - Deep learning framework
- **Matplotlib** - Visualization

---

## 📡 API Reference

### Main Functions

#### `procesar_ocr(ruta_archivo, idioma, dispositivo)`
Process an image and extract text.

**Parameters:**
- `ruta_archivo` (str): Path to image file
- `idioma` (str): Language code ("auto" for auto-detect)
- `dispositivo` (str): "gpu" or "cpu"

**Returns:**
- List of Bloque namedtuples with `text` and `confidence`

#### `mostrar_resultados(ruta_imagen, bloques)`
Display analytical charts for extracted text.

**Parameters:**
- `ruta_imagen` (str): Path to original image
- `bloques` (list): Results from procesar_ocr()

#### `seleccionar_dispositivo()`
Interactive device selection menu.

**Returns:**
- "gpu" or "cpu"

---

## 📞 FAQ

**Q: Can I use this without GPU?**
A: Yes! The tool automatically falls back to CPU if GPU is unavailable.

**Q: What's the accuracy rate?**
A: Typically 95-99% for clean printed text, 85-95% for handwriting.

**Q: How much disk space is needed?**
A: ~5GB for model downloads on first run.

**Q: Can I process batch images?**
A: Currently supports single images. Batch mode coming soon!

**Q: Does it work offline?**
A: Yes, completely offline after initial setup.

---

**Made with ❤️ by ComandoIT.com™**
