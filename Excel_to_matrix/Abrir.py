import pandas as pd
import xlsxwriter


outWorkbook = xlsxwriter.Workbook('Teste.xlsx')
outSheet = outWorkbook.add_worksheet()


#ler os dados colocar os dados em uma lista
dados = pd.read_excel('//Users/evaldonneto/Downloads/times.xlsx')
dados.dropna(inplace= True)
pessoas = dados['Pessoas'].str.split("\n", expand = False)
times = dados['Times'].str.split("\n", expand = False)


outSheet.write('A1', 'Pessoas')
outSheet.write('B1', 'Times')
for item in range(len(pessoas[0])):
    outSheet.write(item+1,0,pessoas[0][item])
    outSheet.write(item+1,1,times[0][item])
    
outWorkbook.close()