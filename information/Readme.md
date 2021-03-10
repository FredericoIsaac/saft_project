# Java SE 6

https://docs.oracle.com/en/java/javase/15/

# Configuração 

java -jar 'FACTEMICLI-2.5.16-9655-cmdClient.jar' -n 503553522 -p 101503553522 -a 2021 -m 02 -op enviar -i 'C:\Users\Frederico\Desktop\Frederico Gago\Confere\Programas\saft_project\saft_exemplo\SAFT_10101_01022021_28022021.xml' -o 'C:\Users\Frederico\Desktop\Frederico Gago\Confere\Programas\saft_project\output_response.txt' -t


# Flow chart

https://app.diagrams.net/#HFredericoIsaac%2Fsaft_project%2Fmaster%2Fsend_saft

# Subprocess Library Explanation

Running Shell Commands using Python (Detailed Explanation):

    https://www.youtube.com/watch?v=IIiKVaxHCX0

    https://gist.github.com/FredericoIsaac/df0bdb79356b7e6b8ff08b6b5f5e213f


# Directory

Documentos (SRV-SABINO2016)lho


## Apontamentos

```python
array_parameters = [language, file_reader, file_exe, nif, number_nif, password, number_password, year, number_year, month, number_month, operation, number_operation, input_param, input_file, output_param, output_file, test]

proc1 = subprocess.run([language, file_reader, file_exe, nif, number_nif, password, number_password, year, number_year, month, number_month, operation, number_operation, input_param, input_file, output_param, output_file, test], capture_output=True, text=True)


# If any code return, like error, if everything ok returns 0:
print(proc1.returncode)

# Print the arguments list passed:
print(proc1.args)

# Option 1:
proc1 = subprocess.run([language, file_reader, file_exe, nif, number_nif, password, number_password, year, number_year, month, number_month, operation, number_operation, input_param, input_file, output_param, output_file, test], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

# if we want to get the error we use stderr=subprocess.PIPE
print(proc1.stderr)  # binary string we can decode:
print(proc1.stderr.decode)
# Too simplify we can use stderr=subprocess.STDOUT so that the error appear in stdout, because if error stdout is empty:
print(proc1.stdout)

# Show the output of the shell command execution (when using this in subprocess stdout=subprocess.PIPE):
print(proc1.stdout)  # it is a binary string so we have to decode():
print(proc1.stdout.decode())

# Option 2  (BETTER):
# if capture_output is true, stdout and stderr will be automatically captured stdout=PIPE and stderr=PIPE is set automatically

proc1 = subprocess.run([language, file_reader, file_exe, nif, number_nif, password, number_password, year, number_year, month, number_month, operation, number_operation, input_param, input_file, output_param, output_file, test], capture_output=True, text=True)


# To run has a string command in the shell instead has reading like a program:
user_input = "output_response.txt ; pwd"
command = "cat {}".format(user_input)
proc_2 = subprocess.run(command, shell=True, capture_output=True)
# No SAFT tem que ser decode("ISO-8859-1") para resultar, decode() so nao da
print(proc_2.stdout.decode("ISO-8859-1"))


import shlex

# Create a list of strings that holds the params
print(shlex.split("java -jar file.txt"))
output: ['java', '-jar', 'file.txt']
```