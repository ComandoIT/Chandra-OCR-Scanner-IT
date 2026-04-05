# Setup Guide - Chandra-OCR Scanner

Complete step-by-step setup instructions for all operating systems.

## 📋 Prerequisites

- **Python 3.8 or higher** (check with `python --version`)
- **Pip package manager** (usually comes with Python)
- **4GB RAM minimum** (8GB+ recommended)
- **2GB disk space** for dependencies

### Optional but Recommended
- **NVIDIA GPU** (CUDA-compatible) for 5x faster processing
- **Ollama** for advanced features

---

## 🪟 Windows Installation

### Step 1: Install Python

1. Download from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **IMPORTANT**: Check "Add Python to PATH"
4. Click "Install Now"

Verify installation:
```bash
python --version
pip --version
```

### Step 2: Clone Repository

```bash
# Using Git (if installed)
git clone https://github.com/comandoit/Chandra-OCR-Scanner-IT.git
cd Chandra-OCR-Scanner-IT

# Or download as ZIP and extract
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the start of your terminal line.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install with GPU support:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

### Step 5: Run Application

```bash
python Chandra-OCR-Scanner-IT.py
```

### Optional: Install Ollama

1. Download from [ollama.ai/download](https://ollama.ai/download)
2. Run the installer
3. Verify: `ollama --version`

---

## 🐧 Linux Installation

### Ubuntu/Debian

```bash
# Update system
sudo apt update && sudo apt upgrade

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Clone repository
git clone https://github.com/comandoit/Chandra-OCR-Scanner-IT.git
cd Chandra-OCR-Scanner-IT

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python3 Chandra-OCR-Scanner-IT.py
```

### For GPU (CUDA) on Linux

```bash
# Install NVIDIA drivers
sudo apt install nvidia-driver-xxx  # Replace xxx with your version

# Install CUDA cuDNN
# Follow: https://developer.nvidia.com/cudnn

# Install torch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Install Ollama on Linux

```bash
curl https://ollama.ai/install.sh | sh
```

---

## 🍎 macOS Installation

### Using Homebrew

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Clone repository
git clone https://github.com/comandoit/Chandra-OCR-Scanner-IT.git
cd Chandra-OCR-Scanner-IT

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python3 Chandra-OCR-Scanner-IT.py
```

### Install Ollama on macOS

```bash
brew install ollama
# Or download from https://ollama.ai/download
```

---

## 🎮 GPU Setup (All Platforms)

### NVIDIA GPU (GeForce, RTX, A100, etc.)

```bash
# Check if CUDA-capable
nvidia-smi

# Install PyTorch with CUDA
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Verify GPU support
python -c "import torch; print(torch.cuda.is_available())"
```

Output should show `True` if GPU is available.

### Apple Silicon (M1/M2/M3)

```bash
# Install with native support
pip install torch torchvision torchaudio

# Enable MPS (Metal Performance Shaders)
# Set environment variable:
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

---

## 🔍 Verification

Test your installation:

```bash
# Check Python
python --version

# Check pip packages
pip list | grep -E "torch|chandra|matplotlib"

# Check GPU (if applicable)
python -c "import torch; print('GPU:', torch.cuda.is_available())"

# Check Ollama (if installed)
ollama --version
```

Expected output:
```
Python 3.10.0  ✅
torch              ✅
chandra-ocr        ✅
matplotlib         ✅
numpy              ✅
GPU: True          ✅
ollama version x.x.x ✅
```

---

## 🆘 Troubleshooting

### "Python not found"
- Add Python to PATH (Windows)
- Use `python3` instead of `python` (macOS/Linux)

### "ModuleNotFoundError: No module named 'torch'"
```bash
pip install torch --index-url https://download.pytorch.org/whl/cu118
```

### "CUDA out of memory"
- Run with CPU instead: `set CUDA_VISIBLE_DEVICES=`
- Reduce image resolution
- Upgrade GPU or add more VRAM

### "venv activation not working"
```bash
# Windows - use full path
C:\path\to\venv\Scripts\activate

# Linux/macOS - check permissions
chmod +x venv/bin/activate
source venv/bin/activate
```

### "Permission denied" errors
```bash
# Linux/macOS
chmod +x Chandra-OCR-Scanner-IT.py
sudo chown -R $USER:$USER .

# Windows - Run as Administrator
```

### "Ollama command not found"
```bash
# Add Ollama to PATH
# Windows: Set environment variable OLLAMA_HOME
# Linux/macOS: Already in PATH if installed via script
```

---

## 🚀 Quick Start

After setup, running is simple:

```bash
# Windows
venv\Scripts\activate
python Chandra-OCR-Scanner-IT.py

# Linux/macOS
source venv/bin/activate
python3 Chandra-OCR-Scanner-IT.py
```

Then:
1. Select **GPU** or **CPU**
2. Confirm language detection
3. Pick an image file
4. View results with beautiful charts!

---

## 📊 System Requirements by Use Case

### Minimal (Testing)
- CPU: Intel i5/AMD Ryzen 5
- RAM: 8GB
- Disk: 2GB
- GPU: Not required (will use CPU)

### Recommended (Daily Use)
- CPU: Intel i7/AMD Ryzen 7
- RAM: 16GB
- Disk: 10GB
- GPU: NVIDIA RTX 3060 / 4060 (optional but faster)

### Professional (Production)
- CPU: Intel Xeon/AMD Ryzen Threadripper
- RAM: 32GB+
- Disk: 50GB+
- GPU: NVIDIA RTX 4080 / A6000 / H100

---

## 🔧 Environment Variables

```bash
# Force CPU mode (disable GPU)
set CUDA_VISIBLE_DEVICES=

# Use specific GPU
set CUDA_VISIBLE_DEVICES=0

# Debug mode (verbose output)
set DEBUG=1

# Custom model cache
set TRANSFORMERS_CACHE=/path/to/cache
```

---

## 📚 Next Steps

1. [Read the README](README.md)
2. [Check out examples](examples/)
3. [Review troubleshooting](TROUBLESHOOTING.md)
4. [Contribute!](CONTRIBUTING.md)

---

**Need help?** Open an issue on [GitHub](https://github.com/comandoit/Chandra-OCR-Scanner-IT/issues)

Happy scanning! 🚀
