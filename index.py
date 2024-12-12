import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
data = pd.read_csv('/content/sample_data/SSH.csv')

# Função para análise e visualização do dataset
def analyze_ssh_data(data):
    # Informações gerais sobre o dataset
    print("\nInformações do Dataset:")
    print(data.info())

    print("\nPrimeiras Linhas do Dataset:")
    print(data.head())

    # Verificar valores ausentes
    print("\nValores Ausentes por Coluna:")
    print(data.isnull().sum())

    # Distribuição das variáveis binárias
    binary_columns = ['is_private', 'is_failure', 'is_root', 'is_valid', 'class']
    plt.figure(figsize=(15, 8))
    for i, col in enumerate(binary_columns, 1):
        plt.subplot(2, 3, i)
        sns.countplot(x=col, data=data, palette="coolwarm")
        plt.title(f'Distribuição de {col}')
    plt.tight_layout()
    plt.show()

    # Correlação entre variáveis numéricas
    numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
    plt.figure(figsize=(10, 8))
    correlation_matrix = data[numeric_columns].corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Matriz de Correlação")
    plt.show()

    # Análise temporal (se aplicável)
    if 'ts' in data.columns:
        plt.figure(figsize=(12, 6))
        data['timestamp'] = pd.to_datetime(data['ts'], unit='s')
        sns.lineplot(x='timestamp', y='is_failure', data=data, label='Falhas')
        sns.lineplot(x='timestamp', y='is_valid', data=data, label='Validações')
        plt.title("Tendências Temporais de Falhas e Sucessos")
        plt.xlabel("Tempo")
        plt.ylabel("Contagem")
        plt.legend()
        plt.show()

    # Comparação entre sucesso e falha
    if 'class' in data.columns:
        plt.figure(figsize=(12, 6))
        sns.countplot(x='class', hue='is_failure', data=data, palette='coolwarm')
        plt.title("Comparação de Classes com Falhas")
        plt.xlabel("Classe")
        plt.ylabel("Contagem")
        plt.legend(title='Falha')
        plt.show()

# Chamar a função de análise
analyze_ssh_data(data)
