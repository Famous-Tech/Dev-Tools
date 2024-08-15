import subprocess

def run_shell_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if output:
            print(output.decode())
        if error:
            print(error.decode())
    except Exception as e:
        print(f"Shell Error: {e}")
