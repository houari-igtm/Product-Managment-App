import tkinter as TK


app=TK.Tk()
app.geometry("1200x600")
app.title("stock managment system")


actions_bg="#D4D3D3"
main_bg="#20403A"
#-----title-----
title_text="stock managment system".capitalize()
title_frame=TK.Frame(app,bg=main_bg)
title_frame.pack(side="top",fill='x')

title_label=TK.Label(title_frame,text=title_text,font=('Tajwal',20),fg='white',bg=main_bg)
title_label.pack(pady=20)

#------action------

action_frame=TK.Frame(app,bg=actions_bg,width=300)
action_frame.pack(fill='y',side='left')
action_frame.pack_propagate(False)

action_label=TK.Label(action_frame,text='Actions',font=('Tajwal',20),fg="#20403A",bg=actions_bg)
action_label.pack(side='top',pady=20)


#------button------

btn_style = {
            "font": ("Tahoma", 14, "bold"),
            "width": 15,
            "height": 2,
            "fg": "white",
            "relief":"flat",
            "cursor": "hand2",
            "bg":main_bg
            
}


buttons_frame=TK.Frame(action_frame,bg=actions_bg)
buttons_frame.pack()

dashboard_btn=TK.Button(buttons_frame,**btn_style,text='Dashboard')
dashboard_btn.pack(pady=20)
products_btn=TK.Button(buttons_frame,**btn_style,text='Products')
products_btn.pack(pady=20)
add_btn=TK.Button(buttons_frame,**btn_style,text='Add')
add_btn.pack(pady=20)
quit_btn=TK.Button(buttons_frame,text='Quit',bg='red', font=("Tahoma", 14, "bold"),width= 15,height= 2,fg="white",cursor="hand2",relief="flat",)
quit_btn.pack(pady=20)



app.mainloop()
