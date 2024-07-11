def converter_brl_para_usd(valor_brl, taxa_cambio):
    """
    Converte valor de reais (BRL) para dólares (USD).
    
    :param valor_brl: Valor em reais a ser convertido
    :param taxa_cambio: Taxa de câmbio de BRL para USD
    :return: Valor convertido em dólares
    """
    return valor_brl / taxa_cambio

def converter_usd_para_brl(valor_usd, taxa_cambio):
    """
    Converte valor de dólares (USD) para reais (BRL).
    
    :param valor_usd: Valor em dólares a ser convertido
    :param taxa_cambio: Taxa de câmbio de USD para BRL
    :return: Valor convertido em reais
    """
    return valor_usd * taxa_cambio

def main():
    # Exemplo de taxa de câmbio fixa. Atualize conforme necessário.
    taxa_cambio_brl_para_usd = 5.17  # 1 USD = 5.17 BRL
    taxa_cambio_usd_para_brl = 1 / taxa_cambio_brl_para_usd

    print("Sistema de Conversão de Moedas")
    print("Escolha a opção de conversão:")
    print("1. Converter de Reais (BRL) para Dólares (USD):")
    print("2. Converter de Dólares (USD) para Reais (BRL):")

    opcao = int(input("Digite a opção (1 ou 2): "))

    if opcao == 1:
        valor_brl = float(input("Digite o valor em reais (BRL): "))
        valor_usd = converter_brl_para_usd(valor_brl, taxa_cambio_brl_para_usd)
        print(f"R$ {valor_brl:.2f} BRL é equivalente a $ {valor_usd:.2f} USD")
    
    elif opcao == 2:
        valor_usd = float(input("Digite o valor em dólares (USD): "))
        valor_brl = converter_usd_para_brl(valor_usd, taxa_cambio_usd_para_brl)
        print(f"$ {valor_usd:.2f} USD é equivalente a R$ {valor_brl:.2f} BRL")
    
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
