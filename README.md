# graphGrammar
Gramatyki grafowe 2021-2022

## Prerequisites

### pipenv (for linux users)

Install pipenv:

```pip install --user pipenv```

Find your base's binary directory:

```python -m site --user-base```

Add your base's binary directory to PATH

```export PATH="$PATH:<BASES_BINARY_DIRECTORY>/bin"```

Activate changes:

```source ~/.bashrc```

(more information can be found here: https://www.jetbrains.com/help/pycharm/pipenv.html)

## Installation

Install project dependencies

```pipenv install```

Start pipenv shell

```pipenv shell```

## Run application

```python main.py```

## Pycharm configuration

On first pycharm startup, you should be asked to set up pipenv environment. You should have pipenv installed (check above). 
You can provide 'Pipenv executable' as 

```<BASES_BINARY_DIRECTORY>/bin/pipenv.```

Next you can go to main.py file and click ctrl+shift+F10

