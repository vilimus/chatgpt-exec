# chatgpt-exec
Interact with ChatGPT in Python terminal.

# Usage
It is a standard back-and-forth interaction with ChatGPT, with three special commands:
- `q`/`quit` to quit
- `s`/`save` to save the current conversation
- `e`/`exec` to execute a code chunk that ChatGPT produced
  - note: this assumes ChatGPT printed ONE code chunk. If it printed multiple code chunks, just ask nicely for it to combine them!
  
Once a code chunk is executed, the results can be referenced via the keyword `<RESULT>`.
