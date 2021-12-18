# graphGrammar
Gramatyki grafowe 2021-2022

## Prerequisites (for linux users)

### pipenv

Install pipenv:

```pip install --user pipenv```

Find your base's binary directory:

```python -m site --user-base```

Add your base's binary directory to PATH

```export PATH="$PATH:<BASES_BINARY_DIRECTORY>/bin"```

Activate changes:

```source ~/.bashrc```

(more information can be found here: https://www.jetbrains.com/help/pycharm/pipenv.html)

## Execution (for linux users)

### 1. From shell

Install project dependencies

```pipenv install```

Start pipenv shell

```pipenv shell```

Run application

```python main.py```

### 2. From Pycharm

On first pycharm startup, you should be asked to set up pipenv environment. To continue, you should have pipenv installed (check above). 
You can provide 'Pipenv executable' as 

```<BASES_BINARY_DIRECTORY>/bin/pipenv.```

Finally, you can go to main.py file and click ```ctrl+shift+F10```, and it should work.

## Troubleshooting

1. ```matplotlib is currently using agg, which is a non-gui backend...``` -
your system may miss python-tk package, so try to install it.
(Example for ubuntu: ```sudo apt-get install python3-tk``` )