import pandas as pd
import matplotlib.pyplot as plt

def makeHistogram(Data):
    key_list = list(Data.keys())
    xName = key_list[0]
    yName = key_list[1]
    df = pd.DataFrame(Data,columns=[xName,yName])
    df.plot(x = xName, y= yName, kind = 'bar')
    plt.show()

def main():
    # Data = {'Country': ['USA','Canada','Germany','UK','France'],
    #         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
    # }

    Data = {'Data Scientist, USA': ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY'], 'Number of job':[78112,454163,287754,896481,5841354,1124741,458416,174988,123715,2259177,1297760,110014,310762,200847,1554790,736053,277829,409769,406856,1276979,952217,119656,899514,779235,556498,251131,83152,1086100,80801,156510,162360,1053763,189041,382632,1771785,1282502,335615,467366,1722800,104092,567580,63652,767854,3355422,358381,1695499,52227,3033877,594778,151314,77381]}

    makeHistogram(Data)

if __name__ == "__main__":
    main()
