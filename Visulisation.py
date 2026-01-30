import matplotlib.pyplot as plt
import pandas as pd
def show_chart():
    df = pd.read_csv('finance_data.csv')
    category_data = df.groupby('Category')['Amount'].sum()
    
    category_data.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Mera Kharcha (Category-wise)')
    plt.show()

show_chart()

