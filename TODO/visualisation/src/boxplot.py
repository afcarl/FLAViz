import pandas as pd
import matplotlib.pyplot as plt

from summarystats import SummaryStats

class Boxplot():
    def __init__(self, data, n, num_plots, analysis_type):
        self.__data = data
        self.__N = n
        self.__analysis_type = analysis_type
        self.__num_plots = num_plots        
        #print self.__data

    def single_output(self):
        s = SummaryStats(self.__data, self.__analysis_type )    
        print s.mean()
        box_df = pd.DataFrame()
        box_df['mean'] = s.mean()
        box_df['median'] = s.median()
        box_df['upper_quartile'] = s.upper_quartile()
        box_df['lower_quartile'] = s.lower_quartile()
        box_df['max'] = s.maximum()
        box_df['min'] = s.minimum()
        
        bp = box_df.boxplot(column = ['min','median','mean','upper_quartile','lower_quartile','max'], positions =[1,3,4,5,2,6])
        # plt.hold(True)        
        plt.savefig('boxplot_main.png', bbox_inches='tight')  
        plt.close()


    def multiple_output(self):
        s = SummaryStats(self.__data, self.__analysis_type )           
        box_df = pd.DataFrame()
        box_df['mean'] = s.mean()
        box_df['median'] = s.median()
        box_df['upper_quartile'] = s.upper_quartile()
        box_df['lower_quartile'] = s.lower_quartile()
        box_df['max'] = s.maximum()
        box_df['min'] = s.minimum()

        count = 0
        for i in range(0,len(box_df.index)/self.__N):                    
            tmp_df = box_df[count:count+self.__N]
            bp = tmp_df.boxplot(column = ['min','median','mean','upper_quartile','lower_quartile','max'], positions =[1,3,4,5,2,6])
            plot_name = "boxplot_"+str(i)+".png"        
            plt.savefig(plot_name, bbox_inches='tight')  
            plt.clf()           
            count = count + self.__N
        plt.close()

