import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore

root = ttk.Window()

b1 = ttk.Button(root, text="Solid Button", bootstyle=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Outline Button", bootstyle=(SUCCESS, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
