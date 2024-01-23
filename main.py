from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntry
import tkinter as tk
from db_functions import get_names_champs

enemy_team = {}
champ_names = get_names_champs()


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.toplane_label = tk.Label(self, text="Вражеский топлейн")
        self.toplane = AutocompleteEntry(self, completevalues=champ_names)
        self.jungle_label = tk.Label(self, text="Вражеский лесник")
        self.jungle = AutocompleteEntry(self, completevalues=champ_names)
        self.midlane_label = tk.Label(self, text="Вражеский мидер")
        self.midlane = AutocompleteEntry(self, completevalues=champ_names)
        self.adc_label = tk.Label(self, text="Вражеский адк")
        self.adc = AutocompleteEntry(self, completevalues=champ_names)
        self.support_label = tk.Label(self, text="Вражеский саппорт")
        self.support = AutocompleteEntry(self, completevalues=champ_names)

        self.btn_save = tk.Button(self, text="Сохранить", command=self.save)
        self.btn_clear = tk.Button(self, text="Очистить", command=self.clear)
        self.toplane_label.grid(row=0, column=0, sticky='w')
        self.toplane.grid(row=0, column=1, sticky='w')
        self.jungle_label.grid(row=1, column=0, sticky='w')
        self.jungle.grid(row=1, column=1, sticky='w')
        self.midlane_label.grid(row=2, column=0, sticky='w')
        self.midlane.grid(row=2, column=1, sticky='w')
        self.adc_label.grid(row=3, column=0, sticky='w')
        self.adc.grid(row=3, column=1, sticky='w')
        self.support_label.grid(row=4, column=0, sticky='w')
        self.support.grid(row=4, column=1, sticky='w')
        self.btn_save.grid(row=5, column=0, sticky='w')
        self.btn_clear.grid(row=5, column=1, sticky='w')

    def save(self) -> None:
        enemy_team['toplane'] = self.toplane.get()
        enemy_team['midlane'] = self.midlane.get()
        enemy_team['jungle'] = self.jungle.get()
        enemy_team['adc'] = self.adc.get()
        enemy_team['support'] = self.support.get()
        print(enemy_team)

    def clear(self):
        self.toplane.delete(0, END)
        self.midlane.delete(0, END)
        self.jungle.delete(0, END)
        self.adc.delete(0, END)
        self.support.delete(0, END)


app = SampleApp()
app.title('LoL_ADC_helper')
app.geometry("400x250")
app.mainloop()