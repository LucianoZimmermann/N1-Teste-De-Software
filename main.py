import pytest

def criptografar(texto, chave, alfabeto):
    texto_criptografado = ''
    for caractere in texto:
        if caractere in alfabeto:
            indice = alfabeto.index(caractere)
            novo_indice = (indice + chave) % len(alfabeto)
            texto_criptografado += alfabeto[novo_indice]
        else:
            texto_criptografado += caractere
    return texto_criptografado

def descriptografar(texto_criptografado, chave, alfabeto):
    texto_descriptografado = ''
    for caractere in texto_criptografado:
        if caractere in alfabeto:
            indice = alfabeto.index(caractere)
            novo_indice = (indice - chave) % len(alfabeto)
            texto_descriptografado += alfabeto[novo_indice]
        else:
            texto_descriptografado += caractere
    return texto_descriptografado

alfabeto = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìîóòõôúùûABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈÊÍÌÎÓÒÕÔÚÙÛ '

def test_criptografar():
    texto = "Luciano Luís Zimmermann"
    chave = 6
    texto_criptografado = criptografar(texto, chave, alfabeto)
    assert texto_criptografado == "RáiogtufRáôyfÈosskxsgtt"

def test_descriptografar():
    texto_criptografado = "RáiogtufRáôyfÈosskxsgtt"
    chave = 6
    texto_descriptografado = descriptografar(texto_criptografado, chave, alfabeto)
    assert texto_descriptografado == "Luciano Luís Zimmermann"

if __name__ == "__main__":
    pytest.main()

    ##texto = input("Digite o texto a ser criptografado: ")
    ##chave = int(input("Digite o indice da criptografia: "))

    ##texto_criptografado = criptografar(texto, chave, alfabeto)
    ##print("Texto criptografado:", texto_criptografado)

    ##texto_descriptografado = descriptografar(texto_criptografado, chave, alfabeto)
    ##print("Texto descriptografado:", texto_descriptografado)



