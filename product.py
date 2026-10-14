import tkinter as TK


app=TK.Tk()
app.geometry("1200x600")
app.title("stock managment system")



#-----texts-----
title_text="stock managment system".capitalize()


#------Frames------
title_frame=TK.Frame(app,bg="#20403A")
title_frame.pack(side="top",fill='x')

action_frame=TK.Frame(app,bg='silver',width=300)
action_frame.pack(fill='y',side='left')
action_frame.pack_propagate(False)

#------Labels------
title_label=TK.Label(title_frame,text=title_text,font=('Tajwal',20),fg='white',bg="#20403A")
title_label.pack(pady=20)

action_label=TK.Label(action_frame,text='Actions',font=('Tajwal',15),fg="#20403A",bg='silver')
action_label.pack(side='top',pady=20)

#------buttons-----


app.mainloop()
