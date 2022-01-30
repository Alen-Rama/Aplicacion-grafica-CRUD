from tkinter import *
from tkinter import messagebox
import sqlite3


root =Tk()
root.title("DB Interface")
root.iconbitmap("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\logoDB-removebg-preview.ico")


nombrePantalla = StringVar()
passwordPantalla = StringVar()
apellidoPantalla = StringVar()
direccionPantalla = StringVar()
idPantalla = StringVar()


#? FUNCIONES MENU---------------------------------------------------------------------------------------------------


def salirAplicacion():
    #? SALIR DE LA APLICACIÓN
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor == "yes":
        root.destroy()


def conectarDB():
    #? CREAR LA BASE DE DATOS
    try:
        Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
        Cursor = Conexion.cursor()
        Cursor.execute('''
        CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100)
        )
        ''')
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")
    else:
        Conexion.commit()
        Conexion.close()
        messagebox.showinfo("BBDD", "BBDD creada con éxito")


def borrarCampos():
    #? BORRA LO QUE HAY ESCRITO EN LOS TODOS LOS CAMPOS 
    cuadroNombre.delete(0, "end")
    cuadroPassword.delete(0, "end")
    cuadroApellido.delete(0, "end")
    cuadroDireccion.delete(0, "end")
    cuadroComentario.delete("1.0", "end")
    cuadroId.delete(0, "end")


def crearRegistroMenu():
    #? CREA UN NUEVO REGISTRO DESDE EL MENU
    Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
    Cursor = Conexion.cursor()
    try:
        Cursor.execute(f"INSERT INTO DATOSUSUARIOS VALUES (NULL, '{nombrePantalla.get()}', '{passwordPantalla.get()}', '{apellidoPantalla.get()}', '{direccionPantalla.get()}', '{cuadroComentario.get('1.0', 'end-1c')}')")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "No se ha conectado con la BBDD")
    else:
        Conexion.commit()
        Conexion.close()
        messagebox.showinfo("BBDD", "Registro insertado con éxito")
    cuadroNombre.delete(0, "end")
    cuadroPassword.delete(0, "end")
    cuadroApellido.delete(0, "end")
    cuadroDireccion.delete(0, "end")
    cuadroComentario.delete("1.0", "end")
    cuadroId.delete(0, "end")


def leerRegistroMenu(id):
    cuadroComentario.delete("1.0", "end")
    Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
    Cursor = Conexion.cursor()
    try:
        Cursor.execute(f"SELECT * FROM DATOSUSUARIOS WHERE ID={id}")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "No se ha conectado con la BBDD")
    else:
        leerUsuario = Cursor.fetchall()
        for datos in leerUsuario:
            nombrePantalla.set(datos[1])
            passwordPantalla.set(datos[2])
            apellidoPantalla.set(datos[3])
            direccionPantalla.set(datos[4])
            cuadroComentario.insert("1.0", datos[5])
        Conexion.commit()
        Conexion.close()


def actualizarRegistroMenu(id):
    Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
    Cursor = Conexion.cursor()
    try:
        Cursor.execute(f"UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='{nombrePantalla.get()}', PASSWORD='{passwordPantalla.get()}', APELLIDO='{apellidoPantalla.get()}', DIRECCION='{direccionPantalla.get()}', COMENTARIOS='{cuadroComentario.get('1.0', 'end-1c')}' WHERE ID={id}")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "No se ha conectado con la BBDD")
    else:
        Conexion.commit()
        Conexion.close()
        messagebox.showinfo("BBDD", "Registro actualizado con éxito")
    cuadroNombre.delete(0, "end")
    cuadroPassword.delete(0, "end")
    cuadroApellido.delete(0, "end")
    cuadroDireccion.delete(0, "end")
    cuadroComentario.delete("1.0", "end")
    cuadroId.delete(0, "end")


def eliminarRegistroMenu(id):
    Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
    Cursor = Conexion.cursor()
    try:
        Cursor.execute(f"DELETE FROM DATOSUSUARIOS WHERE ID={id}")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "No se ha conectado con la BBDD")
    else:
        valor = messagebox.askquestion("¡Eliminar!", "¿Estas seguro de eliminar el registro?")
        if valor == "yes":
            Conexion.commit()
            Conexion.close()
            messagebox.showinfo("BBDD", "Registro eliminado con éxito")
    cuadroNombre.delete(0, "end")
    cuadroPassword.delete(0, "end")
    cuadroApellido.delete(0, "end")
    cuadroDireccion.delete(0, "end")
    cuadroComentario.delete("1.0", "end")
    cuadroId.delete(0, "end")


def licencia():
    #? LICENCIA
    messagebox.showinfo("DB Interface", "Proyecto basico de Python")


def acercaDe():
    #? ACERCA DE...
    messagebox.showinfo("DB Interface", "Version 1.0")


def desenfocar():
    #? QUITA EL FOCO DE UN WIDGET
    print(root.focus())


#? FUNCIONES BOTONES------------------------------------------------------------------------------------------------


def crearRegistro():
    #? CREA UN NUEVO REGISTRO
    Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
    Cursor = Conexion.cursor()
    try:
        Cursor.execute(f"INSERT INTO DATOSUSUARIOS VALUES (NULL, '{nombrePantalla.get()}', '{passwordPantalla.get()}', '{apellidoPantalla.get()}', '{direccionPantalla.get()}', '{cuadroComentario.get('1.0', 'end-1c')}')")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "No se ha conectado con la BBDD")
    else:
        Conexion.commit()
        Conexion.close()
        messagebox.showinfo("BBDD", "Registro insertado con éxito")
    cuadroNombre.delete(0, "end")
    cuadroPassword.delete(0, "end")
    cuadroApellido.delete(0, "end")
    cuadroDireccion.delete(0, "end")
    cuadroComentario.delete("1.0", "end")
    cuadroId.delete(0, "end")


def leerRegistro(id):
    cuadroComentario.delete("1.0", "end")
    Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
    Cursor = Conexion.cursor()
    try:
        Cursor.execute(f"SELECT * FROM DATOSUSUARIOS WHERE ID={id}")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "No se ha conectado con la BBDD")
    else:
        leerUsuario = Cursor.fetchall()
        for datos in leerUsuario:
            nombrePantalla.set(datos[1])
            passwordPantalla.set(datos[2])
            apellidoPantalla.set(datos[3])
            direccionPantalla.set(datos[4])
            cuadroComentario.insert("1.0", datos[5])
        Conexion.commit()
        Conexion.close()


def actualizarRegistro(id):
    Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
    Cursor = Conexion.cursor()
    try:
        Cursor.execute(f"UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='{nombrePantalla.get()}', PASSWORD='{passwordPantalla.get()}', APELLIDO='{apellidoPantalla.get()}', DIRECCION='{direccionPantalla.get()}', COMENTARIOS='{cuadroComentario.get('1.0', 'end-1c')}' WHERE ID={id}")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "No se ha conectado con la BBDD")
    else:
        Conexion.commit()
        Conexion.close()
        messagebox.showinfo("BBDD", "Registro actualizado con éxito")
    cuadroNombre.delete(0, "end")
    cuadroPassword.delete(0, "end")
    cuadroApellido.delete(0, "end")
    cuadroDireccion.delete(0, "end")
    cuadroComentario.delete("1.0", "end")
    cuadroId.delete(0, "end")


def eliminarRegistro(id):
    Conexion = sqlite3.connect("C:\\Users\\alenr\\OneDrive\\Escritorio\\Python\\DBInterface\\Usuarios")
    Cursor = Conexion.cursor()
    try:
        Cursor.execute(f"DELETE FROM DATOSUSUARIOS WHERE ID={id}")
    except sqlite3.OperationalError:
        messagebox.showwarning("¡Atención!", "No se ha conectado con la BBDD")
    else:
        valor = messagebox.askquestion("¡Eliminar!", "¿Estas seguro de eliminar el registro?")
        if valor == "yes":
            Conexion.commit()
            Conexion.close()
            messagebox.showinfo("BBDD", "Registro eliminado con éxito")
    cuadroNombre.delete(0, "end")
    cuadroPassword.delete(0, "end")
    cuadroApellido.delete(0, "end")
    cuadroDireccion.delete(0, "end")
    cuadroComentario.delete("1.0", "end")
    cuadroId.delete(0, "end")


#? CREACIÓN DE LA BARRA DE MENU-------------------------------------------------------------------------------------


barraMenu = Menu(root)
root.config(menu=barraMenu)


BBDDMenu = Menu(barraMenu, tearoff=0)
BBDDMenu.add_command(label="Conectar", command=conectarDB)
BBDDMenu.add_command(label="Salir", command=salirAplicacion)


borrar = Menu(barraMenu, tearoff=0)
borrar.add_command(label="Borrar campos", command=borrarCampos)


crud = Menu(barraMenu, tearoff=0)
crud.add_command(label="Crear", command=crearRegistroMenu)
crud.add_command(label="Leer", command=lambda:leerRegistroMenu(idPantalla.get()))
crud.add_command(label="Actualizar", command=lambda:actualizarRegistroMenu(idPantalla.get()))
crud.add_command(label="Borrar", command=lambda:eliminarRegistroMenu(idPantalla.get()))


ayuda = Menu(barraMenu, tearoff=0)
ayuda.add_command(label="Licencia", command=licencia)
ayuda.add_command(label="Acerca de...", command=acercaDe)


barraMenu.add_cascade(label="BBDD", menu=BBDDMenu)
barraMenu.add_cascade(label="Borrar", menu=borrar)
barraMenu.add_cascade(label="CRUD", menu=crud)
barraMenu.add_cascade(label="Ayuda", menu=ayuda)


#? CREACIÓN DEL FRAME-----------------------------------------------------------------------------------------------


frame = Frame(root)
frame.pack()


frame2 = Frame(frame)
frame2.config(width=270, height=1, bg="black")
frame2.grid(row=6, column=0, columnspan=6, padx=10, pady=10)


#? NOMBRE-----------------------------------------------------------------------------------------------------------


nombreLabel = Label(frame, text="Nombre:")
nombreLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


cuadroNombre = Entry(frame, textvariable=nombrePantalla)
cuadroNombre.grid(row=0, column=2, columnspan=3, padx=10, pady=10)


#? PASSWORD---------------------------------------------------------------------------------------------------------


passwordLabel = Label(frame, text="Password:")
passwordLabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


cuadroPassword = Entry(frame, textvariable=passwordPantalla)
cuadroPassword.grid(row=1, column=2, columnspan=3, padx=10, pady=10)
cuadroPassword.config(show="*")


#? APELLIDO---------------------------------------------------------------------------------------------------------


apellidoLabel = Label(frame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


cuadroApellido = Entry(frame, textvariable=apellidoPantalla)
cuadroApellido.grid(row=2, column=2, columnspan=3, padx=10, pady=10)


#? DIRECCIÓN--------------------------------------------------------------------------------------------------------


direccionLabel = Label(frame, text="Dirección:")
direccionLabel.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


cuadroDireccion = Entry(frame, textvariable=direccionPantalla)
cuadroDireccion.grid(row=3, column=2, columnspan=3, padx=10, pady=10)


#? COMENTARIOS------------------------------------------------------------------------------------------------------


comentarioLabel = Label(frame, text="Comentarios:")
comentarioLabel.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


cuadroComentario = Text(frame, width=15, height=6)
cuadroComentario.grid(row=4, column=2, columnspan=3, padx=10, pady=10)


#? VERTICAL SCROLLBAR FOR COMENTARIOS-------------------------------------------------------------------------------


scrollvert = Scrollbar(frame, command=cuadroComentario.yview)
scrollvert.grid(row=4, column=5, sticky="nsew")


cuadroComentario.config(yscrollcommand=scrollvert.set)


#? BOTONES----------------------------------------------------------------------------------------------------------


createButton = Button(frame, text="Create", command=crearRegistro)
createButton.grid(row=5, column=0, padx=10, pady=10)


readButton = Button(frame, text="Read", width=5, command=lambda:leerRegistro(idPantalla.get()))
readButton.grid(row=5, column=1, padx=10, pady=10)


updateButton = Button(frame, text="Update", command=lambda:actualizarRegistro(idPantalla.get()))
updateButton.grid(row=5, column=2, padx=10, pady=10)


deleteButton = Button(frame, text="Delete", command=lambda:eliminarRegistro(idPantalla.get()))
deleteButton.grid(row=5, column=3, columnspan=3, padx=10, pady=10)


quitarFoco = Button(frame, text="Quitar foco", command=desenfocar)
quitarFoco.grid(row=8, column=0, columnspan=6, padx=10, pady=10)


#? ID---------------------------------------------------------------------------------------------------------------


idLabel = Label(frame, text="Id:")
idLabel.grid(row=7, column=0, columnspan=2, padx=10, pady=10)


cuadroId = Entry(frame, textvariable=idPantalla)
cuadroId.grid(row=7, column=2, columnspan=3, padx=10, pady=10)


root.mainloop()

