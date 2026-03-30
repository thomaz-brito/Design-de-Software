saldo=float(input())
inv=input()
quantidade=0
total=0
taxas=0
while inv!="encerrar":
    if inv not in ("ações","fundos imobiliarios","cdb","lci","criptomoedas"):
        print("Produto nao reconhecido - tente novamente")
    else:
        val=float(input())
        if inv=="ações":
            if saldo-1.02*val>=0:
                saldo=saldo-1.02*val
                quantidade+=1
                total+=val
                taxas=taxas+0.02*val
            else:
                print("Saldo insuficiente")
        if inv=="fundos imobiliarios":
            if saldo-1.015*val>=0:
                saldo=saldo-1.015*val
                quantidade+=1
                total+=val
                taxas=taxas+0.015*val
            else:
                print("Saldo insuficiente")
        if inv=="cdb":
            if saldo-val<0:
                print("Saldo insuficiente")
            elif val<1000:
                print("Valor mínimo não atingido - tente novamente")
            else:
                saldo=saldo-val
                quantidade+=1
                total+=val
        if inv=="lci":
            if saldo-val<0:
                print("Saldo insuficiente")
            elif val<500:
                print("Valor mínimo não atingido - tente novamente")
            else:
                saldo=saldo-val
                quantidade+=1
                total+=val
        if inv=="criptomoedas":
            if val<200:
                if saldo-val-5<0:
                    print("Saldo insuficiente")
                else:
                    saldo=saldo-val-5
                    quantidade+=1
                    total+=val
                    taxas=taxas+5
            else:
                if saldo-1.03*val<0:
                    print("Saldo insuficiente")
                else:
                    saldo=saldo-1.03*val
                    quantidade+=1
                    total+=val
                    taxas=taxas+0.03*val
    inv=input()     

if quantidade>=3:
    saldo+=0.05*taxas
if total>10000:
    saldo+=50

print(f"O total investido foi {total:.2f}")
print(f"Seu saldo final é {saldo:.2f}")
