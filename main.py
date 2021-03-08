import os
import subprocess

# jar_file_path = "FACTEMICLI-2.5.16-9655-cmdClient.jar"
# saft_file = "C:\\Users\\Frederico\\Desktop\\rederico Gago\\Confere\\Programas\\saft_project\\saft_exemplo\\SAFT_10101_01022021_28022021.xml"
# file_output = "C:\\Users\\Frederico\\Desktop\\Frederico Gago\\Confere\\Programas\\saft_project\\output_response.txt"
# command = f"java -jar {jar_file_path} -n 503553522 -p 101503553522 -a 2021 -m 02 -op enviar -i {saft_file} -o {file_output} -t"


# os.system(f"cmd /k java -jar FACTEMICLI-2.5.16-9655-cmdClient.jar -n 503553522 -p 101503553522 -a 2021 -m 02 -op enviar -i " + saft_file + " -o 'C:\\Users\\Frederico\\Desktop\\Frederico Gago\\Confere\\Programas\\saft_project\\output_response.txt' -t")
# os.system("cmd /k java -version")

# subprocess.run(("cmd", "/C", command))

# subprocess.run(["ls", "-l"])

string = "java -jar FACTEMICLI-2.5.16-9655-cmdClient.jar -n 503553522 -p 101503553522 -a 2021 -m 02 -op enviar -i 'C:\\Users\\Frederico\\Desktop\\Frederico_Gago\\Confere\\Programas\\saft_project\\saft_exemplo\\SAFT_10101_01022021_28022021.xml' -o 'C:\\Users\\Frederico\\Desktop\\Frederico_Gago\\Confere\\Programas\\saft_project\\output_response.txt' -t"
#
p1 = subprocess.run(string, shell=True)
# # os.system(string)
print(p1.args)

