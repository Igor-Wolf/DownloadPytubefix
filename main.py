import subprocess

def run_script(script_name):
    """Executa um script Python e retorna True se a execução for bem-sucedida, False caso contrário."""
    try:
        print(f"Executando {script_name}...")
        result = subprocess.run(['python', script_name], check=True, text=True, capture_output=True)
        print(result.stdout)  # Exibe a saída do script
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {script_name}:")
        print(e.stderr)  # Exibe a saída de erro do script
        return False

# Executa o script.py
if run_script('script.py'):
    # Executa o conversor.py somente se script.py for bem-sucedido
    if run_script('conversor.py'):
        print("Todos os scripts foram executados com sucesso.")
    else:
        print("Erro ao executar conversor.py.")
else:
    print("Erro ao executar script.py.")
