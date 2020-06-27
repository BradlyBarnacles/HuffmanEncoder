import os
import matplotlib.pyplot as plt
import json

class Node:

    def __init__(self, freq, letter = None):

        self.left = None
        self.right = None
        self.freq = freq
        self.letter = letter

    def generate_table(self):
        if self.letter != None:
            return {self.letter: ""}
        
        right = self.right.generate_table()
        for key in right.keys():
            right[key] = "1" + right[key]
            
        left = self.left.generate_table()
        for key in left.keys():
            left[key] = "0" + left[key]

        return {**left, **right} 

            

    def generate_list(self):
        if self.letter == None:
            return [ self.left.generate_list() , self.right.generate_list() ]
        else:
            return self.letter
        

path = 'E:/maildir/'
char_frequency = {}



for entry in os.listdir(path):
    if "_sent_mail" in os.listdir(os.path.join(path, entry)):
        directory = os.path.join(path, entry, "_sent_mail")
        for file in os.listdir(directory):
            with open(os.path.join(directory, file), 'r') as f:
                for char in f.read():
                    try:
                        char_frequency[char] += 1
                    except:
                        char_frequency[char] = 1
    break

nodes = []
for char, freq in char_frequency.items():
    nodes.append(Node(freq, letter = char))

while len(nodes) > 1:
    a = min(nodes, key = lambda n: n.freq)
    nodes.remove(a)
    b = min(nodes, key = lambda n: n.freq)
    nodes.remove(b)
    new = Node(a.freq + b.freq)
    
    new.left = a
    new.right = b
    nodes.append(new)

tree = nodes[0]

with open('encode.txt', 'w') as file:
    file.write(json.dumps(tree.generate_table()))

with open('decode.txt', 'w') as file:
    file.write(json.dumps(tree.generate_list()))
    

