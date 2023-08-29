"""
Feito por: Matheus Gabriel Souza Thimoteo Nº27 e Thiago Schmitz Da Silva Nº34
"""
import PySimpleGUI as sg

sg.theme("DarkPurple7")
layout = [
  [sg.Push(), sg.Text("Energia potencial gravitacional"), sg.Push()],
  [sg.Text("Massa (kg)"), sg.Push(), sg.Input(size=(5,1), border_width=0, key="-MASS-")], 
  [sg.Text("Aceleração da gravidade (m/s2)"), sg.Push(), sg.Input(size=(5,1), border_width=0, key="-ACELERATION-")],
  [sg.Text("Altura (m)"), sg.Push(), sg.Input(size=(5,1), border_width=0, key="-HEIGHT-")],
  [sg.Push(), sg.Button("Calcular"), sg.Push()]
   
  ]
  
window = sg.Window("Cálculo de energia potencial gravitacional", layout=layout, font="monospace 20")

while True:
  event, values = window.read()  
  if event == 'Exit' or event == sg.WIN_CLOSED:
    break    
  try:        
    values["-MASS-"] = float(values["-MASS-"])
    values["-ACELERATION-"] = float(values["-ACELERATION-"])
    values["-HEIGHT-"] = float(values["-HEIGHT-"])
  except ValueError:
    pass    
  if values["-MASS-"] == "" or values["-ACELERATION-"] == "" or values["-HEIGHT-"] == "" :    
    sg.popup(f"Preencha todos os campos para ter o resultado", font="Arial 18")    
    
  elif type(values["-MASS-"]) == str or type(values["-ACELERATION-"]) == str or type(values["-HEIGHT-"]) == str:    
    sg.popup(f"Preencha todos os campos somente com números", font="Arial 18") 
    
  else:      
    massa = str(values["-MASS-"])    
    mas = massa.replace(',','.')  
    massa = float(mas)
    aceleracao = str(values["-ACELERATION-"])
    ace = aceleracao.replace(',','.')
    aceleracao = float(ace)
    altura = str(values["-HEIGHT-"])
    alt = altura.replace(',','.')
    altura = float(alt)  
    res = massa * aceleracao * altura
    sg.Popup(f"A energia potencial gravitacional é: {res:.2f}J", font="Arial 18",)    
    window["-MASS-"].update("")
    window["-ACELERATION-"].update("")
    window["-HEIGHT-"].update("")
    
