
# YouTube Trend & Idea Analyzer

YouTube Trend & Idea Analyzer is a Python-based toolkit designed to help content creators analyze YouTube trends, generate video ideas, and evaluate their concepts. Whether you're looking to stay ahead of the curve or refine your creative process, YouTube Trend & Idea Analyzer is free and here to assist!

---

## Features

- **Trending Video Analysis**: Fetch and analyze trending YouTube videos, highlighting top categories, tags, and average view counts.
- **Video Idea Generation**: Create unique, trend-aligned video ideas tailored to your goals.
- **Idea Evaluation**: Assess your video concepts for trend alignment, originality, sustainability, and SEO potential.

---

### Prerequisite: Install Python

Before running the setup, ensure Python is installed on your system.

- **Windows**:
  1. Download Python from [python.org](https://www.python.org/downloads/).
  2. Run the installer and check "Add Python to PATH" during installation.
- **MacOS**:
  - Use the official Python installer or run:
    ```bash
    brew install python
    ```
- **Linux**:
  - Use your package manager:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

After installation, verify Python is installed:
```bash
python --version

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aidreamacademy/youtube-analyzer
   cd youtube-analyzer
   ```

2. Run the setup script:
   ```bash
   python setup.py
   ```
   - The script will:
     1. Install all required dependencies listed in `requirements.txt`.
     2. Prompt you to enter your YouTube and Anthropic API keys.
     3. Save the keys in a `.env` file for future use.

---

## Usage

1. Run the main script:
   ```bash
   python youtube_analyzer.py
   ```

2. Select an option from the menu:
   - **Analyze Current Trends**: Fetch and display trending video data.
   - **Generate Video Ideas**: Create new video ideas based on trends.
   - **Evaluate Your Video Idea**: Assess your own video idea using trends and metrics.

---

## Dependencies

- [Google API Client](https://github.com/googleapis/google-api-python-client): For accessing YouTube data.
- [Anthropic API](https://www.anthropic.com/): For generating and evaluating video ideas.
- [Python Dotenv](https://github.com/theskumar/python-dotenv): For managing API keys.
- Other dependencies are listed in `requirements.txt`.

---

## Files

- `youtube_analyzer.py`: Main script to run the application.
- `setup.py`: Automates the installation of dependencies and setup of API keys.
- `youtube_api.py`: Wrapper for YouTube API operations.
- `anthropic_api.py`: Wrapper for Anthropic API interactions.
- `trend_analysis.py`: Functions to analyze YouTube trends.
- `idea_generation.py`: Functions for generating and evaluating video ideas.
- `constants.py`: Stores YouTube category mappings.
- `requirements.txt`: Lists all dependencies required for the project.

---

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- YouTube API for providing trending video data.
- Anthropic API for enabling AI-driven video idea generation.

---

## Contact

For questions or support, please create an issue or contact the repository owner.
