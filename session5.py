from typing import List 
import time


def time_it(fn, *args, repetitons= 1, **kwargs):

    if fn == 'temp_converter':
        start_time = time.time()
        for _ in range( repetitons ):
            temp_converter(args)
        end_time = time.time()
        return (end_time-start_time)/repetitons
    elif fn == 'polygon_area':
        start_time = time.time()
        for _ in range( repetitons ):
            temp_converter(args)
        end_time = time.time()
        return (end_time-start_time)/repetitons



def temp_converter(temp , temp_given_in= 'F'):

    if temp < 0:
        raise ValueError("Input Temperature is Negative")
    else:
        if temp_given_in.upper() == 'F':
            t = (temp-32)*5/9
            return t
        elif temp_given_in.upper() == 'C':
            t = 9/5 * (temp) + 32
            return t
        elif temp_given_in.upper() not in ('C' , 'F'):
            raise NotImplementedError("Invalid Temperature Coneversion")



def polygon_area(side_length = 1 , side = 3 ):

    if side_length <= 0:
        raise ValueError("How come Side is zero.")
    else:
        if side <= 0 or side >=7:
            raise NotImplementedError 
        elif side in ( 2 , 1 ):
            raise ValueError("No Polygon of Side 1 & 2 Exists")
        elif side == 3:
            return True
        elif side == 4:
            return side_length*side_length
        elif side == 5:
            return True
        elif side == 6:
            return True



def speed_converter(speed , dist = 'KM', time = 'HR'):

    if speed < 0 or type(dist) == str or type(time) == str:
        raise ValueError("Invalid Input Format")
    else:
        if dist.upper == 'KM':
            if time.upper()  == 'S':
                return True
            elif time.upper == 'MS':
                return True
            elif time.upper() == 'M':
                return True
            elif time.upper() == 'HR':
                return True
            elif time.upper() == 'DAY':
                return True
            else:
                raise ValueError("Valid Distance Invalid Time")
        elif dist.upper == 'M':
            if time.upper()  == 'S':
                return True
            elif time.upper == 'MS':
                return True
            elif time.upper() == 'M':
                return True
            elif time.upper() == 'HR':
                return True
            elif time.upper() == 'DAY':
                return True
            else:
                raise ValueError("Valid Distance Invalid Time")
        elif dist.upper == 'FT':
            if time.upper()  == 'S':
                return True
            elif time.upper == 'MS':
                return True
            elif time.upper() == 'M':
                return True
            elif time.upper() == 'HR':
                return True
            elif time.upper() == 'DAY':
                return True
            else:
                raise ValueError("Valid Distance Invalid Time")
        elif dist.upper == 'YRD':
            if time.upper()  == 'S':
                return True
            elif time.upper == 'MS':
                return True
            elif time.upper() == 'M':
                return True
            elif time.upper() == 'HR':
                return True
            elif time.upper() == 'DAY':
                return True
            else:
                raise ValueError("Valid Distance Invalid Time")
        else:
            raise ValueError("Invalid User Distance Input")





def squared_power_list( number , start = 0 , end = 5 ):

    a = []
    if type(start) != int or type(end) != int or type(number) != int :
        raise ValueError("String Input Not allowed")
    elif number < 0 :
        raise ValueError("Negative Number Not allowed")
    else:
        if start > end :
            raise ValueError("proper number start and end is not mentioned")
        else:
            for i in range( start , end+1 ):
                a.append( number**i )
            return a
