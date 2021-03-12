import socket
import sys
from threading import *

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.picker import MDThemePicker

Window.size = (350, 700)

Builder.load_string("""
<Button@Button>:
	halign:'left'

<MDLabel@MDLabel>:
	theme_text_color:'Custom'
	text_color:[190/255,190/255,190/255,1]

<MBoxLayout@BoxLayout>:
    elevation:8
	size_hint_y:0
	padding:12
	canvas.before:
		Color:
			rgba:(48/255,63/255,159/255,1)
		RoundedRectangle:
			pos:self.pos
			size:self.size
			radius:[0,21,21,21]


<Label@Label>:
	color:[190/255,190/255,190/255,1]

<box>:
	elevation:8
	size_hint_y:0
	padding:12
	canvas.before:
		Color:
			rgba:(48/255,63/255,159/255,1)
		RoundedRectangle:
			pos:self.pos
			size:self.size
			radius:[0,21,21,21]

<MainApp>:
	orientation:'vertical'
	canvas.before:
		Color:
			rgba:(1,1,0,1)
		Rectangle:
			pos:self.pos
			size:self.size

	MDToolbar:
		icon:'android-messages'
		type:'bottom'
		elevation:12
		mode:'free-end'
		left_action_items:[['arrow-left', lambda x: root.contacts_()]]
		on_action_button:
			root.receive_msg()
		MDIconButton:
			height:'50dp'
			size_hint:(None, None)
			# width:'50dp'
			pos_hint:{'center_x':.1, 'center_y':.5}
			canvas.before:
				Color:
					rgba:(1,1,1,1)
				RoundedRectangle:
					pos:self.pos
					size:self.size
					radius:[30]
					source:'da.jpg'
		MDFlatButton:
			text:'Rogers'
			color:[1,1,1,1]
			font_size:17
			theme_text_color:'Custom'
			text_color:[1,1,1,1]
			pos_hint:{'center_x':.5, 'center_y':.5}

		Label:
			text:''

		MDIconButton:
			text_color:[0,0,0,1]
			theme_text_color:'Custom'
			text_color:[1,1,1,1]
			icon:'wifi'	
			pos_hint:{'center_y':.5, 'center_x':.7}
			on_release:
				root.chatting_()
		MDIconButton:
			text_color:[0,0,0,1]
			theme_text_color:'Custom'
			text_color:[1,1,1,1]
			icon:'moon-waxing-crescent'	
			pos_hint:{'center_y':.5, 'center_x':.7}
			on_release:
				root.settings_()
		MDIconButton:
			text_color:[0,0,0,1]
			theme_text_color:'Custom'
			text_color:[1,1,1,1]
			icon:'dots-vertical'	
			pos_hint:{'center_y':.5, 'center_x':.7}
			on_release:
				root.settings_()


	MDBoxLayout:
		pos_hint:{'center_x':.5, 'center_y':.5}
		ScreenManager:
			id:screen_manager
			Screen:
				name:'contacts'
				BoxLayout:
					canvas.before:
						Color:
							rgba:(1,1,1,1)
						Rectangle:
							pos:self.pos
							size:self.size
							source:'background.jpg'
					canvas.after:
						Color:
							rgba:(0,0,0,.5)
						Rectangle:
							pos:self.pos
							size:self.size
					ScrollView:
						id:net
						BoxLayout:
							id:chattingui
							height:800
							size_hint_x:1
							size_hint_y:None
							orientation:'vertical'
							padding:'12dp'
							spacing:30	
							BoxLayout:
								elevation:10
								size_hint_y:0
								padding:12
								canvas.before:
									Color:
										rgba:(30/255,136/255,229/255,1)
									RoundedRectangle:
										pos:self.pos
										size:self.size
										radius:[21,0,21,21]
								Label:
									font_size:12
									color:[1,1,1,1]
									size_hint_x:1
									size_hint_y:None
									text_size:self.size
									valign:'center'
									font_size:12
									text:'first chat '						
		

				FloatLayout:
					pos_hint:{'center_x':.5, 'center_y':.5}
					size_hint:(.87,1)
					BoxLayout:
						pos_hint:{'center_x':.45}
						height:'43dp'
						id:txwrite
						size_hint:(1, None)
						padding:4
						canvas.before:
							Color:
								rgba:(38/255,50/255,56/255,1)
							RoundedRectangle:
								pos:self.pos
								size:self.size
								radius:[20]
						MDIconButton:
							icon:'wifi'
							size_hint:(1/5,1)
							theme_text_color:'Custom'
							text_color:(1,1,1,1)
							text:''
						TextInput:
							foreground_color:[240/255,240/255,240/255,1]
							background_color:[0,0,0,0]
							background_normal:''
							height:'37dp'
							cursor_color:[21/255,101/255,192/255,1]
							cursor_width:3
							cursor_height:3
							hint_text:'Type chat...'
							id:txt
							on_focus:
								root.mover()
						MDIconButton:
							icon:'content-copy'
							size_hint:(1/5,1)
							theme_text_color:'Custom'
							text_color:(1,1,1,1)
							text:''
					MDIconButton:
						id:sender_btn
						icon:'telegram'
						pos_hint:{'center_x':.99, 'center_y':.1}
						on_release:
							root.interfacey()
						on_release:
							root.back()
					MDFloatingActionButton:
						pos_hint:{'center_y':.7, 'center_x':.9}
						icon:'message'
						on_release:
							root.receive_msg()
					
				
				
				
			Screen:
				name:'chat'
				FloatLayout:
					MDLabel:
						pos_hint:{'center_x':.5, 'center_y':.75}
						halign:'center'
						size_hint:(1,None)
						text:'Connect'
						id:not_conn
						font_style:'H5'
						font_family:'Ubuntu Mono'
						theme_text_color:'Custom'
						text_color:(0,0,0,.9)
					MDLabel:
						theme_text_color:'Custom'
						text_color:(0,0,0,.9)
						font_style:'Caption'
						pos_hint:{'center_x':.5, 'center_y':.7}
						halign:'center'
						size_hint:(1,None)
						text:'Press to connect'
					MDFloatingActionButton:
						elevation:
						md_bg_color:[1,1,1,1]
						pos_hint:{'center_x':.69, 'center_y':.6}
						icon:'wifi'
						on_release:
							root.connection()
					MDFloatingActionButton:
						elevation:4
						md_bg_color:[1,1,1,1]
						pos_hint:{'center_x':.31, 'center_y':.6}
						icon:'network'
						on_release:
							root.connectee()
					MDLabel:
						font_size:13
						theme_text_color:'Custom'
						text_color:(1,1,1,.5)
						pos_hint:{'center_x':.5, 'center_y':.5}
						halign:'center'
						size_hint:(1,None)
						text:f'00:00:00'
						theme_text_color:'Custom'
						text_color:(0,0,0,.9)
					MDLabel:
						id:feedback
						font_size:15
						theme_text_color:'Custom'
						text_color:(190/255,190/255,190/255,1)
						pos_hint:{'center_x':.5, 'center_y':.4}
						halign:'center'
						size_hint:(1,None)
						theme_text_color:'Custom'
						text_color:(0,0,0,.9)
						text:'feedback'
					MDLabel:
						id:solver
						font_size:14
						theme_text_color:'Custom'
						text_color:(0,0,0,.9)
						pos_hint:{'center_x':.5, 'center_y':.3}
						halign:'center'
						size_hint:(.8,None)
						text:'retry procedure'
		
		
			Screen:
				name:'settings'
				GridLayout:
					cols:2
					#orientation:'vertical'
					size_hint:(.9,.9)
					pos_hint:{'center_x':.5, 'center_y':.5}
					FloatLayout:
						MDRectangleFlatIconButton:	
							pos_hint:{'center_x':.5, 'center_y':.5}
							text:'Theme'
							on_release:
								root.theme( )

			Screen:
				name:'profile'
				MDLabel:
					text:'Profile'
					font_style:'H4'
					halign:'center'
					size_hint:(1, None)
					pos_hint:{'center_x':.5, 'center_y':.79}
				MDLabel:
					text:'Username and Image'
					font_style:'Caption'
					halign:'center'
					size_hint:(1, None)
					pos_hint:{'center_x':.5, 'center_y':.73}
				MDTextField:
					hint_text:'Name'
					size_hint:(.9, None)
					max_lenght:7
					hint_text_color:[0,0,0,1]
					icon_right:'account'
					pos_hint:{'center_x':.5, 'center_y':.63}
					mode:'fill'
					fill_color:[0,0,0,.2]
					line_color_focus:[1,1,1,1]
					line_color_normal:[1,1,1,1]

				MDRectangleFlatIconButton:
					text:'Create'
					icon:'creation'
					pos_hint:{'center_x':.5, 'center_y':.34}
			
	
				
<sent>:
	elevation:8
	size_hint_y:0
	padding:12
	canvas.before:
		Color:
			rgba:(236/255,239/255,241/255,1)
		RoundedRectangle:
			pos:self.pos
			size:self.size
			radius:[0,21,21,21]
	Label:
		id:sent_chat
		font_size:12
		color:[0,0,0,1]
		size_hint_x:1
		size_hint_y:None
		text_size:self.size
		valign:'center'
		font_size:12
		# text:'what'
		
		
<chat_rec>:
	elevation:8
	size_hint_y:0
	padding:12
	canvas.before:
		Color:
			rgba:(30/255,136/255,229/255,1)
		RoundedRectangle:
			pos:self.pos
			size:self.size
			radius:[21,0,21,21]
	Label:
		id:sent_chat
		font_size:12
		color:[1,1,1,1]
		size_hint_x:1
		size_hint_y:None
		text_size:self.size
		valign:'center'
		font_size:12
		# text:'what'


<received>:
	elevation:10
	size_hint_y:0
	padding:12
	canvas.before:
		Color:
			rgba:(60/255,62/255,68/255,1)
		RoundedRectangle:
			pos:self.pos
			size:self.size
			radius:[21,0,21,21]
	Label:
	    id:chat_senty
		font_size:12
		color:[200/255,200/255,200/255,1]
		size_hint_x:1
		size_hint_y:None
		text_size:self.size
		valign:'center'
		font_size:12
		text:'what'
""")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if True:
    try:
        client, address = s.accept()
    except:
        pass


class sent(BoxLayout):
    def __init__(self, chat='nothing sent', **kwargs):
        super(sent, self).__init__(**kwargs)
        self.chat = chat
        self.from_me()

    def from_me(self):
        chats = self.chat
        txt = self.ids.sent_chat
        txt.text = chats


class chat_rec(BoxLayout):
    def __init__(self, chat='nothing sent', **kwargs):
        super(chat_rec, self).__init__(**kwargs)
        self.chat = chat
        self.from_me()

    def from_me(self):
        chats = self.chat
        txt = self.ids.sent_chat
        txt.text = chats


class received_now(BoxLayout):
    def __init__(self, chat='nothing sent', **kwargs):
        super(received_now, self).__init__(**kwargs)
        self.chat = chat
        self.from_me()

    def from_me(self):
        chats = self.chat
        txtxt = self.ids.chat_senty
        txtxt.text = chats


class MainApp(MDBoxLayout):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

    def theme(self):
        them = MDThemePicker()
        them.open()

    def mover(self):
        va = self.ids.txwrite
        va.pos_hint = {'center_y': .5}
        vat = self.ids.sender_btn
        vat.pos_hint = {'center_y': .5}

    def back(self):
        va = self.ids.txwrite
        va.pos_hint = {'center_y': .1}
        vat = self.ids.sender_btn
        vat.pos_hint = {'center_y': .1}

    def connection(self):
        tav = self.ids.not_conn
        solve = self.ids.solver

        class sock(Thread):
            def run(Thread):
                host = socket.gethostbyname(socket.gethostname())
                port = 1725
                s.bind((host, port))
                s.listen(5)
                print(f'{host}:{port}')
                print('all successful')
                solve.text = 'No worries,\nconnection successful'
                solve.color = [76 / 255, 175 / 255, 80 / 255, 1]
                solve.bold = True
                tav.text = 'Connected'

        SOCK = sock()

        if tav.text != 'You are Connected' and tav.text != 'Connected':
            try:
                SOCK.start()
            except:
                if tav.text == 'Connected':
                    pass
                else:
                    solve.text = 'Please retry, failed to connect'
                    solve.color = [239 / 255, 83 / 255, 80 / 255, 1]
                    tav.text = 'Retry Failed'

    def connectee(self):
        tav = self.ids.not_conn
        solve = self.ids.solver

        class my_clients(Thread):
            def run(Thread):
                t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostbyname(socket.gethostname())
                port = 1725
                t.connect((host, port))
                print('client connected successfully')
                t.close()

                solve.text = 'No worries,\nconnection successful'
                solve.color = [76 / 255, 175 / 255, 80 / 255, 1]
                tav.text = 'You are Connected'

        net = my_clients()

        if tav.text != 'Connected':
            if tav.text != 'You are Connected':
                try:
                    net.start()
                except:
                    if tav.text == 'You are Connected':
                        pass
                    else:
                        solve.text = 'Please retry, failed to connect'
                        solve.color = [239 / 255, 83 / 255, 80 / 255, 1]
                        tav.text = 'Retry Failed'
        else:
            pass

    def whilt(self):
        pass

    def tat(self):
        pap = self.ids.top_tool
        pap.text = 'metatre'

    def goo(self, dt):
        pap = self.ids.top_tool
        gui = self.ids.chattingui
        va = self.ids.txt
        gui = self.ids.chattingui
        my_txt = 'hello world '
        sender = sent(my_txt)

        nuxy = Label(text='roger it worked')
        gui.add_widget(nuxy)
        pap.text = 'metatre'
        if pap.text == 'Rogers':
            pap.text = 'metatre'
        else:
            pap.text = 'Rogers'

    def receive_msg(self):
        gui = self.ids.chattingui
        tav = self.ids.not_conn

        class client_rec_sock(Thread):
            def run(self):
                client, address = s.accept()
                msg = client.recv(5000).decode()
                print(msg)
                if msg == '':
                    pass
                else:
                    chat_recv = chat_rec(msg)
                    gui.add_widget(chat_recv)
                sys.exit()

        class sock_rec_sock(Thread):
            def run(self):
                ttyy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostbyname(socket.gethostname())
                port = 1725
                ttyy.connect((host, port))
                msg = ttyy.recv(5000).decode()
                print(msg)
                if msg == '':
                    pass
                else:
                    chat_recv = chat_rec(msg)
                    gui.add_widget(chat_recv)
                ttyy.close()
                sys.exit()

            pass

        crs = client_rec_sock()
        srs = sock_rec_sock()
        if True:
            try:
                if tav.text == 'You are Connected':
                    print(tav.text)
                    srs.start()
                elif tav.text == 'Connected':
                    print(tav.text)
                    crs.start()
            except:
                print('failed')

    def contacts_(self):
        self.ids.screen_manager.current = 'contacts'

    def chatting_(self):
        self.ids.screen_manager.current = 'chat'

    def settings_(self):
        self.ids.screen_manager.current = 'settings'

    def profile(self):
        self.ids.screen_manager.current = 'profile'

    def interfacey(self):
        va = self.ids.txt
        gui = self.ids.chattingui
        textex = va.text
        tav = self.ids.not_conn

        class receiving_socket(Thread):
            def run(Thread):
                tts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostbyname(socket.gethostname())
                port = 1725
                tts.connect((host, port))
                print(textex)
                tts.send(textex.encode())
                tts.close()

        class sending_socket(Thread):
            def run(Thread):
                client, address = s.accept()
                print(f'{address} is chatting')
                print(textex)
                client.send(textex.encode())

        if tav.text == 'Connected':
            if textex == '':
                pass
            else:
                sender = sent(textex)
                gui.add_widget(sender)
                vart = sending_socket()
                vart.start()
                va.text = ''
        elif tav.text == 'You are Connected':
            if textex == '':
                pass
            else:
                sender = sent(textex)
                gui.add_widget(sender)
                varty = receiving_socket()
                varty.start()
                va.text = ''


class app(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '900'
        self.theme_cls.theme_style = 'Light'
        nety = MainApp()
        return MainApp()

    def navigation_drawer(self):
        print("it worked")


if __name__ == '__main__':
    app().run()
