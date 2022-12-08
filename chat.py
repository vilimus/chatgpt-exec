import io
import re
import sys
import traceback

from chatgpt.api import ChatGPT 

with open("chatgpt_session_token.txt", "r") as f:
  session_token = f.read()
  
chat = ChatGPT(session_token=session_token)
chat.authenticate()

response = str()
result = str()

done = False
while not done:

  m = input(">")
  
  if m in ["q", "quit"]:
    done = True
  
  elif m in ["s", "save"]:
    filename = input("Enter filename: ")
    with open(filename, "w") as f:
      f.write(reponse)
   
  elif m in ["e", "exec"]:
    # get code from response
    x = [m for m in re.finditer('```', response)]
    if len(x) != 2:
      print("Can't do it!")
    else:
      m1, m2 = x
      code = response[m1.end():m2.start()]

      # intercept stdout
      old_stdout = sys.stdout
      new_stdout = io.StringIO()
      sys.stdout = new_stdout
      
      # execute code
      try:
        exec(code)
        result = sys.stdout.getvalue().strip()
      except Exception as e:
        result = traceback.format_exc()
        
      # replace stdout
      sys.stdout = old_stdout
      print(result)
      
  else:
    m = m.replace("<RESULT>", result)
    try:
      response = chatgpt.send_message(m).content
      print(f"\nChatGPT: {response}\n")
    except:
      print("Timeout")
