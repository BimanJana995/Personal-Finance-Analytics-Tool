import matplotlib.pyplot as plt
import pandas as pd
def show_chart():
    df = pd.read_csv('finance_data.csv')
    # Category ke hisab se group karna
    category_data = df.groupby('Category')['Amount'].sum()
    
    # Pie chart banana
    category_data.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Mera Kharcha (Category-wise)')
    plt.show()

show_chart()
