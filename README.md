
# DevOps Core Tooling

[![CI Pipeline](https://github.com/NidhiiBuilds/devops-core-tooling/actions/workflows/ci.yml/badge.svg)](https://github.com/NidhiiBuilds/devops-core-tooling/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A practical Python project demonstrating professional DevOps practices, Git collaboration, automated testing, and CI workflows.

## Architecture Overview

The project uses GitHub for source control and GitHub Actions to automate testing and code quality checks.

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI
    |
    +---- Checkout Code
    |
    +---- Install Dependencies
    |
    +---- Flake8 (Code Quality)
    |
    +---- Pytest (Automated Tests)
    |
    v
CI Result
```

## Project Structure

```text
devops-core-tooling/
├── .github/workflows/ci.yml
├── tests/
├── auth.py
├── config.py
├── dashboard.py
├── logger.py
├── main.py
├── requirements.txt
└── README.md
```

## Installation

**Requirements:** Python 3.11+ and Git.

1. Clone the repository:

   ```bash
   git clone https://github.com/NidhiiBuilds/devops-core-tooling.git
   cd devops-core-tooling
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Testing

Run automated tests:

```bash
python -m pytest -v
```

Check code quality:

```bash
python -m flake8 .
```

## Usage

Example dashboard function:

```python
from dashboard import get_dashboard_message

print(get_dashboard_message("Developer"))
```

## CI Automation

GitHub Actions automatically runs Flake8 and Pytest whenever code is pushed to `main` or a pull request targets `main`.

## Contributing

1. Create a feature branch.
2. Make your changes and test them.
3. Commit with a descriptive message.
4. Open a pull request for review.

Please follow the guidelines in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
