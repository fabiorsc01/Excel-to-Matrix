import pandas as pd
import xlsxwriter

outWorkbook = xlsxwriter.Workbook("Resultado.xlsx")
outSheet = outWorkbook.add_worksheet()

#ler os dados colocar os dados em uma lista
dados = pd.read_excel('Teste1.xlsx')
dados.dropna(inplace= True)

etapas = dados['Etapas'].str.split("\n", expand = False)
resultados = dados['Resultados'].str.split("\n", expand = False)

lista_dados= []
outSheet.write('F1', 'Passos')
for i in range(len(etapas)):
    for etapa, result in zip(etapas[i], resultados[i]):
        lista_dados.append(etapa + ' ' + result +'\n')
    b = ''.join(lista_dados)
    outSheet.write(i+1,5,b) 
    print(lista_dados)
    lista_dados=[]
    
outSheet.write(0,0,'Ref')
outSheet.write(0,1,'Folder')
outSheet.write(0,2,'Title')
outSheet.write(0,3,'Descrição')
outSheet.write(0,4,'Condição inicial')
outSheet.write(0,6,'Comentários')                 
                   
outWorkbook.close()