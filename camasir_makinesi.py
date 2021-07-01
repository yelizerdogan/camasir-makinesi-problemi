import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as karar  

giris1 = karar.Antecedent(np.arange(0, 12, 1),'camasir_miktari')
giris2 = karar.Antecedent(np.arange(0, 101, 1),'kirlilik')
giris3 = karar.Antecedent(np.arange(0,231,1), 'camasir_cinsi')
cikis = karar.Consequent(np.arange(0, 101, 1),'deterjan_miktari')

giris1['az'] = fuzzy.trimf(giris1.universe, [0, 3, 5])
giris1['orta'] = fuzzy.trimf(giris1.universe, [4, 6, 8])
giris1['cok'] = fuzzy.trimf(giris1.universe, [7, 9, 11])


giris2['az_kirli'] = fuzzy.trimf(giris2.universe, [0, 25, 50])
giris2['orta_kirli'] = fuzzy.trimf(giris2.universe, [40, 65, 80])
giris2['cok_kirli'] = fuzzy.trimf(giris2.universe, [70, 90, 100])

giris3['hassas'] = fuzzy.trimf(giris3.universe, [0, 50, 100])
giris3['karma'] = fuzzy.trimf(giris3.universe, [90, 140, 190])
giris3['guclu'] = fuzzy.trimf(giris3.universe, [180, 230, 230])

cikis['cok_az'] = fuzzy.trimf(cikis.universe, [0, 20, 40])
cikis['az'] = fuzzy.trimf(cikis.universe, [30, 45, 60])
cikis['normal'] = fuzzy.trimf(cikis.universe, [50, 65, 80])
cikis['fazla'] = fuzzy.trimf(cikis.universe, [70, 80, 90])
cikis['cok_fazla'] = fuzzy.trimf(cikis.universe, [80, 95, 100])

giris1.view()
giris2.view()
giris3.view()
cikis.view()


kural1 = karar.Rule(giris1['az'] & giris2['az_kirli'] & giris3['hassas'], cikis['cok_az'])
kural2 = karar.Rule(giris1['az'] & giris2['az_kirli'] & giris3['karma'], cikis['cok_az'])
kural3 = karar.Rule(giris1['az'] & giris2['az_kirli'] & giris3['guclu'], cikis['az'])

kural4 = karar.Rule(giris1['az'] & giris2['orta_kirli'] & giris3['hassas'], cikis['cok_az'])
kural5 = karar.Rule(giris1['az'] & giris2['orta_kirli'] & giris3['karma'], cikis['az'])
kural6 = karar.Rule(giris1['az'] & giris2['orta_kirli'] & giris3['guclu'], cikis['az'])

kural7 = karar.Rule(giris1['az'] & giris2['cok_kirli'] & giris3['hassas'], cikis['az'])
kural8 = karar.Rule(giris1['az'] & giris2['cok_kirli'] & giris3['karma'], cikis['normal'])
kural9 = karar.Rule(giris1['az'] & giris2['cok_kirli'] & giris3['guclu'], cikis['normal'])

kural10 = karar.Rule(giris1['orta'] & giris2['az_kirli'] & giris3['hassas'], cikis['cok_az'])
kural11 = karar.Rule(giris1['orta'] & giris2['az_kirli'] & giris3['karma'], cikis['az'])
kural12 = karar.Rule(giris1['orta'] & giris2['az_kirli'] & giris3['guclu'], cikis['normal'])

kural13 = karar.Rule(giris1['orta'] & giris2['orta_kirli'] & giris3['hassas'], cikis['az'])
kural14 = karar.Rule(giris1['orta'] & giris2['orta_kirli'] & giris3['karma'], cikis['normal'])
kural15 = karar.Rule(giris1['orta'] & giris2['orta_kirli'] & giris3['guclu'], cikis['normal'])

kural16 = karar.Rule(giris1['orta'] & giris2['cok_kirli'] & giris3['hassas'], cikis['normal'])
kural17 = karar.Rule(giris1['orta'] & giris2['cok_kirli'] & giris3['karma'], cikis['fazla'])
kural18 = karar.Rule(giris1['orta'] & giris2['cok_kirli'] & giris3['guclu'], cikis['cok_fazla'])

kural19 = karar.Rule(giris1['cok'] & giris2['az_kirli'] & giris3['hassas'], cikis['normal'])
kural20 = karar.Rule(giris1['cok'] & giris2['az_kirli'] & giris3['karma'], cikis['normal'])
kural21 = karar.Rule(giris1['cok'] & giris2['az_kirli'] & giris3['guclu'], cikis['normal'])

kural22 = karar.Rule(giris1['cok'] & giris2['orta_kirli'] & giris3['hassas'], cikis['normal'])
kural23 = karar.Rule(giris1['cok'] & giris2['orta_kirli'] & giris3['karma'], cikis['fazla'])
kural24 = karar.Rule(giris1['cok'] & giris2['orta_kirli'] & giris3['guclu'], cikis['fazla'])

kural25 = karar.Rule(giris1['cok'] & giris2['cok_kirli'] & giris3['hassas'], cikis['fazla'])
kural26 = karar.Rule(giris1['cok'] & giris2['cok_kirli'] & giris3['karma'], cikis['cok_fazla'])
kural27 = karar.Rule(giris1['cok'] & giris2['cok_kirli'] & giris3['guclu'], cikis['cok_fazla'])

funding_karar = karar.ControlSystem([kural1, kural2, kural3, kural4, kural5, kural6, kural7,kural8,kural9,kural10,kural11,kural12,kural13,kural14,kural15,kural16,kural17,kural18,kural19,kural20,kural21,kural22,kural23,kural24,kural25,kural26,kural27])

funding_ = karar.ControlSystemSimulation(funding_karar)

# Giriş değerleri...
funding_.input['camasir_miktari'] = 7
funding_.input['kirlilik'] = 70
funding_.input['camasir_cinsi'] = 85
# Hesap
funding_.compute()
print(funding_.output['deterjan_miktari'])
cikis.view(sim=funding_)