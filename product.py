import tkinter as TK


app=TK.Tk()
app.geometry("1200x600")
app.title("stock managment system")



#-----title-----
title_text="stock managment system".capitalize()
title_frame=TK.Frame(app,bg="#20403A")
title_frame.pack(side="top",fill='x')

title_label=TK.Label(title_frame,text=title_text,font=('Tajwal',20),fg='white',bg="#20403A")
title_label.pack(pady=20)

#------action------
actions_bg="#D4D3D3"

action_frame=TK.Frame(app,bg=actions_bg,width=300)
action_frame.pack(fill='y',side='left')
action_frame.pack_propagate(False)

action_label=TK.Label(action_frame,text='Actions',font=('Tajwal',15),fg="#20403A",bg=actions_bg)
action_label.pack(side='top',pady=20)


#------button------
buttons_frame=TK.Frame(action_frame,bg='black',width=150,height=150)
buttons_frame.pack()



app.mainloop()
