
import PySimpleGUI as sg
import logo as imgLogo
import mic as imgMic
import asistente_virtual as pjem

def Asistente(window_name):
    sg.theme('Dark')
    layout =[
        [sg.Button( 'Salir',
        key='_SALIR_')],
        [sg.Image(data=imgLogo.logo2,key='_IMAGE_')],
        [sg.Button(
        '',
        image_data= imgMic.mic2, # Carga la imagen del microfono en el boton
        button_color= (sg.theme_background_color(), sg.theme_background_color()), # Elimina el color negro de fondo del gif
        border_width=0,
        key='_MIC_'
        )
     ],
     []
    ]

    window = sg.Window(
        title='',
        layout=layout,
        no_titlebar=True,
        grab_anywhere= True,
        auto_size_buttons=False,
        auto_size_text=False,
        finalize=True,
        alpha_channel=1,
        transparent_color= '#000000' # Transparenta el color de fondo de la ventana
    )


    while True:
        event, values = window.read(timeout=10)
        #pjem.run()
        if event == '_MIC_':
            print("activo microfono")
            pjem.run()
        if event == sg.WINDOW_CLOSED or event == '_SALIR_':
            break
        window.Element('_IMAGE_').UpdateAnimation(imgLogo.logo2,  time_between_frames=50)
    
    window.close()

Asistente("Asistente del PJEM")