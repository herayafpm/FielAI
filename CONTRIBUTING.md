# Contributing to FielAI

Thank you for your interest in contributing to FielAI! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version, etc.)
- Error messages and logs

### Suggesting Features

We welcome feature suggestions! Please open an issue with:
- Clear description of the feature
- Use case and benefits
- Possible implementation approach (optional)

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/herayafpm/FielAI.git
   cd FielAI
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the code style guidelines
   - Add tests for new features
   - Update documentation

4. **Test your changes**
   ```bash
   # Run tests
   python tests/test_memory.py
   
   # Test manually
   python src/main.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

6. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub

## Code Style Guidelines

### Python Code Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions small and focused
- Add type hints where appropriate

Example:
```python
def process_input(self, user_input: str) -> str:
    """
    Process user input and generate response.
    
    Args:
        user_input: The user's text input
        
    Returns:
        AI-generated response
    """
    # Implementation
    pass
```

### Commit Messages

Format: `Type: Description`

Types:
- `Add:` New feature
- `Fix:` Bug fix
- `Update:` Update existing feature
- `Refactor:` Code refactoring
- `Docs:` Documentation changes
- `Test:` Test additions/changes
- `Style:` Code style changes

Examples:
```
Add: voice activity detection
Fix: memory persistence issue
Update: improve STT accuracy
Docs: add installation guide
```

## Project Structure

```
FielAI/
├── src/              # Core source code
├── utils/            # Utility scripts
├── config/           # Configuration files
├── tests/            # Unit tests
├── docs/             # Documentation
├── examples/         # Example usage
└── scripts/          # Helper scripts
```

## Development Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If exists
   ```

2. **Run in development mode**
   ```bash
   python src/main.py
   ```

3. **Run tests**
   ```bash
   python -m pytest tests/
   # Or
   python tests/test_memory.py
   ```

## Areas for Contribution

### High Priority
- [ ] Voice Activity Detection (VAD)
- [ ] Web UI (Gradio/Streamlit)
- [ ] Better error handling
- [ ] Performance optimization
- [ ] More comprehensive tests

### Medium Priority
- [ ] Multi-language support improvements
- [ ] Plugin system
- [ ] Cloud backup integration
- [ ] Mobile app
- [ ] Docker support

### Low Priority
- [ ] Custom model training
- [ ] Advanced analytics
- [ ] Voice cloning
- [ ] Multi-user support

## Testing Guidelines

- Write unit tests for new features
- Ensure existing tests pass
- Test on multiple platforms if possible
- Include edge cases

Example test:
```python
def test_save_conversation(self):
    """Test saving a conversation"""
    user_input = "Hello"
    ai_response = "Hi!"
    
    self.memory.save_conversation(user_input, ai_response)
    count = self.memory.collection.count()
    
    self.assertEqual(count, 1)
```

## Documentation

When adding features:
- Update README.md if needed
- Add docstrings to code
- Update relevant documentation in `docs/`
- Add examples if applicable

## Code Review Process

1. All PRs require review
2. CI/CD checks must pass
3. Code must follow style guidelines
4. Tests must pass
5. Documentation must be updated

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn
- Focus on the code, not the person

## Questions?

- Open an issue for questions
- Check existing issues first
- Join discussions on GitHub

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to FielAI! 🚀**