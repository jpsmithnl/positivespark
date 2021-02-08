# PositiveSpark
Python project for pushing updates to twitter, etc.

## Setup
Decide on how to use python. If Anaconda, etc in your path be careful of conflicts. 
Pyenv is my favorite way to manage python. 

[Pyenv available from github on linux, brew for macOS](https://github.com/pyenv/pyenv)

If you're on Windows there's a [fork](https://github.com/pyenv-win/pyenv-win).
On Windows in an administrator command prompt:
```
choco install pyenv-win 
pyenv rehash
pyenv install --list
pyenv install 3.8.2
pyenv local 3.8.2 
```

This is a [poetry](https://python-poetry.org/docs/) project. See [here](https://python-poetry.org/docs/#installation) about how to install poetry itself. To install dependencies run `poetry install`

This project uses the Twitter API, to get an API key create a new project. Store the keys it posts somewhere safe:
https://developer.twitter.com/en/portal/projects/new

Under `Twitter Developer Portal` > `Settings` > `App permissions` make sure to allow write permissions.

Tokens need to be refreshed afters changing permissions, under `Keys and tokens`>`Authentication Tokens` hit `Regenerate` if they were not created with the correct permissions.
