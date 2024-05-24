import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def citeste_csv(file_path):
    """
    Funcția citește un fișier CSV și returnează un DataFrame Pandas
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Fișierul '{file_path}' nu a fost găsit.")
    except pd.errors.EmptyDataError:
        print(f"Fișierul '{file_path}' este gol.")
    except pd.errors.ParserError:
        print(f"A existat o eroare la parsarea fișierului '{file_path}'.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")


def extrage_statistici_si_genereaza_boxplot(df):
    """
    Funcția extrage statistici pentru atributele numerice continue și generează grafice Boxplot.

    :param df: DataFrame Pandas cu datele din fișierul CSV
    """

    # Afișează statisticile
    stats = df.describe(percentiles=[.25, .5, .75], include=[np.number])
    print("Statistici pentru atributele numerice continue:")
    print(stats, '\n')

    # Generează grafice Boxplot
    plt.figure(figsize=(10, 8))
    df.boxplot()
    plt.title('Boxplot pentru atributele numerice continue')
    plt.xticks(rotation=90)
    # plt.show()

def extrage_statistici_atribute_discrete_si_ordinale(df):
    """
    Funcția extrage statistici pentru atributele discrete sau ordinale.

    :param df: DataFrame Pandas cu datele din fișierul CSV
    """

    # Afișează statisticile
    print("Statistici pentru atributele discrete sau ordinale:")

    stats = df.describe(include=['O', 'category'])
    stats = stats.loc[['count', 'unique']]
    print(stats, '\n')

if __name__ == "__main__":
    # Exemplu de utilizare
    file_path = './tema2_SalaryPrediction/SalaryPrediction_full.csv'
    
    # Citește datele din fișier
    df = citeste_csv(file_path)
    
    # Verifică dacă DataFrame-ul a fost creat și afișează primele 5 rânduri
    if df is not None:
        print(df.head())

        # Extrage statistici și generează grafice Boxplot
        extrage_statistici_si_genereaza_boxplot(df)

        # Extrage statistici pentru atributele discrete sau ordinale
        extrage_statistici_atribute_discrete_si_ordinale(df)
