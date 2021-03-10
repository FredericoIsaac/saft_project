# --------------------------------------- ENVIAR SAFT LINHA DE COMANDOS --------------------------------------- #
# import subprocess
#
#
# language = "java"
# file_reader = "-jar"
# file_exe = "jar_file/FACTEMICLI-2.5.16-9655-cmdClient.jar"  # In the current directory
# nif = "-n"
# number_nif = "503553522"
# password = "-p"
# number_password = "00000000000000"
# year = "-a"
# number_year = "2021"
# month = "-m"
# number_month = "02"
# operation = "-op"
# number_operation = "enviar"  # "validar"
# input_param = "-i"
# input_file = r"C:\Users\Frederico\Desktop\Frederico_Gago\Confere\Programas\saft_project\saft_exemplo\SAFT_10101_01022021_28022021.xml"
# output_param = "-o"
# output_file = r"C:\Users\Frederico\Desktop\Frederico_Gago\Confere\Programas\saft_project\output_response.xml"
# test = "-t"
#
#
# proc1 = subprocess.run([language, file_reader, file_exe, nif, number_nif, password, number_password, year, number_year, month, number_month, operation, number_operation, input_param, input_file, output_param, output_file, test], capture_output=True)
#
# print(proc1)
# print("-"*100)
# print(proc1.stderr.decode("ISO-8859-1"))
# print("-"*100)
# print(proc1.stdout.decode("ISO-8859-1"))


# --------------------------------------- TEMP FILE LOGIC --------------------------------------- #


class SAFT:
    def __init__(self, temp_path, nif):
        self.path = temp_path
        self.nif = nif


# --------------------------------------- TEMP FILE LOGIC --------------------------------------- #
import os
import xml.etree.ElementTree as ET
import psycopg2


# TODO 1. Pesquisar pasta Temp e tirar listagem de SAFT's colocar numa list os endereços.

TEMP_DIRECTORY = r"temp_file"

for file in os.listdir(TEMP_DIRECTORY):
    if file.endswith(".xml"):
        saft_path = os.path.join(TEMP_DIRECTORY, file)

        # TODO 2. Abrir cada ficheiro, procurar e extrair NIF.
        nif: int
        root = ET.parse(saft_path).getroot()

        for nif_saft in root.iter("{urn:OECD:StandardAuditFile-Tax:PT_1.04_01}TaxRegistrationNumber"):
            nif = int(nif_saft.text)

        print(nif)

        _10101 = SAFT(saft_path, nif)

        # TODO 3. Get from database the company number (10101) and Password ("00000000000")
