#Entrada
#Campanha de concientização ambiental
tipo_de_imovel = input ("Informe o tipo de seu imovel (ex.: casa, apartamento ou comercial): ")
consumo_mensal = float (input ("Informe o consumo mensal de àgua do seu imóvel em cubagem (m3): "))

#Verificação das condições
if tipo_de_imovel not in ["comercial", "casa", "apartamento"]:
    print("Tipo de imóvel inválido.")
elif tipo_de_imovel == "comercial":
    print ("Tarifa comercial aplicada - consulte o plano corporativo")
elif tipo_de_imovel == "apartamento" and consumo_mensal < 10:
    print ("Consumo economico - excelente controle de agua!")
elif tipo_de_imovel == "apartamento" or (tipo_de_imovel == "casa" and consumo_mensal <= 25) :
    print ("Consumo moderado - dentro do padrao residencial.")
else:
    print ("Consumo excessivo - adote medidas de economia ou verifique possiveis vazamentos.")