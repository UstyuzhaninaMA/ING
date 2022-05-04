import matplotlib.pyplot as plt
import numpy as np

def read_settings(f_name): 
    with open(f_name, 'r') as settings_f:
        return [float(i) for i in settings_f.read().split('\n')]
    
period, qStep = read_settings("settings.txt")

data_ar = np.loadtxt("data.txt", dtype = float) 
data_ar = data_ar * qStep # приводим к нужной величине
exp_time= len(data_ar) * period 

t = np.arange(0, exp_time, period) # создаем массив данных времени с нужным шагом
charge_time = np.argmax(data_ar) * period
discharge_time = exp_time - charge_time 


fig, ax = plt.subplots(figsize = (15, 10), dpi = 100) # создаем пространство для графика
ax.plot(t, data_ar, marker = "o", markersize = 5, markevery = 100, markerfacecolor = "black", label = 'V(t)', color = 'green') # устанавливаем основные параметры графика

ax.set_title('Зависимость напряжения на конденсаторе от времени по мере его зарядки и разрядки', fontsize = 17, wrap = True)
ax.set_xlabel('Время, с') 
ax.set_ylabel('Напряжение, В')
ax.set_xlim(0, 60)
ax.set_ylim(0, 3)

ax.text(50, 2.15, 'Время зарядки:   {:.2f} c'.format(charge_time), bbox = dict(facecolor = 'blue', alpha = 0.3)) # добавляем данные о времени зарядки и разрядки конденсатора, указываем им позицию и их размер, цвет
ax.text(50, 2, 'Время разрядки: {:.2f} c'.format(discharge_time), bbox = dict(facecolor = 'blue', alpha = 0.3))

ax.minorticks_on() # включаем метки
ax.grid(which = 'major', linewidth = 2) 
ax.grid(which = 'minor', linestyle = ':')

ax.legend()

fig.savefig('graph.svg')
plt.show()