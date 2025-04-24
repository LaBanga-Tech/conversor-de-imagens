from customtkinter import (
    CTk,
    CTkButton,
    CTkLabel,
    CTkFrame,
    StringVar,
    CTkOptionMenu,
)
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

types = ["png", "bmp", "webp", "tiff", "tif", "ico", "jpg", "jpeg"]

win = CTk("#111111")
win.title("Conversor de imagens")
width = 800
height = 600
pad_left = (win.winfo_screenwidth() - width) // 2
pad_top = (win.winfo_screenheight() - height) // 2
win.geometry(f"{width}x{height}+{pad_left}+{pad_top}")
win.iconbitmap("./imagens/conversor.ico")
win.resizable(False, False)


def Choose_File():
    file = filedialog.askopenfilename()
    extension = file.split(".")[-1]

    if extension in types:
        filename.set(file)
        return
    else:
        messagebox.showerror("Aviso", "Este arquivo não é suportado!")


def Choose_Dir():
    dir = filedialog.askdirectory()
    dirname.set(dir)


def Convert():
    if filename.get() != "" and dirname.get() != "":
        original_name = filename.get().split("/")[-1].split(".")[0]
        new_name = f"{dirname.get()}/{original_name}.{ext.get()}"
        new_extension = ext.get()
        try:
            Image.open(filename.get()).save(fp=new_name, format=new_extension)
            messagebox.showinfo("Sucesso", "Imagem convertida com sucesso!")
        except:
            messagebox.showwarning("Aviso", "Não foi possível concluir saldo!")


# POSTER
image_tk = ImageTk.PhotoImage(Image.open("./imagens/conversor.png").resize((600, 300)))

CTkLabel(win, image=image_tk, text=None).pack()

# ! PRIMEIRO FRAME
frame1 = CTkFrame(win, fg_color="#252525", corner_radius=1)
frame1.pack(pady=(10, 0))

# ? LABEL - ARQUIVO SELECIONADO
filename = StringVar(value="")
CTkLabel(frame1, width=600, anchor="w", textvariable=filename).grid(
    column=0, row=0, padx=(10, 0)
)

# ? BOTÃO - SELECIONA IMAGEM PARA CONVERÇÃO
selector_file_button = CTkButton(
    frame1, text="Selecionar Imagem", corner_radius=1, command=Choose_File
)
selector_file_button.grid(column=1, row=0, pady=20, padx=(0, 10))

# ? LABEL - DIRETÓRIO DESTINO
dirname = StringVar(value="")
CTkLabel(frame1, text="/image", width=600, anchor="w", textvariable=dirname).grid(
    column=0, row=1, padx=(10, 0)
)

# ? BOTÃO - SELECIONA DIRETÓRIO DESTINO
selector_dir_button = CTkButton(
    frame1, text="Selecionar Pasta", corner_radius=1, command=Choose_Dir
)
selector_dir_button.grid(column=1, row=1, pady=20, padx=(0, 10))

# ** SEGUNDO FRAME
frame2 = CTkFrame(win, fg_color="#252525", corner_radius=1)
frame2.pack(pady=40)

# ! COMBO - SELECIONA A EXTENSÃO DESEJADA
ext = StringVar(value="png")


def Get_Extension(ev):
    ext.set(ev)
    return


CTkOptionMenu(
    frame2,
    values=types,
    command=Get_Extension,
).grid(column=0, row=0, padx=(10, 460), pady=20)

# ! BOTÃO - CONVERTE  PARA O FORMATO DESAJADO
bt_convert = CTkButton(frame2, text="Converter", corner_radius=1, command=Convert)
bt_convert.grid(column=1, row=0, padx=(0, 10))

win.mainloop()
