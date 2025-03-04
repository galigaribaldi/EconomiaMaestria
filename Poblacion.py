import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Poblacion:
    
    ##Totales
    df_base_totales = []
    abajo_totales = 0
    arriba_totales = 0
    indice_envejecimiento_totales = 0
    ID_suma_arriba_totales = 0
    ID_suma_abajo_totales = 0
    IDependencia_totales = 0
    total_poblacion = 0
    total_poblacion_hombres = 0
    total_poblacion_mujeres = 0
    
    ##Rango
    df_base_rango = []
    abajo_rango = 0
    arriba_rango = 0
    indice_envejecimiento_rango = 0
    ID_suma_arriba_rango = 0
    ID_suma_abajo_rango = 0
    IDependencia_rango = 0
    rango_poblacion = 0
    rango_poblacion_hombres = 0
    rango_poblacion_mujeres = 0
    
    def __init__(self, base_totales):
        self.df_base_totales = base_totales
        self.df_base_rango = base_totales

    def totalesPoblacion(self):
        self.total_poblacion = int(self.df_base_totales["Poblacion_Total"].sum())
        self.total_poblacion_hombres = int(self.df_base_totales["Poblacion_Hombres"].sum())
        self.total_poblacion_mujeres = int(self.df_base_totales["Poblacion_Mujeres"].sum())
        
    def indiceEnvejecimientoTotal(self):
        df_filtrados_envejecimiento_Arriba = self.df_base_totales[
            (self.df_base_totales['Grupos_año_edad']=='0 meses') | (self.df_base_totales['Grupos_año_edad']=='1 mes') |
            (self.df_base_totales['Grupos_año_edad']=='2 meses') | (self.df_base_totales['Grupos_año_edad']=='7 meses') |
            (self.df_base_totales['Grupos_año_edad']=='3 meses') | (self.df_base_totales['Grupos_año_edad']=='8 meses') |
            (self.df_base_totales['Grupos_año_edad']=='4 meses') | (self.df_base_totales['Grupos_año_edad']=='9 meses') |
            (self.df_base_totales['Grupos_año_edad']=='5 meses') | (self.df_base_totales['Grupos_año_edad']=='10 meses') |
            (self.df_base_totales['Grupos_año_edad']=='6 meses') | (self.df_base_totales['Grupos_año_edad']=='11 meses') |
            (self.df_base_totales['Grupos_año_edad']=='12 meses') |
            (self.df_base_totales['Grupos_año_edad']=='Menores de 1 año') | (self.df_base_totales['Grupos_año_edad']=='0 años')  |
            (self.df_base_totales['Grupos_año_edad']=='1 año')   | (self.df_base_totales['Grupos_año_edad']=='2 años')  |
            (self.df_base_totales['Grupos_año_edad']=='3 años')  | (self.df_base_totales['Grupos_año_edad']=='4 años')  |
            (self.df_base_totales['Grupos_año_edad']=='5 años')  | (self.df_base_totales['Grupos_año_edad']=='6 años')  |
            (self.df_base_totales['Grupos_año_edad']=='7 años')  | (self.df_base_totales['Grupos_año_edad']=='8 años')  |
            (self.df_base_totales['Grupos_año_edad']=='9 años')  | (self.df_base_totales['Grupos_año_edad']=='10 años') |
            (self.df_base_totales['Grupos_año_edad']=='11 años') | (self.df_base_totales['Grupos_año_edad']=='12 años') |
            (self.df_base_totales['Grupos_año_edad']=='13 años') | (self.df_base_totales['Grupos_año_edad']=='14 años') 
        ]

        df_filtrados_envejecimiento_Abajo = self.df_base_totales[
            (self.df_base_totales['Grupos_año_edad']=='65 años') | (self.df_base_totales['Grupos_año_edad']=='66 años') |
            (self.df_base_totales['Grupos_año_edad']=='67 años') | (self.df_base_totales['Grupos_año_edad']=='68 años') | 
            (self.df_base_totales['Grupos_año_edad']=='69 años') | (self.df_base_totales['Grupos_año_edad']=='70 años') |
            (self.df_base_totales['Grupos_año_edad']=='71 años') | (self.df_base_totales['Grupos_año_edad']=='72 años') |
            (self.df_base_totales['Grupos_año_edad']=='73 años') | (self.df_base_totales['Grupos_año_edad']=='74 años') |
            (self.df_base_totales['Grupos_año_edad']=='75 años') | (self.df_base_totales['Grupos_año_edad']=='76 años') |
            (self.df_base_totales['Grupos_año_edad']=='77 años') | (self.df_base_totales['Grupos_año_edad']=='78 años') |
            (self.df_base_totales['Grupos_año_edad']=='79 años') | (self.df_base_totales['Grupos_año_edad']=='80 años') |
            (self.df_base_totales['Grupos_año_edad']=='81 años') | (self.df_base_totales['Grupos_año_edad']=='82 años') |
            (self.df_base_totales['Grupos_año_edad']=='83 años') | (self.df_base_totales['Grupos_año_edad']=='84 años') |
            (self.df_base_totales['Grupos_año_edad']=='85 años') | (self.df_base_totales['Grupos_año_edad']=='86 años') |
            (self.df_base_totales['Grupos_año_edad']=='87 años') | (self.df_base_totales['Grupos_año_edad']=='88 años') |
            (self.df_base_totales['Grupos_año_edad']=='89 años') | (self.df_base_totales['Grupos_año_edad']=='90 años') |
            (self.df_base_totales['Grupos_año_edad']=='91 años') | (self.df_base_totales['Grupos_año_edad']=='92 años') |
            (self.df_base_totales['Grupos_año_edad']=='93 años') | (self.df_base_totales['Grupos_año_edad']=='94 años') |
            (self.df_base_totales['Grupos_año_edad']=='95 años') | (self.df_base_totales['Grupos_año_edad']=='96 años') |
            (self.df_base_totales['Grupos_año_edad']=='97 años') | (self.df_base_totales['Grupos_año_edad']=='98 años') |
            (self.df_base_totales['Grupos_año_edad']=='99 años') | (self.df_base_totales['Grupos_año_edad']=='100 años') |            
            (self.df_base_totales['Grupos_año_edad']=='85 años y más')  | (self.df_base_totales['Grupos_año_edad']=='85 a 94 años')   |
            (self.df_base_totales['Grupos_año_edad']=='De 85 a 89 años')| (self.df_base_totales['Grupos_año_edad']=='De 85 a 94 años') |
            (self.df_base_totales['Grupos_año_edad']=='De 95 años y más') | (self.df_base_totales['Grupos_año_edad']=='De 95 a 99 años') |
            (self.df_base_totales['Grupos_año_edad']=='De 100 más años')  | (self.df_base_totales['Grupos_año_edad']=='De 90 a 94 años') |
            (self.df_base_totales['Grupos_año_edad']=='De 100 y más años') | (self.df_base_totales['Grupos_año_edad']=='De 85 años y más')
        
        ]

        self.arriba_totales = df_filtrados_envejecimiento_Abajo["Poblacion_Hombres"].sum()+df_filtrados_envejecimiento_Abajo["Poblacion_Mujeres"].sum() 
        self.abajo_totales = df_filtrados_envejecimiento_Arriba["Poblacion_Hombres"].sum()+df_filtrados_envejecimiento_Arriba["Poblacion_Mujeres"].sum() 
        self.indice_envejecimiento_totales = (self.arriba_totales/self.abajo_totales)*100
        return {
            "sum_abajo_totales": float(self.abajo_totales),
            "sum_arriba_totales": float(self.arriba_totales),
            "indice_envejecimiento": float(self.indice_envejecimiento_totales),
        }

    def indiceDependenciaTotal(self):
        df_filtrados_envejecimiento_Abajo = self.df_base_totales[
                (self.df_base_totales['Grupos_año_edad']=='15 años') | (self.df_base_totales['Grupos_año_edad']=='16 años') |
                (self.df_base_totales['Grupos_año_edad']=='17 años') | (self.df_base_totales['Grupos_año_edad']=='18 años') |
                (self.df_base_totales['Grupos_año_edad']=='19 años') | (self.df_base_totales['Grupos_año_edad']=='20 años') |
                (self.df_base_totales['Grupos_año_edad']=='21 años') | (self.df_base_totales['Grupos_año_edad']=='22 años') |
                (self.df_base_totales['Grupos_año_edad']=='23 años') | (self.df_base_totales['Grupos_año_edad']=='24 años') |
                (self.df_base_totales['Grupos_año_edad']=='25 años') | (self.df_base_totales['Grupos_año_edad']=='26 años') |
                (self.df_base_totales['Grupos_año_edad']=='27 años') | (self.df_base_totales['Grupos_año_edad']=='28 años') |
                (self.df_base_totales['Grupos_año_edad']=='29 años') | (self.df_base_totales['Grupos_año_edad']=='30 años') |
                (self.df_base_totales['Grupos_año_edad']=='31 años') | (self.df_base_totales['Grupos_año_edad']=='32 años') |
                (self.df_base_totales['Grupos_año_edad']=='33 años') | (self.df_base_totales['Grupos_año_edad']=='34 años') |
                (self.df_base_totales['Grupos_año_edad']=='35 años') | (self.df_base_totales['Grupos_año_edad']=='36 años') |
                (self.df_base_totales['Grupos_año_edad']=='37 años') | (self.df_base_totales['Grupos_año_edad']=='38 años') |
                (self.df_base_totales['Grupos_año_edad']=='39 años') | (self.df_base_totales['Grupos_año_edad']=='40 años') |
                (self.df_base_totales['Grupos_año_edad']=='41 años') | (self.df_base_totales['Grupos_año_edad']=='42 años') |
                (self.df_base_totales['Grupos_año_edad']=='43 años') | (self.df_base_totales['Grupos_año_edad']=='44 años') |
                (self.df_base_totales['Grupos_año_edad']=='45 años') | (self.df_base_totales['Grupos_año_edad']=='46 años') |
                (self.df_base_totales['Grupos_año_edad']=='47 años') | (self.df_base_totales['Grupos_año_edad']=='48 años') |
                (self.df_base_totales['Grupos_año_edad']=='49 años') | (self.df_base_totales['Grupos_año_edad']=='50 años') |
                (self.df_base_totales['Grupos_año_edad']=='51 años') | (self.df_base_totales['Grupos_año_edad']=='52 años') |
                (self.df_base_totales['Grupos_año_edad']=='53 años') | (self.df_base_totales['Grupos_año_edad']=='54 años') |
                (self.df_base_totales['Grupos_año_edad']=='55 años') | (self.df_base_totales['Grupos_año_edad']=='56 años') |
                (self.df_base_totales['Grupos_año_edad']=='57 años') | (self.df_base_totales['Grupos_año_edad']=='58 años') |
                (self.df_base_totales['Grupos_año_edad']=='59 años') | (self.df_base_totales['Grupos_año_edad']=='60 años') |
                (self.df_base_totales['Grupos_año_edad']=='61 años') | (self.df_base_totales['Grupos_año_edad']=='62 años') |
                (self.df_base_totales['Grupos_año_edad']=='63 años') | (self.df_base_totales['Grupos_año_edad']=='64 años')
                ]


        
        self.ID_suma_arriba_totales = self.abajo_totales + self.arriba_totales
        self.ID_suma_abajo_totales = df_filtrados_envejecimiento_Abajo["Poblacion_Hombres"].sum() + df_filtrados_envejecimiento_Abajo["Poblacion_Mujeres"].sum()
        self.IDependencia_totales = (self.ID_suma_arriba_totales/self.ID_suma_abajo_totales)*100
        
        return {
            "suma_arriba_totales": self.ID_suma_arriba_totales,
            "suma_abajo_totales": self.ID_suma_abajo_totales,
            "indice_dependencia": self.IDependencia_totales
        }
        
    def relacionHombreMujerDfTotal(self):
        self.df_base_totales["Relacion_Hombre_mujer"]=(self.df_base_totales["Poblacion_Hombres"]/self.df_base_totales["Poblacion_Mujeres"])*100
        self.df_base_totales["Relacion_Mujer_hombre"] =(self.df_base_totales["Poblacion_Mujeres"]/self.df_base_totales["Poblacion_Hombres"])*100
        self.df_base_totales.replace([np.inf, -np.inf], np.nan, inplace=True)
        self.df_base_totales.dropna(subset=["Relacion_Hombre_mujer", "Relacion_Mujer_hombre"], how="all", inplace=True)
        df_relacion_hombre_mujer = self.df_base_totales[
            [
                "Municipio", "Grupos_año_edad", "Poblacion_Hombres", 
                "Poblacion_Mujeres", "Relacion_Hombre_mujer", "Relacion_Mujer_hombre"
            ]
        ]
        return df_relacion_hombre_mujer
        
    def graficaPiramideTotal(self, save=False, name="default"):
        #definir límites para x and y
        y = range(0, len(self.df_base_totales))
        x_male = self.df_base_totales['Poblacion_Hombres']
        x_female = self.df_base_totales['Poblacion_Mujeres']
        
        #define los parámetros de la trama
        fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(9, 6))
        
        #especifique el color de fondo y el título de la trama
        fig.patch.set_facecolor('xkcd:light grey')
        plt.figtext(.5,.9,"Piramide de Población", fontsize=15, ha='center')
        
        x_male = self.df_base_totales['Poblacion_Hombres']
        x_female = self.df_base_totales['Poblacion_Mujeres']#definir barras masculinas y femeninas
        axes[0].barh(y, x_male, align='center', color='royalblue')
        axes[0].set(title='Hombres')
        axes[1].barh(y, x_female, align='center', color='lightpink')
        axes[1].set(title='Mujeres')
        
        # ajuste los parámetros de la cuadrícula y especifique etiquetas para el eje y
        axes[1].grid()
        #axes[0].set(yticks=y, yticklabels=self.df_base_totales['Grupos_año_edad'])
        axes[0].invert_xaxis()
        axes[0].grid()
        
        # Etiquetas
        axes[0].set_xlabel("Cantidad de Personas")
        axes[1].set_xlabel("Cantidad de Personas")
        if save:
            plt.save(name)
        #display plot 
        plt.show()
        
    def generarResumenTablasDfTotal(self, año="1900"):
        ###Crecimiento poblacional
        df_resumen = pd.DataFrame()
        df_resumen["Año"] = [año]
        df_resumen["Total Poblacion"] = [float(self.df_base_totales["Población_total"].sum())]
        df_resumen["Hombres"] = [float(self.df_base_totales["Poblacion_Hombres"].sum())]
        df_resumen["Mujeres"] = [float(self.df_base_totales["Poblacion_Mujeres"].sum())]
        df_resumen["% Crecimiento Poblacional"] = [
            float(df_resumen["Hombres"])/
            float(df_resumen["Mujeres"])*100]
        ###Indice de Envejecimiento
        df_resumen["Poblacion de 65 años y mas"] = [self.indiceEnvejecimientoTotal()["sum_arriba_totales"]]
        df_resumen["Poblacion de 0-14 años"] = [self.indiceEnvejecimientoTotal()["sum_abajo_totales"]]
        df_resumen["% de Envejecimiento"] = [self.indiceEnvejecimientoTotal()["indice_envejecimiento"]]
        ###Indice de Dependencia
        df_resumen["Poblacion Dependiente (0-14 y 15-64 "] = [self.indiceDependenciaTotal()["suma_arriba_totales"]]
        df_resumen["Poblacion en edad laboral"] = [self.indiceDependenciaTotal()["suma_abajo_totales"]]
        df_resumen["% de Dependencia"] = [self.indiceDependenciaTotal()["indice_dependencia"]]
        ###Relacion hombre Mujer  y mujer hombre
        df_resumen["Relacion_Hombre_mujer"]=(df_resumen["Hombres"]/df_resumen["Mujeres"])*100
        df_resumen["Relacion_Mujer_hombre"] =(df_resumen["Mujeres"]/df_resumen["Hombres"])*100
        df_resumen.replace([np.inf, -np.inf], np.nan, inplace=True)
        df_resumen.dropna(subset=["Relacion_Hombre_mujer", "Relacion_Mujer_hombre"], how="all", inplace=True)                
        return df_resumen

    def indiceEnvejecimientoRangos(self):
        df_filtrados_envejecimiento_Arriba = self.df_base_rango[
            (self.df_base_rango['Grupos_año_edad']=='De 0 a 4 años') | (self.df_base_rango['Grupos_año_edad']=='De 5 a 9 años') | 
            (self.df_base_rango['Grupos_año_edad']=='De 10 a 14 años')
        ]

        df_filtrados_envejecimiento_Abajo = self.df_base_rango[
            (self.df_base_rango['Grupos_año_edad']=='De 65 a 69 años') | (self.df_base_rango['Grupos_año_edad']=='De 70 a 74 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 75 a 79 años') | (self.df_base_rango['Grupos_año_edad']=='De 80 a 84 años') | 
            (self.df_base_rango['Grupos_año_edad']=='De 85 a 94 años') | (self.df_base_rango['Grupos_año_edad']=='De 95 años y más')|
            (self.df_base_rango['Grupos_año_edad']=='De 85 a 89 años') | (self.df_base_rango['Grupos_año_edad']=='De 90 a 94 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 95 a 99 años') | (self.df_base_rango['Grupos_año_edad']=='De 100 y más años')|
            (self.df_base_rango['Grupos_año_edad']=='De 85 años y más')
        ]

        self.arriba_rango = df_filtrados_envejecimiento_Abajo["Poblacion_Hombres"].sum()+df_filtrados_envejecimiento_Abajo["Poblacion_Mujeres"].sum() 
        self.abajo_rango = df_filtrados_envejecimiento_Arriba["Poblacion_Hombres"].sum()+df_filtrados_envejecimiento_Arriba["Poblacion_Mujeres"].sum() 
        self.indice_envejecimiento_rango = (self.arriba_rango/self.abajo_rango)*100
        return {
            "sum_abajo_totales": float(self.abajo_rango),
            "sum_arriba_totales": float(self.arriba_rango),
            "indice_envejecimiento": float(self.indice_envejecimiento_rango),
        }

    
    def indiceDependenciaRangos(self):
        df_filtrados_envejecimiento_Abajo = self.df_base_rango[
            (self.df_base_rango['Grupos_año_edad']=='De 15 a 19 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 20 a 24 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 25 a 29 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 30 a 34 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 35 a 39 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 40 a 44 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 45 a 49 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 50 a 54 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 55 a 59 años') |
            (self.df_base_rango['Grupos_año_edad']=='De 60 a 64 años')
        ]
        
        self.ID_suma_arriba_rango = self.abajo_rango + self.arriba_rango
        self.ID_suma_abajo_rango = df_filtrados_envejecimiento_Abajo["Poblacion_Hombres"].sum() + df_filtrados_envejecimiento_Abajo["Poblacion_Mujeres"].sum()
        self.IDependencia_rango = (self.ID_suma_arriba_rango/self.ID_suma_abajo_rango)*100
        
        return {
            "suma_arriba_totales": self.ID_suma_arriba_rango,
            "suma_abajo_totales": self.ID_suma_abajo_rango,
            "indice_dependencia": self.IDependencia_rango
        }
        
    def relacionHombreMujerDfRangos(self):
        self.df_base_rango["Relacion_Hombre_mujer"]=(self.df_base_rango["Poblacion_Hombres"]/self.df_base_rango["Poblacion_Mujeres"])*100
        self.df_base_rango["Relacion_Mujer_hombre"] =(self.df_base_rango["Poblacion_Mujeres"]/self.df_base_rango["Poblacion_Hombres"])*100
        self.df_base_rango.replace([np.inf, -np.inf], np.nan, inplace=True)
        self.df_base_rango.dropna(subset=["Relacion_Hombre_mujer", "Relacion_Mujer_hombre"], how="all", inplace=True)
        df_relacion_hombre_mujer = self.df_base_rango[
            [
                "Municipio", "Grupos_año_edad", "Poblacion_Hombres", 
                "Poblacion_Mujeres", "Relacion_Hombre_mujer", "Relacion_Mujer_hombre"
            ]
        ]
        return df_relacion_hombre_mujer
        
    def graficaPiramideRangos(self, save=False, name="default"):
        #definir límites para x and y
        y = range(0, len(self.df_base_rango))
        x_male = self.df_base_rango['Poblacion_Hombres']
        x_female = self.df_base_rango['Poblacion_Mujeres']
        
        #define los parámetros de la trama
        fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(9, 6))
        
        #especifique el color de fondo y el título de la trama
        fig.patch.set_facecolor('xkcd:light grey')
        plt.figtext(.5,.9,"Piramide de Población", fontsize=15, ha='center')
        
        x_male = self.df_base_rango['Poblacion_Hombres']
        x_female = self.df_base_rango['Poblacion_Mujeres']#definir barras masculinas y femeninas
        axes[0].barh(y, x_male, align='center', color='royalblue')
        axes[0].set(title='Hombres')
        axes[1].barh(y, x_female, align='center', color='lightpink')
        axes[1].set(title='Mujeres')
        
        # ajuste los parámetros de la cuadrícula y especifique etiquetas para el eje y
        axes[1].grid()
        axes[0].set(yticks=y, yticklabels=self.df_base_rango['Grupos_año_edad'])
        axes[0].invert_xaxis()
        axes[0].grid()
        
        # Etiquetas
        axes[0].set_xlabel("Cantidad de Personas")
        axes[1].set_xlabel("Cantidad de Personas")
        if save:
            plt.save(name)
        #display plot 
        plt.show()
        
    def generarResumenTablasDfRangos(self, año="1900"):
        ###Crecimiento poblacional
        df_resumen = pd.DataFrame()
        df_resumen["Año"] = [año]
        df_resumen["Total Poblacion"] = [float(self.df_base_rango["Población_total"].sum())]
        df_resumen["Hombres"] = [float(self.df_base_rango["Poblacion_Hombres"].sum())]
        df_resumen["Mujeres"] = [float(self.df_base_rango["Poblacion_Mujeres"].sum())]
        df_resumen["% Crecimiento Poblacional"] = [
            float(df_resumen["Hombres"])/
            float(df_resumen["Mujeres"])*100]
        ###Indice de Envejecimiento
        df_resumen["Poblacion de 65 años y mas"] = [self.indiceEnvejecimientoRangos()["sum_arriba_totales"]]
        df_resumen["Poblacion de 0-14 años"] = [self.indiceEnvejecimientoRangos()["sum_abajo_totales"]]
        df_resumen["% de Envejecimiento"] = [self.indiceEnvejecimientoRangos()["indice_envejecimiento"]]
        ###Indice de Dependencia
        df_resumen["Poblacion Dependiente (0-14 y 15-64 "] = [self.indiceDependenciaRangos()["suma_arriba_totales"]]
        df_resumen["Poblacion en edad laboral"] = [self.indiceDependenciaRangos()["suma_abajo_totales"]]
        df_resumen["% de Dependencia"] = [self.indiceDependenciaRangos()["indice_dependencia"]]
        ###Relacion hombre Mujer  y mujer hombre
        df_resumen["Relacion_Hombre_mujer"]=(df_resumen["Hombres"]/df_resumen["Mujeres"])*100
        df_resumen["Relacion_Mujer_hombre"] =(df_resumen["Mujeres"]/df_resumen["Hombres"])*100
        df_resumen.replace([np.inf, -np.inf], np.nan, inplace=True)
        df_resumen.dropna(subset=["Relacion_Hombre_mujer", "Relacion_Mujer_hombre"], how="all", inplace=True)        
        return df_resumen