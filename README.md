# Github Trends

**The module finds all the repositories created at the last week, with the highest score and outputs amount issues and progect url to the terminal.**

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

*Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.*

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart
**Ways to use:**
- Have to use  module `github_trending.py` after `python3`, with `number repositories`.
But if you foget enter `number repositories` , by default will be 10.

Example of script launch on Linux, Python 3.5:

```bash
$ python3 github_trending.py 6
1) Progect name:PWA-Book-CN 	             amount issues:5 	 https://github.com/SangKa/PWA-Book-CN
2) Progect name:StarGAN 	                 amount issues:5 	 https://github.com/yunjey/StarGAN
3) Progect name:deep-image-prior 	         amount issues:3 	 https://github.com/DmitryUlyanov/deep-image-prior
4) Progect name:rustify 	                 amount issues:6 	 https://github.com/browserify/rustify
5) Progect name:stream-audio-fingerprint 	 amount issues:0 	 https://github.com/dest4/stream-audio-fingerprint
6) Progect name:py2rs 	                   amount issues:2 	 https://github.com/rochacbruno/py2rs


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
