# Github Trends

**The module finds all the repositories created at the last week, with the highest score and outputs theirs open issues and url to the terminal.**

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

*Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.*

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart
**Ways to use:**
- Have to use  module `github_trending.py` after `python3`, then `enter amount repositories:`.

Example of script launch on Linux, Python 3.5:

```bash
$ python3 github_trending.py
Enter amount repositories: 5
repository №1, name:StarGAN:
open issue:1 	 https://api.github.com/repos/yunjey/StarGAN/issues/3
open issue:2 	 https://api.github.com/repos/yunjey/StarGAN/issues/2
repository №2, name:PWA-Book-CN:
open issue:1 	 https://api.github.com/repos/SangKa/PWA-Book-CN/issues/7
open issue:2 	 https://api.github.com/repos/SangKa/PWA-Book-CN/issues/6
open issue:3 	 https://api.github.com/repos/SangKa/PWA-Book-CN/issues/5
open issue:4 	 https://api.github.com/repos/SangKa/PWA-Book-CN/issues/4
open issue:5 	 https://api.github.com/repos/SangKa/PWA-Book-CN/issues/2
repository №3, name:rustify:
open issue:1 	 https://api.github.com/repos/browserify/rustify/issues/8
open issue:2 	 https://api.github.com/repos/browserify/rustify/issues/6
open issue:3 	 https://api.github.com/repos/browserify/rustify/issues/5
open issue:4 	 https://api.github.com/repos/browserify/rustify/issues/4
open issue:5 	 https://api.github.com/repos/browserify/rustify/issues/3
open issue:6 	 https://api.github.com/repos/browserify/rustify/issues/2
repository №4, name:iA-Fonts:
open issue:1 	 https://api.github.com/repos/iaolo/iA-Fonts/issues/13
open issue:2 	 https://api.github.com/repos/iaolo/iA-Fonts/issues/9
repository №5, name:agile-development-cheat-sheet:
open issue:1 	 https://api.github.com/repos/tucaz/agile-development-cheat-sheet/issues/1

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
