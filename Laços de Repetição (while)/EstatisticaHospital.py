#Um hospital quer conhecer melhor o público de seu pronto atendimento para decidir qual tipo de investimento é mais prioritário. 
#Para isso, faça um programa que pergunta repetidamente para o usuário a idade do paciente. 
#Quando o usuário digita um número negativo o programa mostra o texto a seguir e termina:
#0-11 anos: A.AA %
#12-17 anos: B.BB %
#18-25 anos: C.CC %
#26-35 anos: D.DD %
#36-59 anos: E.EE %
#Acima de 60 anos: F.FF %


idade=int(input())
a=0
b=0
c=0
d=0
e=0
f=0
while idade>=0:
    if 0<=idade<=11:
        a+=1
    if 12<=idade<=17:
        b+=1
    if 18<=idade<=25:
        c+=1
    if 26<=idade<=35:
        d+=1
    if 36<=idade<=59:
        e+=1
    if idade>=60:
        f+=1
    idade=int(input())
s=a+b+c+d+e+f
A=a/s*100
B=b/s*100
C=c/s*100
D=d/s*100
E=e/s*100
F=f/s*100
print(f"0-11 anos: {A:.2f} %\n12-17 anos: {B:.2f} %\n18-25 anos: {C:.2f} %\n26-35 anos: {D:.2f} %\n36-59 anos: {E:.2f} %\nAcima de 60 anos: {F:.2f} %")
