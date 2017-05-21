#!/usr/bin/env python
import sys, os
import yaml
import numpy as np
import pandas as pd

class Transform():
    def __init__(self, data, idx):
        self.__data = data
        self.__idx = idx
        
        #print self.__idx
        #print self.__data
        #print self.__agent
        #print "\n"
        # the main configuration file 
        self.__config_fname = 'config_transform.yaml'

    def main_method():
        # call the get variable function here, and call the yes no condition to write to a hdf
        # do the write to HDF    









    # Function to parse transformation parameters from the configuration file
    def get_variables(self):
        try:
            f = open(self.__config_fname, 'r')
        except IOError:
            erf("unable to read file: %s" % self.__config_fname)

        with f as stream:
            try:
                p = yaml.load(stream)
            except yaml.YAMLError, exc: # error-check for incorrect yaml syntax
                if hasattr(exc, 'problem_mark'):
                    mark = exc.problem_mark
                    print " >> Error in line: (%s:%s) in file: %s" % (mark.line+1, mark.column+1, self.__config_fname)
                else:
                    print " >> Unknown problem with %s file:" % self.__config_fname
                sys.exit()

            variables = p[self.__idx]['variables']
            #print variables.values()
            #print self.__data[variables.values()]            
            return p[self.__idx]['variables']      

#TODO: Change the data in below functions with the data returned from get_parameters function above

    def q_o_q(self,fn): # method to print quaterly growth rate (quarter on quarter)
        variables = self.get_variables()
        def mean():
            roll_mean = self.__data[variables.values()].rolling(window=3,min_periods=3).mean().dropna() # first get rolling window values with step 3 and initial buffer 3
            return roll_mean[::3].pct_change(4) # compute rate between values with a step size 4 
            
        def summation():
            roll_sum = self.__data[variables.values()].rolling(window=3,min_periods=3).sum().dropna()
            return roll_sum[::3].pct_change(4)
            
        f_mapper = {'mean': mean, 'sum': summation} # map the function to apply with the desired input    
        return f_mapper[fn]()




    def m_o_m(self): # method to print monthly growth rate (month on month)
        variables = self.get_variables()
        return self.__data[variables.values()].pct_change(12)


    def m_o_m_ONE_CYCLE(self): # method to print monthly growth rate (month on month in one cycle)
        variables = self.get_variables()
        return self.__data[variables.values()].pct_change(1)




    def annual_P_I_T(self,fn): # method to print annual growth rate, point in time. TODO: point in time not added yet
        variables = self.get_variables()
        def mean():
            roll_mean = self.__data[variables.values()].rolling(window=12,min_periods=12).mean().dropna() # first get rolling window values with step 12 and initial buffer 12
            return (roll_mean[::12]).pct_change(1) # compute rate between values with a step size 1
               
        def summation():
            roll_sum = self.__data[variables.values()].rolling(window=12,min_periods=12).sum().dropna()
            return (roll_sum[::12]).pct_change(1)
            
        f_mapper = {'mean': mean, 'sum': summation} # map the function to apply with the desired input    
        return f_mapper[fn]()



    def q_o_q_ONE_CYCLE(self,fn): # method to print quaterly growth rate (quarter on quarter)
        variables = self.get_variables()
        def mean():
            roll_mean = self.__data[variables.values()].rolling(window=3,min_periods=3).mean().dropna() # first get rolling window values with step 3 and initial buffer 3
            return roll_mean[::3].pct_change(1) # compute rate between values with a step size 4 
            
        def summation():
            roll_sum = self.__data[variables.values()].rolling(window=3,min_periods=3).sum().dropna()
            return roll_sum[::3].pct_change(1)
            
        f_mapper = {'mean': mean, 'sum': summation} # map the function to apply with the desired input    
        return f_mapper[fn]()


    