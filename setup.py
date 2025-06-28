"""
Setup script for AI Music Generator
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="ai-music-generator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Generate music using AI with Facebook's MusicGen model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-music-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "gpu": [
            "torch>=1.9.0+cu118",
            "torchaudio>=0.9.0+cu118",
        ],
    },
    entry_points={
        "console_scripts": [
            "music-generator=examples:main",
        ],
    },
    keywords="ai music generation musicgen pytorch audio synthesis",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ai-music-generator/issues",
        "Source": "https://github.com/yourusername/ai-music-generator",
        "Documentation": "https://github.com/yourusername/ai-music-generator#readme",
    },
)
