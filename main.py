import tkinter as tk


r = tk.Tk()

r.title('Counting Seconds')

T = tk.Text(r, height = 5, width = 52)

T.pack()

sum_result_1 = tk.StringVar()

l = tk.Label(r, text = "Fact of the Day", textvariable=sum_result_1)

l.pack()

def calculate():
    print(T.get("1.0","end-1c"))

    sum_result_1.set(T.get("1.0","end-1c"))

button = tk.Button(r, text='Вычислить', width=25, command=calculate)

button.pack()

r.mainloop()
