Años = {2000 :366, 2001: 365, 2002: 365, 2003: 365, 2004: 366, 2005: 365, 2006: 365, 2007: 365, 2008: 366, 2009: 365, 2010: 365, 2011: 365, 2012: 366,
 2013: 365, 2014: 365, 2015: 365, 2016: 366, 2017: 365, 2018: 365, 2019: 365, 2020: 366, 2021: 365, 2022: 365, 2023: 365,}



clave = (int (input("escriba un numero entre 2000 y 2023: ")))
if clave in Años:
    if clave== (2000 or 2004 or 2008 or 2012 or 2016 or 2020):
        print(f'el año {clave} es biciesto')
    else:
        print(f'el año {clave} no es binario')
else :
     print(f'el año {clave} no es esta')

