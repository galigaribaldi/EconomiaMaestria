import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Quinquenales:
    df_base_totales_quinquenales = []
    abajo_quinquenale = 0
    arriba_quinquenales = 0
    indice_envejecimiento_quinquenales = 0
    ID_suma_arriba_quinquenales = 0
    ID_suma_abajo_quinquenales = 0
    IDependencia = 0
    
    def __init__(self, df_base_totales_quinquenales):
        self.df_base_totales_quinquenales = df_base_totales_quinquenales
    def indiceEnvejecimiento(self):
        df_filtrados_envejecimiento_Abajo = self.df_base_totales_quinquenales[
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 0 a 4 años') | 
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 5 a 9 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 10 a 14 años')
        ]
        df_filtrados_envejecimiento_Arriba = self.df_base_totales_quinquenales[
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 65 a 69 años') | 
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 70 a 74 años') | 
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 75 a 79 años') | 
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 80 a 84 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 85 a 94 años') | 
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 95 años y más') 
        ]
        self.abajo_quinquenales = df_filtrados_envejecimiento_Abajo["Poblacion_Hombres"].sum()+df_filtrados_envejecimiento_Abajo["Poblacion_Mujeres"].sum() 
        self.arriba_quinquenales = df_filtrados_envejecimiento_Arriba["Poblacion_Hombres"].sum()+df_filtrados_envejecimiento_Arriba["Poblacion_Mujeres"].sum() 
        self.indice_envejecimiento_quinquenales = (self.arriba_quinquenales/self.abajo_quinquenales)*100
        return {
            "sum_abajo_quinquenales": float(self.abajo_quinquenales),
            "sum_arriba_quinquenales": float(self.arriba_quinquenales),
            "indice_envejecimiento": float(self.indice_envejecimiento_quinquenales),
        }

    def indiceDependencia(self):
        df_filtrados_envejecimiento_Abajo = self.df_base_totales_quinquenales[
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 15 a 19 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 20 a 24 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 25 a 29 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 30 a 34 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 35 a 39 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 40 a 44 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 45 a 49 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 50 a 54 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 55 a 59 años') |
            (self.df_base_totales_quinquenales['Grupos_año_edad']=='De 60 a 64 años')
        ]
        self.ID_suma_arriba_quinquenales = self.abajo_quinquenales + self.arriba_quinquenales
        self.ID_suma_abajo_quinquenales = df_filtrados_envejecimiento_Abajo["Poblacion_Hombres"].sum() + df_filtrados_envejecimiento_Abajo["Poblacion_Mujeres"].sum()
        self.IDependencia = (self.ID_suma_arriba_quinquenales/self.ID_suma_abajo_quinquenales)*100
        
        return {
            "suma_arriba_quinquenales": self.ID_suma_arriba_quinquenales,
            "suma_abajo_quinquenales": self.ID_suma_abajo_quinquenales,
            "indice_dependencia": self.IDependencia
        }
        
    def relacionHombreMujerDf(self):
        self.df_base_totales_quinquenales["Relacion_Hombre_mujer"]=(self.df_base_totales_quinquenales["Poblacion_Hombres"]/self.df_base_totales_quinquenales["Poblacion_Mujeres"])*100
        self.df_base_totales_quinquenales["Relacion_Mujer_hombre"] =(self.df_base_totales_quinquenales["Poblacion_Mujeres"]/self.df_base_totales_quinquenales["Poblacion_Hombres"])*100
        self.df_base_totales_quinquenales.replace([np.inf, -np.inf], np.nan, inplace=True)
        self.df_base_totales_quinquenales.dropna(subset=["Relacion_Hombre_mujer", "Relacion_Mujer_hombre"], how="all", inplace=True)
        df_relacion_hombre_mujer = self.df_base_totales_quinquenales[
            [
                "Municipio", "Grupos_año_edad", "Poblacion_Hombres", 
                "Poblacion_Mujeres", "Relacion_Hombre_mujer", "Relacion_Mujer_hombre"
            ]
        ]
        return df_relacion_hombre_mujer
        
    def graficaPiramide(self, save=False, name="default"):
        #definir límites para x and y
        y = range(0, len(self.df_base_totales_quinquenales))
        x_male = self.df_base_totales_quinquenales['Poblacion_Hombres']
        x_female = self.df_base_totales_quinquenales['Poblacion_Mujeres']
        
        #define los parámetros de la trama
        fig, axes = plt.subplots(ncols=2, sharey=True, figsize=(9, 6))
        
        #especifique el color de fondo y el título de la trama
        fig.patch.set_facecolor('xkcd:light grey')
        plt.figtext(.5,.9,"Piramide de Población", fontsize=15, ha='center')
        
        x_male = self.df_base_totales_quinquenales['Poblacion_Hombres']
        x_female = self.df_base_totales_quinquenales['Poblacion_Mujeres']#definir barras masculinas y femeninas
        axes[0].barh(y, x_male, align='center', color='royalblue')
        axes[0].set(title='Hombres')
        axes[1].barh(y, x_female, align='center', color='lightpink')
        axes[1].set(title='Mujeres')
        
        # ajuste los parámetros de la cuadrícula y especifique etiquetas para el eje y
        axes[1].grid()
        axes[0].set(yticks=y, yticklabels=self.df_base_totales_quinquenales['Grupos_año_edad'])
        axes[0].invert_xaxis()
        axes[0].grid()
        
        # Etiquetas
        axes[0].set_xlabel("Cantidad de Personas")
        axes[1].set_xlabel("Cantidad de Personas")
        if save:
            plt.save(name)
        #display plot 
        plt.show()
        
    def generarResumenTablasDf(self, año="1900"):
        ###Crecimiento poblacional
        df_resumen = pd.DataFrame()
        df_resumen["Año"] = [año]
        df_resumen["Total Poblacion"] = [float(self.df_base_totales_quinquenales["Población_total"].sum())]
        df_resumen["Hombres"] = [float(self.df_base_totales_quinquenales["Poblacion_Hombres"].sum())]
        df_resumen["Mujeres"] = [float(self.df_base_totales_quinquenales["Poblacion_Mujeres"].sum())]
        df_resumen["% Crecimiento Poblacional"] = [
            float(df_resumen["Hombres"])/
            float(df_resumen["Mujeres"])*100]
        ###Indice de Envejecimiento
        df_resumen["Poblacion de 65 años y mas"] = [self.indiceEnvejecimiento()["sum_arriba_quinquenales"]]
        df_resumen["Poblacion de 0-14 años"] = [self.indiceEnvejecimiento()["sum_abajo_quinquenales"]]
        df_resumen["% de Envejecimiento"] = [self.indiceEnvejecimiento()["indice_envejecimiento"]]
        ###Indice de Dependencia
        df_resumen["Poblacion Dependiente (0-14 y 15-64 "] = [self.indiceDependencia()["suma_arriba_quinquenales"]]
        df_resumen["Poblacion en edad laboral"] = [self.indiceDependencia()["suma_abajo_quinquenales"]]
        df_resumen["% de Dependencia"] = [self.indiceDependencia()["indice_dependencia"]]
        return df_resumen
    