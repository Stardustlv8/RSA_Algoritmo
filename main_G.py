import gtk
import gtk.glade
from RSA_1.CRIPTO import fprim, expresion
from RSA_1.GEN import emod, t_mr
from RSA_1.RSA import euext, inverso, mcd, mcm
from RSA_1.BETA import encripta, desencriptar, gen_cl_pp

class Grafico:
    def __init__(self):
	self.proyecto = gtk.glade.XML('Rsa_1.0.4')
        self.proyecto.signal_autoconnect(self)
	self.archivo1 = ""
	self.archivo2 = ""
	self.archivo3 = ""
	self.respuesta= ""
	self.ventana = self.proyecto.get_widget('window1')
	self.ventana.set_title("RSA 1.0.4")
	# items del menu
        self.menuimagen4 = self.proyecto.get_widget('imagemenuitem4')	
        self.menuimagen5 = self.proyecto.get_widget('imagemenuitem5')	
        self.menuimagen8 = self.proyecto.get_widget('imagemenuitem8')	
        self.menuimagen9 = self.proyecto.get_widget('imagemenuitem9')	
        self.menuimagen10 = self.proyecto.get_widget('imagemenuitem10')	
        self.menuimagen11 = self.proyecto.get_widget('imagemenuitem11')	
        self.menuimagen12 = self.proyecto.get_widget('imagemenuitem12')	
        self.menuimagen13 = self.proyecto.get_widget('imagemenuitem13')	
        self.menuimagen14 = self.proyecto.get_widget('imagemenuitem14')	
        self.menuimagen15 = self.proyecto.get_widget('imagemenuitem15')	
        self.menuimagen16 = self.proyecto.get_widget('imagemenuitem16')	
        self.menuimagen17 = self.proyecto.get_widget('imagemenuitem17')	

	# items botones del espacio de edicion
	self.boton1 = self.proyecto.get_widget('button1')
	self.boton1.set_size_request(20,40)
	self.boton2 = self.proyecto.get_widget('button2')
	self.boton2.set_size_request(20,40)

	# items seleccionador de archivo
	self.selecciona1 = self.proyecto.get_widget('filechooserbutton1')
	self.selecciona2 = self.proyecto.get_widget('filechooserbutton2')
	self.selecciona3 = self.proyecto.get_widget('filechooserbutton3')
	self.selecciona4 = self.proyecto.get_widget('filechooserbutton4')

	# items entry 
	self.entrada1 = self.proyecto.get_widget('entry1')
	self.entrada2 = self.proyecto.get_widget('entry2')
	self.entrada3 = self.proyecto.get_widget('entry3')
	self.entrada4 = self.proyecto.get_widget('entry4')
	self.entrada5 = self.proyecto.get_widget('entry5')
	self.entrada6 = self.proyecto.get_widget('entry6')
	self.entrada7 = self.proyecto.get_widget('entry7')
	self.entrada8 = self.proyecto.get_widget('entry8')
	self.entrada9 = self.proyecto.get_widget('entry9')
	self.entrada10 = self.proyecto.get_widget('entry10')

	# items etiqueta
	self.etiqueta1 = self.proyecto.get_widget('label12')
	self.etiqueta2 = self.proyecto.get_widget('label16')
	self.etiqueta3 = self.proyecto.get_widget('label20')
	self.etiqueta4 = self.proyecto.get_widget('label22')
	self.etiqueta5 = self.proyecto.get_widget('label26')
	self.etiqueta6 = self.proyecto.get_widget('label1')
	
	# Cajas contenedoras.
	self.box2 = self.proyecto.get_widget('vbox2')
	self.box3 = self.proyecto.get_widget('vbox3')
	self.box4 = self.proyecto.get_widget('vbox4')
	self.box5 = self.proyecto.get_widget('vbox5')
	self.box6 = self.proyecto.get_widget('vbox6')
	self.box7 = self.proyecto.get_widget('vbox7')
	self.box8 = self.proyecto.get_widget('vbox8')
	self.box9 = self.proyecto.get_widget('vbox9')
	self.box10 = self.proyecto.get_widget('vbox10')

    def main(self):
	gtk.main()

    def on_window1_destroy(self,widget):# Destruir Ventana
	gtk.main_quit()	
	
    def on_imagemenuitem4_activate(self,widget):#inicio
	self.etiqueta6.set_visible(True) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   

    def on_imagemenuitem5_activate(self,widget):#salir
	gtk.main_quit()        

    def on_imagemenuitem8_activate(self,widget):# generar Claves
	self.etiqueta6.set_visible(False) # inicio
	self.box2.set_visible(True)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   
	        
    def on_imagemenuitem9_activate(self,widget):# Encriptar
	self.etiqueta6.set_visible(False) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(True)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   
	        
    def on_imagemenuitem10_activate(self,widget):# Acerca de
	self.show_aboutdialog()	        

    def on_imagemenuitem11_activate(self,widget):# Desencriptar
	self.etiqueta6.set_visible(False) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(True)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   
        
    def on_imagemenuitem12_activate(self,widget):# Euclides
	self.etiqueta6.set_visible(False) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(True)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   
        
    def on_imagemenuitem13_activate(self,widget):# Euclides Extendido
	self.etiqueta1.set_visible(False) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(True)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   
        
    def on_imagemenuitem14_activate(self,widget):# Congruente
	self.etiqueta6.set_visible(False) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(True)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   

    def on_imagemenuitem15_activate(self,widget):# Factorizacion Prima
	self.etiqueta6.set_visible(False) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(True)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   

    def on_imagemenuitem16_activate(self,widget):# Generar Primo
	self.etiqueta6.set_visible(False) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(True)     # Generar Primo  
	self.box10.set_visible(False)    # Comprobar Primalidad   

    def on_imagemenuitem17_activate(self,widget):# Comprueba Primo
	self.etiqueta6.set_visible(False) # inicio
	self.box2.set_visible(False)     # Generar Claves  
	self.box3.set_visible(False)     # Encriptar
	self.box4.set_visible(False)     # Desencriptar
	self.box5.set_visible(False)     # mcm,mcd  
	self.box6.set_visible(False)     # eu_ext inv_mod  
	self.box7.set_visible(False)     # Congruencias  
	self.box8.set_visible(False)     # Factorizacion Prima  
	self.box9.set_visible(False)     # Generar Primo  
	self.box10.set_visible(True)    # Comprobar Primalidad   

    def on_button1_clicked(self,widget): #Generar Claves
	self.show_aboutdialog1()	
	if self.respuesta=="yes":
	    gen_cl_pp.Generar_Claves()
	else:
	    pass
	self.respuesta = ""

    def show_aboutdialog2(self):
	boton=(gtk.STOCK_YES, gtk.RESPONSE_YES)
	about = gtk.Dialog(buttons=boton)
	about.set_title("Proceso Terminado!")
	etiqueta= gtk.Label()
	etiqueta.set_text("El archivo se encuentra en la ruta:\n"+self.archivo1)
	hcaja=gtk.HBox()
	hcaja.pack_start(etiqueta,False,False,2)
	about.vbox.pack_start(hcaja,False,False,2)
	about.show_all()
	response=about.run()
        about.destroy()

    def show_aboutdialog1(self):
	boton=(gtk.STOCK_YES, gtk.RESPONSE_YES,gtk.STOCK_NO, gtk.RESPONSE_NO)
	about = gtk.Dialog(buttons=boton)
	about.set_title("Advertencia!")
	etiqueta= gtk.Label()
	etiqueta.set_text("Este proceso puede demorar varios minutos\nDesea Continuar?")
	hcaja=gtk.HBox()
	hcaja.pack_start(etiqueta,False,False,2)
	about.vbox.pack_start(hcaja,False,False,2)
	about.show_all()
	response=about.run()
	if response == gtk.RESPONSE_YES:
	    self.respuesta="yes"
	else:
	    self.respuesta="no"
        about.destroy()

    def show_aboutdialog(self):
	about = gtk.AboutDialog()
	about.set_program_name("Manual...")
	about.set_comments("Se puede Utilizar la aplicacion intuitivamente...")
	about.set_name("Referencia rapida")
	nombres=['Aviel Aldama Diaz','Alan Job de la Luz Hernandez','Arely Garcia Perez','Ramses Hernandez Hernandez']
	about.set_authors(nombres)
	about.show()
	response=about.run()
        about.destroy()


    def on_button2_clicked(self,widget): #Generar posible primo
	self.show_aboutdialog1()	
	if self.respuesta=="yes":
            t_mr.genera_1()
	    self.archivo3= t_mr.salida[0]
	    self.entrada9.set_text(str(self.archivo3))
	else:
	    pass
	self.respuesta=""	

    def on_filechooserbutton1_file_set(self,widget):#clave publica
	self.archivo1 = widget.get_filename()

    def on_filechooserbutton2_file_set(self,widget):#archivo
	self.archivo2 = widget.get_filename()

    def on_filechooserbutton3_file_set(self,widget):#clave privada
	self.archivo1 = widget.get_filename()

    def on_filechooserbutton4_file_set(self,widget):# archivo
	self.archivo2 = widget.get_filename()

    def on_entry1_activate(self,widget):# Encripta
        self.archivo3 = widget.get_text()
	if self.archivo1 and self.archivo2 and self.archivo3:
            encripta.Encriptar(self.archivo1,self.archivo2,self.archivo3)
	else:
	    pass
	widget.set_text("")

    def on_entry2_activate(self,widget): # desencripta
        self.archivo3 = widget.get_text()
	if self.archivo1 and self.archivo2 and self.archivo3:
            desencriptar.Desencriptar(self.archivo1, self.archivo2, self.archivo3)
	else:
	    pass
	widget.set_text("")
	self.show_aboutdialog2()	

    def on_entry3_activate(self,widget):# mcd
        val=widget.get_text()
	widget.set_text("")
	valores=expresion.analiza_enteros(val)
	salida="Resultado: \n%s" % (mcd.mcd(valores[0],valores[1]),)
	self.etiqueta1.set_text(salida)
	self.show_aboutdialog2()	

    def on_entry4_activate(self,widget):# mcm
        val=widget.get_text()
	widget.set_text("")
	valores=expresion.analiza_enteros(val)
	salida="Resultado: \n%s" % (mcm.mcm(valores[0],valores[1]),)
	self.etiqueta1.set_text(salida)

    def on_entry5_activate(self,widget):# euclides extendido
	val=widget.get_text()
	widget.set_text("")
	valores=expresion.analiza_enteros(val)
	extendido=euext.euext(valores[0],valores[1])
	max=mcd.mcd(valores[0],valores[1])
	salida="Resultado:\n %s = (%s)%s + (%s)%s"%(max,valores[0],extendido[0],valores[1],extendido[1])
	self.etiqueta2.set_text(salida)

    def on_entry6_activate(self,widget):# inverso modular
	val=widget.get_text()
	widget.set_text("")
	valores=expresion.analiza_enteros(val)
	inv=inverso.inverso(valores[0],valores[1])
	salida="Resultado: \n%s"%(inv,)	
	self.etiqueta2.set_text(salida)

    def on_entry7_activate(self,widget):# Congruente
	val=widget.get_text()
	widget.set_text("")
	valores = expresion.analiza_enteros2(val)
	mod = emod.expmod(valores[0], valores[1], valores[2])
	salida="Resultado: \n%s"%(mod,)
	self.etiqueta3.set_text(salida)

    def on_entry8_activate(self,widget):# factorizacion prima
	val=widget.get_text()
	widget.set_text("")
	valores=expresion.analiza_entero(val)
	inv=fprim.primo(valores)
	salida="Resultado: \n"+str(inv)	
	self.etiqueta4.set_text(salida)	

    def on_entry10_activate(self,widget):# Comprobar primo
	bol=False
	val=widget.get_text()
	widget.set_text("")
	valores=expresion.analiza_entero(val)
	bol = t_mr.primo(valores)
	salida=""

	if bol:
	    salida = "Resultado: \n Es posiblemente un numero primo"
	else:
	    salida = "Resultado: \n Posiblemente no es un numero primo"
		
	self.etiqueta5.set_text(salida)	
	


graf = Grafico()
graf.main()
