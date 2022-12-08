# chatgpt-exec
Interact with ChatGPT in a Python terminal.

Until an official API is released, it relies on [chatgpt-api](https://github.com/mbroton/chatgpt-api).

## Installation
```sh
git clone https://github.com/vilimus/chatgpt-exec.git
cd chatgpt-exec
pip install -r requirements.txt
```

## Usage

```sh
python chatgpt.py
```

It is a standard back-and-forth interaction with ChatGPT, with three special commands:
- `q`/`quit` to quit
- `s`/`save` to save the current conversation
- `e`/`exec` to execute a code chunk that ChatGPT produced
  - note: this assumes ChatGPT printed ONE code chunk. If it printed multiple code chunks, just ask nicely for it to combine them!
  
Once a code chunk is executed, the results can be referenced via the keyword `<RESULT>`.

## Tips

ChatGPT likes to remind you that it cannot access the internet or execute code. Just kindly remind it that you are not asking it to do so, you are simply asking it to write code!
