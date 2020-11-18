import pandas as pd
import matplotlib.pyplot as plt

def main():   
    # Data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
    #         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
    #        }

    # df = pd.DataFrame(Data,columns=['Year','Unemployment_Rate'])
    # df.plot(x ='Year', y='Unemployment_Rate', kind = 'line')
    # plt.show()

    Data = {'Country': ['USA','Canada','Germany','UK','France'],
        'GDP_Per_Capita': [45000,42000,52000,49000,47000]
       }
  
    df = pd.DataFrame(Data,columns=['Country','GDP_Per_Capita'])
    df.plot(x ='Country', y='GDP_Per_Capita', kind = 'bar')
    plt.show()

if __name__ == "__main__":
    main()
