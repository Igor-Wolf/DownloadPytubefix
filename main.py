import subprocess
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def run_script(script_name):
    try:
        print(f"Executando {script_name} com {sys.executable}...")
        result = subprocess.run([sys.executable, script_name], check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {script_name}:")
        print(e.stderr)
        return False

# Executa o script.py
if run_script('script.py'):
    if run_script('conversor.py'):
        print("Todos os scripts foram executados com sucesso.")
    else:
        print("Erro ao executar conversor.py.")
else:
    print("Erro ao executar script.py.")
