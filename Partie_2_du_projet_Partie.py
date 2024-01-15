import tkinter

def lancer_analyse():
    url_page = entry_url.get()
    mots_cles = entry_mots_cles.get()

    if not url_page or not mots_cles:
        messagebox.showerror("Erreur", "Veuillez entrer l'URL de la page et les mots-clés.")
        return

    print("URL de la page :", url_page)
    print("Mots-clés :", mots_cles)


root = tkinter.Tk()
root.title("Analyse de page")

label_url = tkinter.Label(root, text="Entrez l'URL de la page :")
label_url.pack()

entry_url = tkinter.Entry(root, width=50)
entry_url.pack()

label_mots_cles = tkinter.Label(root, text="Entrez les mots-clés (séparés par des virgules) :")
label_mots_cles.pack()

entry_mots_cles = tkinter.Entry(root, width=50)
entry_mots_cles.pack()

bouton_analyse = tkinter.Button(root, text="Lancer l'analyse", command=lancer_analyse)
bouton_analyse.pack()

root.mainloop()
