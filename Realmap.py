import socket
from time import sleep

def scan(site, porta_inicial=None, porta_final=None):
    try:
        if porta_inicial is None:
            porta_inicial = 1
        if porta_final is None:
            porta_final = 8888  

        porta_inicial = int(porta_inicial)
        porta_final = int(porta_final)

        for porta in range(porta_inicial, porta_final + 1):
            conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conexao.settimeout(1)                        
            resultado = conexao.connect_ex((site, porta)) 

            if resultado == 0:
                print(f"a porta {porta} está aberta")
            else:
                print(f"a porta {porta} está fechada!")

            conexao.close()   
            sleep(0.10)       

    except ConnectionRefusedError:
        print(f"a conexão com a porta {porta} foi recusada")
    except Exception as e:
        print(f"Erro durante o scan: {e}")

def banner():
    print(r"""
  [*]===================================[*]
        REALMAP - The Real Port Mapper
  [*]===================================[*]
    """)

def menu():
    print("\n+----------------------------------+")
    print("|          MENU DE OPÇÕES          |")
    print("+----------------------------------+")
    print("| 1 - Escanear uma faixa de portas |")
    print("| 2 - Escanear todas as portas     |")
    print("| 3 - Sobre o RealMap              |")
    print("| 0 - Sair                         |")
    print("+----------------------------------+")
    
    escolha = input("Digite a opção desejada: ")
    return escolha

# programa principal
try:
    banner()
    while True:
        escolha = menu()
        try:
            escolha_int = int(escolha)
        except ValueError:
            print("Digite um número válido!")
            continue

        if escolha_int == 1:
            site = input("digite o endereço do site:  ").strip()
            porta_inicial = input("começar o scan a partir da porta?:  ").strip()
            porta_final = input("termina o scan na porta?:  ").strip()

            try:
                porta_inicial = int(porta_inicial)
                porta_final = int(porta_final)
            except ValueError:
                print("Portas devem ser números inteiros.")
                continue

            if porta_inicial < 1 or porta_final < porta_inicial:
                print("Faixa inválida. Verifique os números das portas.")
                continue

            print("iniciando scan...")
            sleep(1)
            scan(site, porta_inicial, porta_final)

        elif escolha_int == 2:
            site = input("digite o endereço do site:  ").strip()
            print("iniciando scan em todas as portas (1-8888)...")
            sleep(1)
            scan(site)  

        elif escolha_int == 3:
            print("RealMap - criado para aprendizagem. Use apenas em alvos autorizados.")
            sleep(2)

        elif escolha_int == 0:
            print("encerrando sistema...")
            sleep(0.5)
            break

        else:
            print("digite um numero válido!")

except ValueError:
    print("digite um valor válido!")

except KeyboardInterrupt:
    print("\nScan interrompido pelo usuário!")

except socket.error:
    print("o socket falhou!")

except socket.gaierror:
    print("endereço ou IP não encontrado")
