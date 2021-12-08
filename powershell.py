import subprocess

def pwrshell(callpowershell):
    output = subprocess.check_output("powershell.exe " + callpowershell, stderr=subprocess.STDOUT, shell=True)
    output = output.decode('cp866')
    print(output)


pwrshell('ping 10.253.0.10')
