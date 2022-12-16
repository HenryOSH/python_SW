import mpld3
import pandas as pd
import matplotlib as plt
import seaborn as sns

def  sample_plot(df, title):
    df.plot(kind='line',
            marker='p',
            color=['blue','red'],
            lw=3,
            ms=28,
            alpha=0.7)
    plt.title(title)
    plt.text(s='blue line', x=1.7, y=2.5, color='blue')
    plt.text(s='red line', x=2.6, y=1.3, color='red')

data = {
    'c1': [1,3,2,4],
    'c2': [3,4,1,2]
}
df = pd.DataFrame(data)

sample_plot(df, 'matplotlib')
plt.show()