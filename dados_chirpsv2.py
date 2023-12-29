# -*- coding: utf-8 -*-
""" Bibiotecas """

import urllib.request
import xarray as xr
import pyproj
import salem
import rasterio as roi
import warnings
warnings.filterwarnings("ignore")

""" Ficheiro .shp para Mascarar a area de Interesse """

shp = salem.read_shapefile('caminho_do_ficheiro')

""" Dados CHIRPSv2 - Um loop com a range do intervalo de dados necessario... """

for yr in range(1981, 2024):
    url = f'https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/netcdf/p05/chirps-v2.0.{yr}.days_p05.nc'
    savename = url.split('/')[-1]
    urllib.request.urlretrieve(url, savename)

""" Abrir e manipular... """

dados = xr.open_mfdataset('chirps-v2.0.*.days_p05.nc', concat_dim='time', combine='nested')

clima_81_10 = dados.sel(longitude=slice(0, 52),
                        latitude=slice(-35, 6),
                        time=slice('1981-01-01', '2010-12-01'))

clima_81_10 = clima_81_10.groupby('time.year').sum('time')

clima_81_10_avg = clima_81_10.mean('year')
