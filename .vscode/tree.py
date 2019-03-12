# please cd to `gm` and run this file
import os
if not os.getcwd().endswith("\gm"): raise Exception("invalid location")

# import subprocess as sp
# with open("tree", "wb") as file:
# 	file.write(
# 			sp.run(["tree"], shell=True, stdout=sp.PIPE).stdout
# 			# .decode('windows-1252')
# 		)
with open("tree", "r", encoding = 'windows-1252') as file:
	while not file.read(1) == "├":
		file.readline()
	# jump away
	text = "gm\n├" + file.read()

with open("tree", "w", encoding = "utf8") as file:
	file.write(text.replace("│", " ").replace("   ", "\t").replace(" ", ""))
