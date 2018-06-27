import os

root = "C:/Users/Vikhyath Rai/PycharmProjects/internship/robot/robot/inv"
for path, dirs, files in os.walk(root):
    for f in files:
        if f.endswith('.py'):
            print(f)