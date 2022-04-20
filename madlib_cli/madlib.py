
def welcome():
  """
  print welcome message
  """
  print('''Welcome to Madlibs!''')



def read_template(file_path):
  """
  read the file
  """
  try:
    with open(file_path) as template:
      return template.read().strip()
  except FileNotFoundError as fnf_error:
    raise(fnf_error)



def parse_template(template):
  stripped = ""
  parts = []
  content = False
  characters = ""
  
  for letter in template:
    if letter == "{":
        stripped += letter
        content = True
        characters = ""
    elif letter == "}":
        stripped += letter
        content = False
        parts.append(characters)
    elif content:
      characters += letter
    else:
      stripped += letter
  return stripped,tuple(parts)



def merge(template, tupl):
  return template.format(*tupl)