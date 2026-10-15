import tkinter as TK
from tkinter import ttk

app=TK.Tk()
app.geometry("1200x600")
app.title("stock managment system")

products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 699.50, "category": "Electronics"},
    {"id": 3, "name": "Headphones", "price": 59.99, "category": "Accessories"},
    {"id": 4, "name": "Running Shoes", "price": 89.90, "category": "Clothing"},
    {"id": 5, "name": "T-Shirt", "price": 19.99, "category": "Clothing"},
    {"id": 6, "name": "Coffee Maker", "price": 45.00, "category": "Home"},
    {"id": 7, "name": "Desk Lamp", "price": 24.95, "category": "Home"},
    {"id": 8, "name": "Backpack", "price": 39.99, "category": "Accessories"},
]

actions_bg="#D4D3D3"
main_bg="#20403A"
#-----title-----
title_text="stock managment system".capitalize()
title_frame=TK.Frame(app,bg=main_bg)
title_frame.pack(side="top",fill='x')

title_label=TK.Label(title_frame,text=title_text,font=('Tajwal',20),fg='white',bg=main_bg)
title_label.pack(pady=20)

#---footer---
footer_frame=TK.Frame(app,bg=main_bg)
footer_frame.pack(side="bottom",fill='x')
footer_label=TK.Label(footer_frame,text='Developed by belhamri imad eddine lahouari',font=('Tajwal',10),fg='white',bg=main_bg)
footer_label.pack(pady=10)

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
dashboard_btn.pack(pady=(20,0))
products_btn=TK.Button(buttons_frame,**btn_style,text='Products')
products_btn.pack(pady=(20,0))
add_btn=TK.Button(buttons_frame,**btn_style,text='Add')
add_btn.pack(pady=(20,0))
quit_btn=TK.Button(buttons_frame,text='Quit',bg='red', font=("Tahoma", 14, "bold"),width= 15,height= 2,fg="white",cursor="hand2",relief="flat",)
quit_btn.pack(pady=(20,0))

#----the dashboard section-----

dashboard_frame = TK.Frame(app, bg='white')
dashboard_frame.pack(side="right", fill="both", expand=True)

products_count = len(products)
categorys=[]
for i in products:
 if i['category'] not in categorys:
   categorys.append(i['category'])

categories_count=len(categorys)


boxes_frame = TK.Frame(dashboard_frame, bg='white')
boxes_frame.place(relx=0.5, rely=0.5, anchor="center")


box1 = TK.Frame(boxes_frame, bg=main_bg, width=250, height=150)
box1.pack_propagate(False)
box1.pack(side="left", padx=40)
TK.Label(box1, text=products_count, font=('Tahoma', 40, 'bold'), bg=main_bg, fg='white').pack(pady=(25, 0))
TK.Label(box1, text="Products", font=('Tahoma', 16), bg=main_bg, fg='white').pack()

box2 = TK.Frame(boxes_frame, bg=main_bg, width=250, height=150)
box2.pack_propagate(False)
box2.pack(side="left", padx=40)
TK.Label(box2, text=categories_count, font=('Tahoma', 40, 'bold'), bg=main_bg, fg='white').pack(pady=(25, 0))
TK.Label(box2, text="Categories", font=('Tahoma', 16), bg=main_bg, fg='white').pack()

#---products section----



app.mainloop()
