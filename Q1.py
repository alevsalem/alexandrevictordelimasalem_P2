def nascimento(data):
    elementos = data.slipt("/")
    dic_data = {"ANO": elementos[0],
                "MES": elementos[1],
                "DIA": elementos[2]
                }
    return dic_data

def var_booleana(ativo)
    if ativo[-1] == "/n"
        ativo = [:-1]
        if ativo == "SIM"
            return True
        else:
            return False
    else:
        if ativo = [:-1]
            return True
        else:
            return False

def func_str(string)
    lista_str = string.split(":")
    return lista_str

def descritor_arq(arq)
        lista_str = arq.readlines()
        return lista_str
#Não foi considerado a necessidade da presença do "/n" no final de cada linha do arquivo direcionado para cada objeto da lista.

def main():
    abrir = open ("cadastro.txt", "r")
    fazer_lista = descritor_arq(abrir)
    lista_str = func_str(fazer_lista)
    lista_dic = []
    
    for i in lista_str
        dic = {"CPF": lista_str[0]
            "NOME": lista_str[1]
            "NASCIMENTO": nascimento(lista_str[2]),
            "CADASTRO": nascimento(lista_str[3]),
            "ATIVO": var_booleana(lista_str[4])
            }
        lista_dic.append(dic.copyC)
    print(lista_dic)
    
main()
