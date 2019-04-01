# please cd to `gm` and run this file
import os
if not os.getcwd().endswith("\gm"): raise Exception("invalid location")

import sys
tree = sys.argv[1]
print("the printed aim is: " + tree)
with open(tree, "r", encoding = 'utf8') as file:
	file.readline()
	# jump away
	text = "gm\n" + file.read()

with open(tree, "w", encoding = "utf8") as file:
	file.write(text.replace("│   ", "\t").replace("├── README.md\n", ""))
	# file.write(text..replace("│", " ").replace("   ", "\t").replace(" ", ""))
