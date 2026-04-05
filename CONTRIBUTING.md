# Contributing to Chandra-OCR Scanner

Thank you for your interest in contributing to the Chandra-OCR Scanner project! We welcome contributions from the community.

## 🤝 How to Contribute

### Reporting Bugs

Before creating a bug report, please check the [issues](https://github.com/comandoit/Chandra-OCR-Scanner-IT/issues) to avoid duplicates.

When filing a bug report, include:
- **Title**: Clear, descriptive title
- **Description**: What happened and what you expected
- **Steps to Reproduce**: Exact steps to reproduce the issue
- **Environment**: OS, Python version, hardware (GPU/CPU)
- **Attachments**: Screenshots, error logs, or test images (if safe to share)

### Suggesting Enhancements

Enhancement suggestions are welcome! When suggesting, include:
- **Use case**: Why this would be useful
- **Expected behavior**: How it should work
- **Examples**: Code samples or mockups if applicable

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Chandra-OCR-Scanner-IT.git
   cd Chandra-OCR-Scanner-IT
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make your changes**
   - Write clean, commented code
   - Follow PEP 8 style guidelines
   - Test your changes thoroughly

4. **Commit with clear messages**
   ```bash
   git commit -m "Add feature: Clear description of what was added"
   git commit -m "Fix: Clear description of what was fixed"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Open a Pull Request**
   - Reference related issues using `#issue_number`
   - Describe your changes clearly
   - Include before/after examples if applicable

## 📋 Contribution Guidelines

### Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and modular

### Documentation
- Update README.md if adding features
- Add docstrings to new functions
- Include usage examples
- Update this file if process changes

### Testing
- Test on multiple Python versions (3.8+)
- Test on both GPU and CPU
- Test with different image formats
- Include test cases for new features

### Commit Messages
Use clear, descriptive commit messages:
```
Add: New feature description
Fix: Bug fix description
Update: Documentation or refactoring
Remove: Deprecated code or files
```

## 🏗️ Project Structure

```
Chandra-OCR-Scanner-IT/
├── Chandra-OCR-Scanner-IT.py  # Main application
├── README.md                   # Documentation
├── LICENSE                     # MIT License
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
├── CONTRIBUTING.md            # This file
└── docs/                      # Additional documentation (future)
```

## 🧪 Testing

Before submitting a PR, please test your changes:

```bash
# Test with GPU
python Chandra-OCR-Scanner-IT.py

# Test with CPU (set environment variable)
set CUDA_VISIBLE_DEVICES=
python Chandra-OCR-Scanner-IT.py

# Test with different image formats
# - PNG files
# - JPEG files
# - BMP files
```

## 📝 Areas for Contribution

### High Priority
- [ ] Batch image processing
- [ ] Command-line arguments support
- [ ] Configuration file support
- [ ] Performance optimization

### Medium Priority
- [ ] Additional language support
- [ ] Export to different formats (PDF, DOCX)
- [ ] Improved error handling
- [ ] Unit tests

### Low Priority
- [ ] Dark mode UI
- [ ] Theme customization
- [ ] Plugin system

## 🐛 Known Issues

Check [GitHub Issues](https://github.com/comandoit/Chandra-OCR-Scanner-IT/issues) for current known issues.

## 📚 Resources

- [Chandra OCR Documentation](https://github.com/DataLabRx/chandra-ocr)
- [vLLM Documentation](https://docs.vllm.ai/)
- [PyTorch Documentation](https://pytorch.org/docs/)

## ❓ Questions?

- Check existing issues and discussions
- Create a GitHub Discussion
- Contact the maintainers

## 🎉 Thank You

Your contributions help make Chandra-OCR Scanner better for everyone!

---

**Remember**: Be respectful, constructive, and inclusive in all interactions.

Happy coding! 🚀
