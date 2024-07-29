# llama3.1-chat

Python server that bridges the user to llama3.1 LLM served by Ollama

## Dependencies

You need to have [Ollama](https://ollama.com/) installed. After that, you need to install the `llama3.1` LLM released by Meta. This is easily handled by Ollama executing the following command:

```shell
ollama pull llama3.1
```

## How to use this app

After you clone this repo, you just need to install the app dependencies that are defined inside the requirements text file. This is easily handled by [UV](https://github.com/astral-sh/uv) that I personally hardly recommend it. If you don't want to use UV, it is easy to install dependencies just by using pip deployed by Python.

### With UV

Execute the following command to generate a virtual env (in case you want to use one):

```shell
uv venv
```

This will create a `.venv` directory in the root folder and can be activated using:

```shell
source .venv/bin/activate
```

Then execute the command that will install all dependencies:

```shell
uv pip install -r requirements.txt
```

### Using Pip

You need to install `virtualenv` firstly in order to create a new virtual environment for the application (in case you want a virutal environment for this app). For this to happen just execute:

```shell
python3 -m pip install virtualenv
python3 -m virtualenv .venv
```

Then you will have a new `.venv` directory in the root folder ready to be activated and used. All you have to do is:

```shell
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## How to run this app

After all dependencies have been installed, just run this application this way:

```shell
python3 -m streamlit run main.py
```

This will pop up a new window in your default brower with the application running and ready to be used as your particular LLM running locally in your machine.
