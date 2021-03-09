import subprocess


language = "java"
file_reader = "-jar"
file_exe = "FACTEMICLI-2.5.16-9655-cmdClient.jar"  # In the current directory
nif = "-n"
number_nif = "503553522"
password = "-p"
number_password = "0000000000"
year = "-a"
number_year = "2021"
month = "-m"
number_month = "02"
operation = "-op"
number_operation = "enviar"  # "validar"
input_param = "-i"
input_file = r"C:\Users\Frederico\Desktop\Frederico_Gago\Confere\Programas\saft_project\saft_exemplo\SAFT_10101_01022021_28022021.xml"
output_param = "-o"
output_file = r"C:\Users\Frederico\Desktop\Frederico_Gago\Confere\Programas\saft_project\output_response.xml"
test = "-t"


proc1 = subprocess.run([language, file_reader, file_exe, nif, number_nif, password, number_password, year, number_year, month, number_month, operation, number_operation, input_param, input_file, output_param, output_file, test], capture_output=True)

print(proc1)
print("-"*100)
print(proc1.stderr.decode("ISO-8859-1"))
print("-"*100)
print(proc1.stdout.decode("ISO-8859-1"))
