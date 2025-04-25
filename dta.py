import pandas as pd

base_dados = pd.read_csv("Tratamento-Dados\Cópia de Base_despadronizada - Base_Corrigida.csv")

base_dados['sexo'] = base_dados['sexo'].str.strip().str.lower()

map_sexo = {
    'm': 'Masculino', 'masc': 'Masculino', 'masculino': 'Masculino',
    'f': 'Feminino', 'fem': 'Feminino', 'feminino': 'Feminino'
}

base_dados['sexo'] = base_dados['sexo'].map(map_sexo)


base_dados['nota_matematica'] = base_dados['nota_matematica'].astype(str).str.replace(',', '.').astype(float)
base_dados['nota_portugues'] = base_dados['nota_portugues'].astype(str).str.replace(',', '.').astype(float)
base_dados['frequencia'] = base_dados['frequencia'].astype(str).str.replace(',', '.').astype(float)
base_dados['media'] = (base_dados['nota_matematica'] + base_dados['nota_portugues'] + (base_dados['frequencia'] / 10)) / 3



def verificar_aprovacao(media):
    if media >= 7:
        return 'Sim'
    else:
        return 'Não'
    
base_dados['aprovado'] = base_dados['media'].apply(verificar_aprovacao)

base_dados['nota_matematica'] = base_dados['nota_matematica'].astype(str).str.replace('.', ',')
base_dados['nota_portugues'] = base_dados['nota_portugues'].astype(str).str.replace('.', ',')
base_dados['media'] = base_dados['media'].astype(str).str.replace('.', ',')
base_dados['frequencia'] = base_dados['frequencia'].astype(str).str.replace('.', ',')


print(base_dados)















