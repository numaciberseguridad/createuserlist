#!/usr/bin/env python3

file_name = "names.txt"

with open(file_name, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n") #Borra lineas innecesarias de texto  (\n)
        
        name = line.split(" ") 
        # imprime los nombres de usuario en tres formatos distintos
        print(name[0] + name[1])
        print(name[0][:1] + name[1])
        print(name[0] + name[1][:1])
