# Contributing to SpyNet

Thank you for your interest in contributing to SpyNet! This document provides guidelines for contributing to the project.

## Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/SpyNet.git
   cd SpyNet
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Configuration**
   ```bash
   cp config.json.example config.json
   # Add your test API keys
   ```

## Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions focused and small
- Comment complex logic

### Testing

- Run the test suite before submitting:
  ```bash
  python test_spynet.py
  ```
- Add tests for new features
- Ensure all tests pass

### Commits

- Write clear, descriptive commit messages
- Use present tense ("Add feature" not "Added feature")
- Reference issues when applicable

### Pull Requests

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Open a Pull Request with:
   - Clear description of changes
   - Screenshots for UI changes
   - Reference to related issues

## Areas for Contribution

### High Priority
- Cross-platform testing and fixes
- Performance optimization
- UI/UX improvements
- Bug fixes

### Features
- Conversation history
- Voice input support
- Custom themes
- Additional AI model integrations
- Plugin system

### Documentation
- Tutorial videos
- Additional examples
- Translation to other languages
- API documentation

## Reporting Issues

When reporting bugs, please include:
- OS and Python version
- Steps to reproduce
- Expected vs actual behavior
- Error messages or logs
- Screenshots if applicable

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help newcomers
- Focus on the project goals

## Questions?

Feel free to open an issue for:
- Feature requests
- Bug reports
- Questions about usage
- Discussion of improvements

## License

By contributing, you agree that your contributions will be licensed under the same terms as the project.

---

Thank you for contributing to SpyNet! 🎉
