import requests


def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def main():
    while True:
        try:
            cep = int(input("Digite o CEP: "))
            endereco = consultar_cep(cep)
            try:
                if len(str(cep)) != 8:
                    raise ValueError("O Cep tem 8 Digits")
                else:
                    print(f"{endereco['logradouro']}, Bairro {endereco['bairro']}, {endereco['localidade']}/"
                          f"{endereco['uf']}, DDD:{endereco['ddd']}")
                    break
            except ValueError as e:
                print(e)

        except ValueError:
            print('Digite um cep válido')


if __name__ == "__main__":
    main()
