# FAQ - Frequently Asked Questions

## Installation & Setup

### Q: Do I need to install Ollama?
**A:** No, Ollama is optional. The scanner works perfectly with vLLM (which is included in requirements.txt). Ollama only adds advanced features.

### Q: What Python version do I need?
**A:** Python 3.8 or higher. Check with `python --version`. We recommend Python 3.10+.

### Q: I'm getting "pip: command not found"
**A:** You may need to use `pip3` instead of `pip` on macOS/Linux.

### Q: Can I use this without a virtual environment?
**A:** Yes, but we strongly recommend using a virtual environment to avoid dependency conflicts.

### Q: How much disk space do I need?
**A:** About 5-10GB:
- Python: 200MB
- Dependencies: 3-4GB
- Model cache: 1-2GB
- Buffer: ~1GB

---

## Performance

### Q: Why is my first run so slow?
**A:** The first run downloads and caches models (~2-3GB). This is a one-time operation. Subsequent runs will be much faster.

### Q: How can I make it faster?
**A:**
1. Use GPU if available (2-5x faster)
2. Increase RAM (16GB+ recommended)
3. Upgrade CPU to modern processor
4. Process smaller images

### Q: Can I process multiple images at once?
**A:** Currently, no. But batch processing is on the roadmap for v2.0. For now, process images one at a time.

### Q: What's the accuracy percentage based on?
**A:** Confidence scores come from the OCR engine's internal prediction metrics. 98%+ means the engine is very confident in its extraction.

### Q: Why different confidence scores for different lines?
**A:** Different text:
- Clear printed fonts → Higher confidence (98%+)
- Faded/damaged text → Lower confidence (70-90%)
- Handwriting → Variable confidence (50-95%)

---

## GPU & Hardware

### Q: Do I need a GPU?
**A:** No. GPU is optional and speeds up processing 2-5x. CPU works fine but slower.

### Q: Which GPUs are supported?
**A:** NVIDIA GPUs with CUDA Compute Capability 3.0+:
- GeForce GTX 960+
- RTX 2060+
- A100, H100, etc.

### Q: What about AMD/Intel GPUs?
**A:** Not directly supported by vLLM yet. AMD users can use ROCm, Intel users can use OpenVINO (future support).

### Q: I have Apple Silicon (M1/M2/M3). Will it work?
**A:** Yes! Use MPS (Metal Performance Shaders):
```bash
export PYTORCH_ENABLE_MPS_FALLBACK=1
python3 Chandra-OCR-Scanner-IT.py
```

### Q: How much VRAM do I need for GPU?
**A:**
- Minimum: 4GB (may be slow)
- Recommended: 8GB+
- Professional: 12GB+

### Q: Can I use multiple GPUs?
**A:** Not in current version, but multi-GPU support is planned.

---

## Image Processing

### Q: What image formats are supported?
**A:**
- ✅ PNG (.png)
- ✅ JPEG (.jpg, .jpeg)
- ✅ BMP (.bmp)
- ✅ TIFF (.tiff)
- ✅ WebP (.webp)

### Q: What's the best image format?
**A:** PNG for best quality (lossless compression).

### Q: What about PDF files?
**A:** Chandra supports PDFs natively. Select a PDF in the file picker.

### Q: Can I process really large images?
**A:** Yes, but:
- Very large images (8K+) may be slow
- May require more VRAM
- Consider downsampling for faster processing

### Q: Should I rotate/fix the image first?
**A:** Chandra handles various angles, but straight images work best. Heavy rotation or distortion may reduce accuracy.

### Q: Can I pre-process images?
**A:** Not in the current UI, but you can use external tools like:
- ImageMagick: `convert input.jpg -rotate 90 output.jpg`
- Pillow in Python
- GIMP (GUI)

---

## Language & Accuracy

### Q: What languages are supported?
**A:** The tool supports 10+ languages including:
- Spanish, English, Portuguese, French
- German, Italian, Chinese, Japanese
- Russian, Arabic, and more

### Q: Does it auto-detect language?
**A:** Yes! The "auto" option detects language automatically.

### Q: Why is accuracy lower for my language?
**A:** Some languages have:
- Fewer training data
- Complex scripts (requires special handling)
- Limited fonts in training set

### Q: Can I improve accuracy?
**A:** Tips:
1. Use clear images (good lighting, focus)
2. Avoid skewed/rotated text
3. Remove backgrounds for clarity
4. Use high resolution (300+ DPI)
5. Process terminals with monospace fonts (works great!)

### Q: Handwriting recognition accuracy?
**A:** Typically 50-90% depending on:
- Handwriting clarity
- Pen pressure consistency
- Paper condition
- Language complexity

### Q: Any tips for terminal output?
**A:** Great news! The scanner excels at:
- Monospaced fonts (code, terminals)
- High contrast text
- Standard ASCII characters

---

## Privacy & Security

### Q: Does my data get sent to the cloud?
**A:** No! 100% local processing. Zero data sent anywhere.

### Q: Are there any privacy logs?
**A:** No logs or tracking. Everything runs on your machine.

### Q: Can I process sensitive data?
**A:** Yes! Safe for:
- Financial documents
- Personal information
- Business secrets
- Medical records
- Classified data

All processing stays on your computer.

### Q: Is the code open source?
**A:** Yes! MIT License. Fully open and auditable.

---

## Troubleshooting

### Q: "No module named 'torch'"
**A:** Install PyTorch:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### Q: "CUDA out of memory"
**A:** Solutions:
1. Use CPU mode: `set CUDA_VISIBLE_DEVICES=`
2. Close other GPU apps
3. Reduce image size
4. Upgrade GPU memory

### Q: "vLLM server not responding"
**A:** Check installation:
```bash
pip install vllm --upgrade
python -c "import vllm; print('OK')"
```

### Q: Application hangs on startup
**A:** Usually downloading models. This is normal for first run. Wait or check:
```bash
ls ~/.cache/torch/
```

### Q: Can't find image file I selected
**A:** Make sure:
- File path has no special characters
- File is not in use by another program
- File hasn't been deleted
- Sufficient disk space

### Q: Getting permission denied errors
**A:**
```bash
# Linux/macOS
chmod +x Chandra-OCR-Scanner-IT.py

# Windows - Run as Administrator
```

---

## Advanced Usage

### Q: Can I use this as a Python library?
**A:** Not in current version, but:
```python
import subprocess
result = subprocess.run(['chandra', 'input.png', 'output_dir'])
```

### Q: Can I automate processing?
**A:** Yes, with command line:
```bash
chandra image.png output_dir --method vllm
```

### Q: Custom configuration?
**A:** Future versions will support config files. Currently edit:
```python
# In the Python file, near the top
GPU_ENABLED = True
CONFIDENCE_THRESHOLD = 0.80
```

### Q: How do I increase detail level?
**A:** The scanner already uses maximum detail. To get even more:
1. Increase image resolution
2. Use higher quality source images
3. Process sections separately

---

## Contributing & Development

### Q: Can I contribute?
**A:** Yes! See [CONTRIBUTING.md](CONTRIBUTING.md)

### Q: How do I report bugs?
**A:** Open an issue on [GitHub](https://github.com/comandoit/Chandra-OCR-Scanner-IT/issues) with:
- Exact error message
- Steps to reproduce
- Your environment (OS, Python version, GPU?)
- Screenshot/attachment if relevant

### Q: Can I request a feature?
**A:** Yes! Open an issue with your use case and requirements.

### Q: How do I contribute code?
**A:**
1. Fork the repository
2. Create feature branch
3. Make changes
4. Submit pull request
5. See [CONTRIBUTING.md](CONTRIBUTING.md) for details

---

## Updates & Releases

### Q: How often are releases?
**A:**
- Bug fixes: As needed
- Features: Quarterly (Q)
- Major version: Annually

### Q: How do I update?
**A:**
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

### Q: What version am I using?
**A:** Check the header in:
```bash
grep "version" Chandra-OCR-Scanner-IT.py
```

### Q: Is there a changelog?
**A:** Yes! See [CHANGELOG.md](CHANGELOG.md)

---

## Comparison with Other Tools

### Q: How does this compare to Tesseract?
**A:**
- Chandra: Better for complex layouts, AI-powered
- Tesseract: More languages, mature ecosystem

### Q: vs EasyOCR?
**A:**
- Chandra: Better terminal fonts, faster with vLLM
- EasyOCR: Simpler setup, lighter weight

### Q: vs AWS Textract?
**A:**
- Chandra: Free, local, private
- Textract: More accurate, but costs money and requires internet

---

## Still Have Questions?

1. Check [README.md](README.md) for overview
2. See [SETUP.md](SETUP.md) for installation
3. Review [CONTRIBUTING.md](CONTRIBUTING.md) for development
4. Open [GitHub Issues](https://github.com/comandoit/Chandra-OCR-Scanner-IT/issues)
5. Contact: [info@comandoit.com](mailto:info@comandoit.com)

---

**Last Updated**: 2025-04-05
**Maintained by**: ComandoIT.com™
