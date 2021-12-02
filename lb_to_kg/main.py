import tkinter


class UnitConverter:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('Pounds to Kilograms Converter')
        self.window.config(padx=20, pady=20)
        self.pounds_input = tkinter.Entry(width=7)
        self.pounds_input.grid(column=1, row=0)

        self.pounds_label = tkinter.Label(text='lbs')
        self.pounds_label.grid(column=2, row=0)

        self.is_equal_label = tkinter.Label(text='is equal to')
        self.is_equal_label.grid(column=0, row=1)

        self.kilograms_result_label = tkinter.Label(text='0')
        self.kilograms_result_label.grid(column=1, row=1)

        self.kilograms_label = tkinter.Label(text='kg')
        self.kilograms_label.grid(column=2, row=1)

        self.calculate_button = tkinter.Button(text='Calculate', command=self.lbs_to_kg)
        self.calculate_button.grid(column=1, row=2)

    def lbs_to_kg(self):
        lbs = float(self.pounds_input.get())
        kg = lbs / 2.205
        self.kilograms_result_label.config(text=f'{kg:.2f}')


unit_converter = UnitConverter()
unit_converter.window.mainloop()
