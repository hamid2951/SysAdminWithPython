#import subprocess module
import subprocess

#ls bash command
subprocess.run(["ls"])

#ls with one argument
subprocess.run(["ls","-l"])

#ls with multiple arguments
subprocess.run(["ls","-l","solution"])

#System Information
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Diskspace Information
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])