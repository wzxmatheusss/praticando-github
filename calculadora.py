def calculadora():
    """
    Calculadora simples que realiza operações básicas de matemática.
    """
    print("=== Calculadora Simples ===")
    print("Operações disponíveis:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")
    
    while True:
        operacao = input("\nEscolha uma operação (1-5): ").strip()
        
        if operacao == "5":
            print("Encerrando a calculadora. Até logo!")
            break
        
        if operacao not in ["1", "2", "3", "4"]:
            print("Operação inválida! Tente novamente.")
            continue
        
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            
            if operacao == "1":
                resultado = numero1 + numero2
                print(f"\n{numero1} + {numero2} = {resultado}")
            
            elif operacao == "2":
                resultado = numero1 - numero2
                print(f"\n{numero1} - {numero2} = {resultado}")
            
            elif operacao == "3":
                resultado = numero1 * numero2
                print(f"\n{numero1} * {numero2} = {resultado}")
            
            elif operacao == "4":
                if numero2 == 0:
                    print("\nErro: Não é possível dividir por zero!")
                else:
                    resultado = numero1 / numero2
                    print(f"\n{numero1} / {numero2} = {resultado}")
        
        except ValueError:
            print("Erro: Digite números válidos!")
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    calculadora()
