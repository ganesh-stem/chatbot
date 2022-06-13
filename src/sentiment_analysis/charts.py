import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def donut_chart(sizes, colors, labels):
    fig1, (ax1, ax2) = plt.subplots(1, 2)

    ax1.pie(sizes[0], colors = colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=.2))
    ax2.pie(sizes[1], colors = colors, autopct='%1.1f%%', startangle=90)

    #draw circle
    centre_circle = plt.Circle((0,0),0.80,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.set_title('You')
    ax1.axis('equal')  

    ax2.set_title('Bot')
    ax2.axis('equal')  
    ax2.legend(labels, bbox_to_anchor=(1,0), loc="lower right", bbox_transform=plt.gcf().transFigure)

    plt.tight_layout()

    fig1.savefig('sentiment_analysis\outputs\sa.png')
    fig1.savefig("media\language\sa\sa.png")