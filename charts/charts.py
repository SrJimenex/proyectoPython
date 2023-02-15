import matplotlib.pyplot as plt
def creador_de_grafica_pie():
    values = [200,50,150]
    labels = ['A','B','C']
    fig, ax = plt.subplots()
    ax.pie(values,labels = labels)
    plt.savefig('pie.png')
    plt.close()
