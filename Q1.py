def nascimento(data):
    lista_elementos = data.split("/")

    ano = int(lista_elementos[0])
    mes = int(lista_elementos[1])
    dia = int(lista_elementos[2])

    data_spl = {"Ano": ano, "Mes": mes, "Dia": dia}

    return data_spl

def var_booleana(campo):
    if len(campo) == 4:
        campo = campo[:3]
    
    if campo[0] == "S":
        return True
    return False

def func_str(string):
    lista_str = string.split(":")
    return lista_str

def descritor_arq(arq):
    arq.seek(0)
    lista_linhas = arq.readlines()
    
    return lista_linhas

def main():
    pacientes = []
    arq = open("cadastro.txt", "r")

    dic_cadastro = {"CPF":"",
             "Nome":"",
             "Data_de_nascimento":"",
             "Data_de_cadastro":"",
             "Ativo":""}
    
    arq_linhas = descritor_arq(arq)

    for i in range(len(arq_linhas)):
        dic_atual = dic_cadastro.copy()
        dados_atuais = func_str(arq_linhas[i])
        dic_atual["CPF"] = dados_atuais[0]
        dic_atual["Nome"] = dados_atuais[1]
        dic_atual["Data_de_nascimento"] = nascimento(dados_atuais[2])
        dic_atual["Data_de_cadastro"] = nascimento(dados_atuais[3])
        dic_atual["Ativo"] = var_booleana(dados_atuais[4])
        pacientes.append(dic_atual)

    print(pacientes)

    arq.close()

main()
