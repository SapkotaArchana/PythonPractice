"""
To delete files we should import os
"""


import os
# os.remove("myfile.txt")

# Checking if file exists
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


# deleting folder
# os.rmdir("myfolder")   # We can only remove empty folders. this file doesn't exists so error'