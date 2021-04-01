import subprocess

# Exercise 2: ls
subprocess.run(["ls"])

# Exercise 3: ls with one argument
subprocess.run(["ls","-l"])

# Exercise 4: ls with multiple arguments
subprocess.run(["ls","-l","solution"])

# Exercise 5: System Information
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Excercise #6: Diskspace Information
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])