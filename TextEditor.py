from tkinter import *
from tkinter import filedialog
import os


root = Tk()

root.geometry('600x700')
root.title('TextEditor')


def chenge_theme(theme):
	text_fild['bg'] = view_colors[theme]['text_bg']
	text_fild['fg'] = view_colors[theme]['text_fg']
	text_fild['insertbackground'] = view_colors[theme]['cursor']
	text_fild['selectbackground'] = view_colors[theme]['select_bg']
	
def chenge_fonts(fonts):
		text_fild['font'] = font[fonts]['font']


def notepad_exit():
	root.destroy()


def open_file():
	file_path = filedialog.askopenfilename(title='Выбор Файла')
	if file_path:
		text_fild.delete('1.0', END)
		text_fild.insert('1.0', open(file_path, encoding='utf-8').read())
def cls():
	text_fild.delete('1.0', END)


def save_file():
		file_path = filedialog.asksaveasfilename(title='сохранить')
		f = open(file_path, encoding='utf-8')
		text = text_fild.get('1.0', END)
		f.write(text)
		f.close
	

main_menu = Menu(root)

# Раздел Файл

file_menu = Menu(main_menu)
file_menu.add_command(label='Открыть Файл', command=open_file)
file_menu.add_command(label='Сохранить Файл', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Очистить Экран', command=cls)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)
# Вид

view_menu = Menu(main_menu)
view_menu_sub = Menu(view_menu)
font_menu_sub = Menu(view_menu)

view_menu_sub.add_command(label='Тёмная Тема', command=lambda: chenge_theme('dark'))
view_menu_sub.add_command(label='Светлая Тема', command=lambda: chenge_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comis Sans MS', command=lambda: chenge_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda:chenge_fonts('TNR'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)


main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)

root.config(menu=main_menu)



f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

view_colors = {
          'dark' : {
               'text_bg' : 'black', 'text_fg' : 'lime', 'cursor': 'white', 'select_bg': 'orange'
    
          },
          'light' : {          
              'text_bg' : 'white', 'text_fg' : 'black', 'cursor': 'blue', 'select_bg': 'orange'
          
          
          }


}

font = {
          'Arial' : {
               'font' : 'Arial 14 bold'
    
          },
          'CSMS' : {          
               'font' : ('Comic Sans Ms', 14, 'bold')
          
          
          },
          'TNR' : {
                   'font' : ('Times New Roman', 14, 'bold')
          
          
          
          }


}


          
text_fild = Text(f_text, bg='black', fg='lime', padx=10, pady=10, wrap=WORD,   insertbackground='white', selectbackground='orange', spacing3=10, width=30,font='Arial 14 bold')
text_fild.pack(expand=1, fill=BOTH, side = LEFT)
scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

mainloop()
