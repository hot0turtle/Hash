import hashlib   

desire = int(input("Quer autenticar 1; Ou Cadastrar? 2 :"))

if desire == 1:
    print("autenticar")
elif desire == 2:
    
    user = input("Qual o usuario  :")[:4]
    with open( r'C:\Users\leonardo.hanke\Documents\Hash\text.txt', 'w') as f:
        f.write(f"{user},")
    
    pas = input("Qual a senha  :")[:4]
    
    with open( r'C:\Users\leonardo.hanke\Documents\Hash\text.txt', 'w') as f:
        f.write(f"{pas}\n")
