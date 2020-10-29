#!/usr/bin/env python
# coding: utf-8

import numpy as np
import seaborn as sns
import matplotlib


def turnIntoAMPM(x):
    if x > 11:
        if x == 12:
            return '12 PM'
        return "{} PM".format(x - 12)
    else:
        return "{} AM".format(x)
    
def textFormat(textParams,value, num =True,comma =True,decimal = 0 ):
    percent = textParams["percent"]
    dollar = textParams["dollar"] 
    if num:
        if comma: return f"{dollar}{round(int(float(value)),decimal):,} {percent}" 
        else: return f"{round(int(float(value)),decimal):} {percent}" 
        
    else: return f"{dollar}{value}"
    
def shorten(num, precision=2, suffixes=['', 'K', 'M', 'G', 'T', 'P']):
    if num < 1:
        return num  # avoid dividing by 0 or negatives
    m = int(log10(num) // 3)
    return f'{num/1000.0**m:.{precision}f}{suffixes[m]}'
              
def textAnnotationV(ax, modifyAxisText = False, precision = 2, textParams={"percent":"","dollar":""},**kwargs): 
    for bar in ax.patches:
        height = bar.get_height()
        position = bar.get_x()
        centerOfBarWidth = bar.get_width()/2
        if modifyAxisText:
            s = textFormat(textParams,shorten(height,precision=precision))  
        else s= textFormat(textParams,height)
        ax.text(( position + centerOfBarWidth), height,s, **kwargs)
        
def textAnnotationH(ax,modifyAxisText = False,precision=2,textParams={"percent":"","dollar":""},**kwargs):
    for bar in ax.patches:
        x = bar.get_height()/2+ bar.get_width()
        y = bar.get_y()+ bar.get_height()/2
        if modifyAxisText:
            s = textFormat(textParams,shorten(bar.get_width(),precision=precision))
        else: textFormat(textParams,bar.get_width())
        ax.text(x,y,s, **kwargs)
              


def missing_values(data):
    """
    Function that takes in a dataframe, iterates over each of its columns and checks for
    common indicators of missing values (ie. negative values).   

    Args:
         data (pandas.DataFrame): Dataframe to be checked

    Returns:
        list (dict): a list containing (if any) a dictionar[y/ies] of key:value pair in the 
        following format - {column's missing value: % of column's missing value} - sorted in descending order
    """
    faultyData = {}
    if len(data.columns) <= 0:
        print('Something went wrong. No columns detected.')
    lenData = len(data)

    # iterate through all columns in dataset to search for each defined missing value
    for col in data.columns:
        if data[col].isnull().any():
            percentMissing = data[col].isnull().sum() / lenData
            # null
            faultyData[col] = f"Null values in {col}: {round(percentMissing*100,2)}"

        try:
            if len(np.where(data[col] == '')) > 1:
                percentMissing = len(data[data[col] == '']) / lenData
                # empty string
                faultyData[col] = f"Empty string values in {col}: {round(percentMissing*100,2)}"
        except:
            print(col)

        # if value is a number and less than 0
        if np.issubdtype(data[col].dtype, np.number) and len(data[data[col] < 0]) > 1:
            percentMissing = len(data[data[col] < 0]) / lenData
            # negative value
            faultyData[col] = f"Negative values in {col}: {round(percentMissing*100,2)}"

        commonFaultyValues = ['n/a', 'na', 'an', 'n\a', '?', 'none', 'null']
        try:
            if len(data[data[col].str.lower.isin(commonFaultyValues)]) > 1:
                percentMissing = len(
                    data[data[i].str.lower.isin(commonFaultyValues)]) / lenData
                # other
                faultyData[col] = f"Other null values present in {col}: {round(percentMissing*100,2)}"
        except:
            print(col)

    return sorted(faultyData.items(),
                  key=lambda x: float(faultyData[x[0]].split(' ')[-1]),
                  reverse=True)

def modifyChartBasic(ax,title,labelSize,xLabel='',yLabel='',grid=False,
                titleSize=False):
    """
    Function that takes in graph variables for the purpose of customizing basic 
    default settings (ie. setting label size)
    """
    if titleSize != False:
        ax.set_title(title,fontsize=titleSize,fontweight='semibold', pad=10)
    else:
        ax.set_title(title)
    if grid:
        ax.grid(axis=grid, alpha=.4)
    # spines
    sns.despine()
    ax.spines['bottom'].set_color('gray')
    ax.spines['left'].set_color('lightgrey')

    # labels
    ax.set_ylabel(yLabel, labelpad=5, fontsize=16)
    ax.set_xlabel(xLabel, labelpad=5, fontsize=16)

    # tick settings
    ax.tick_params(labelsize=labelSize)
    ax.tick_params(axis='both', left=False, bottom=False)

def modifyChartExtra(ax,maxs=False,highlightTop =False,
                 highlightXVal=False, topValueColor=False,grayTickLabels=False,topChild=None):
    """
    Main Function used to create extra modifications to chart. 
    """
    if maxs:
        modifyMaxYTick(ax,maxs,highlightTop)
    if topValueColor:
        modifyMaxValueColor(ax,topValueColor,topChild)
     # changing size and color of tick labels (ticks are set to 0 to not display)   
    ax.tick_params(labelsize=15, size=0, labelcolor='#8a8a8d' if grayTickLabels else 'black')
    if highlightTop:
        ax.get_yticklabels()[-1].set_color('black')
    if highlightXVal:
        # get first x ticklabel and set color to black
        ax.get_xticklabels()[0].set_color('black')

def modifyMaxYTick(ax, maxValue,highlightTop):
    """
    Function that modifies y-scale to have the top y-tick label represent the maximum value
    whilst 'preventing' overlap between the last and second to last tick labels 
    """  
    # keep all except last  tick - ensure that the ticks don't overlap
    midCenterQuarter = (ax.get_yticks()[1] - ax.get_yticks()[0]) / 4

    ax.set_ylim(0, maxValue)  # set the yticks
    # add the last tick value
    y_ticks = np.append(
        [i for i in ax.get_yticks() if i < (maxValue - midCenterQuarter)], [maxValue])
    # set the modified y ticks
    ax.set_yticks(y_ticks)
    
def modifyMaxValueColor(ax,topValueColor,topChild):
    """
    Function that changes that modifies the color of the first child artist 
    (here meant to represent the rectangle artist that maps to the top value; if values in descending order and a bar graph)
    of the main artist object
    """  
    if topChild is None:
        topChild = ax.get_children()[0]
        topChild.set_color(topValueColor)
    else:
        topChild.set_color(topValueColor)
    topChild.set_alpha(.8)

def count_valuesUpdateDictionary(x, counts):
    #if numerical, check if null 
    if x=='nan' or x==None or (type(x) in [float, int] and math.isnan(x)): 
        return counts
    
    #if not null 
    counts.setdefault(x, 0)
    counts[x] = counts.get(x,0)+1
    return counts

def count_values(df, columnName, noFalse=None):
    """ Custom count values function that takes into account a list's inner values.

    Args:
        df (pd.Dataframe): dataframe of interest
        columnName (str): column of interest
        noFalse(varies, optional): the value to ignore
    Return:
        dict: a dictionary with all the values and their respective counts 
    """
   
    counts={}
    for val in df[columnName].values:
        if isinstance(val,(np.ndarray, list)):#if a list
            for i in val:
                if isinstance(i,(np.ndarray, list)): #if a sublist
                    for sub in i: 
                        counts= count_valuesUpdateDictionary(sub, counts)
                else:  #if not a sublist  
                    counts = count_valuesUpdateDictionary(i, counts)
        else: 
            counts =count_valuesUpdateDictionary(val, counts)
            
    if noFalse != None: 
        #filter out the value to ignore, typically a False value
        return  {i[0]:i[1] for i in counts.items() if i[0] != noFalse}
    return counts

