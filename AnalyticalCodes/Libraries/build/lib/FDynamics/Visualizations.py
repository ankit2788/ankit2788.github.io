from abc import ABC, abstractmethod
from FDynamics.Utils import GetReadableTime
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

class Animation(ABC):
    '''
    ABC class for all animation objects
    '''
    
    @abstractmethod
    def initFigure(self, Plotlimits = None , fig = None, axis = None):
        '''
        This is a generic method and shoudl be used by all animation logics while initializing the figure.
        Sets up the figure for animation.
        Returns fig and axis objects.

        If Plotlimits are not provided --> fig, axis are returned as None
        '''

        pass
        
    
    @abstractmethod
    def initPlotElements(self, axis = None):
        '''
        initializes the plot elements which are supposed to be animated
        '''
        pass
    
    @abstractmethod
    def initAnimation(self):
        '''
        Initialization to plot the background of each frame
        '''
        pass

    @abstractmethod
    def SequentialAnimate(self, frame):
        '''
        Animation function and is called sequentially
        '''
        pass

    @abstractmethod
    def RunAnimation(self, Plotlimits = None, fig = None, axis = None, interval = 10):
        pass




class Stills(ABC):
    """
    ABC for all still plots
    """
    
    @abstractmethod
    def Plot(self):
        '''
        plots the timeseries
        '''
        pass


class CurveAnimation(Animation):

    @abstractmethod
    def __init__(self, X_AxisDetails, CurveDetails, CurveLabel):
        '''
        Initialize the Animation object with below attributes:
        Inputs: 
            X_AxisDetails --> Dataframe object to be plotted on X-axis. 
            CurveDetails --> tuple of Curve at every instant 
            
        '''
        self.CurveDetails       = CurveDetails
        self.CurveLabel         = CurveLabel
        self.X_AxisDetails      = X_AxisDetails
        
        #Nb of IV curves to be plotted along side (Bid, Ask, Fit etc)
        self.NbCurves = len(CurveDetails)
        self.Timers = list(X_AxisDetails.index)


    def initFigure(self, Plotlimits = None , fig = None, axis = None):
        '''
        If plot limits are not provided, this method sets the limits, 
        and then calls the base class method of initailizing the figure
        '''

        #set plot limits
        if Plotlimits is None:
            X_lim, Y_lim    = None, None
        else:
            X_lim, Y_lim    = Plotlimits[0], Plotlimits[1]
        
        #set up the figure and axis and plot elements we need to animate
        if ((fig is None) & (axis is None) & (Y_lim is not None)):            
            fig     = plt.figure()
            if X_lim is not None:
                axis    = plt.axes(xlim = X_lim, ylim = Y_lim)
            else:
                axis    = plt.axes(ylim = Y_lim)
        else:
            fig     = None
            axis    = None  

        return fig, axis


    def initPlotElements(self, axis = None):
        '''
        initializes the plot elements which are supposed to be animated
        '''

        if axis is None:
            pass
        else:
            self.lines = []
            for i in np.arange(self.NbCurves):
                objline,    = axis.plot([], [], ls = "dashed",lw = 0.5, marker = "x", markersize = 5, markerfacecolor = "red", label = self.CurveLabel[i])
                self.lines.append(objline)
            
            #self.TimeText      = axis.text(0.02, 0.5, "", transform = axis.transAxes)
            self.TimeText      = axis.text(0.45, 0.9, "", transform = axis.transAxes)
            



    def initAnimation(self):
        '''
        Initialization to plot the background of each frame
        '''

        for line in self.lines:
            line.set_data([],[])
        
        return tuple(self.lines) 
        

    def SequentialAnimate(self, frame, timer_in_epoch = False, time_dateobject = False):
        '''
        Animation function and is called sequentially
        '''
        timer = self.Timers[frame]
        if timer_in_epoch:
            self.TimeText.set_text("{0}".format(GetReadableTime(timer)))
        else:
            if time_dateobject:
                self.TimeText.set_text("{0}".format(timer.strftime("%Y, %b %d")))
            else:
                self.TimeText.set_text("{0}".format(timer))

        x = self.X_AxisDetails.loc[timer]      #Strikes to be plotted on X axis

        for Nbline, line in enumerate(self.lines):
            y = self.CurveDetails[Nbline].loc[timer]
            line.set_data(x, y)
        
        return tuple(self.lines) +  (self.TimeText,)


    def RunAnimation(self, Plotlimits = None, fig = None, axis = None, interval = 10, timer_in_epoch = True, time_dateobject = False):

        pass

        

