# please cd to the gm to run this file
import os
if not os.getcwd().endswith("\gm"): raise Exception("invalid location")
with open("tree", "r", encoding = "utf8") as file:
	while not file.read(1) == "├":
		file.readline()
	# jump away
	text = "gm\n├" + file.read()

with open("tree", "w", encoding = "utf8") as file:
	file.write(text.replace("│", " ").replace("   ", "\t").replace(" ", ""))

	
