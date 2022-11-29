from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.core.window import Window

Window.size = (300, 500)

helper1 = '''
#------NAVIGATION-DRAWER-CONTENTS----

<ContentNavigationDrawer>
	MDNavigationDrawer:
		MDNavigationDrawerMenu:

#-----------------------HEADER----------------------------
			
			MDNavigationDrawerHeader:
				title: 'Calculator'
				text: 'Simple Calculator'
				
	
			MDNavigationDrawerDivider:
				
#---------NAVIGATION-DRAWER-APPS-----------	
			MDNavigationDrawerLabel:
				text: 'Apps'
			MDNavigationDrawerItem:
				icon: 'calculator-variant-outline'
				text: 'Calculator'
				right_text: '+-÷×'
				on_release: 
					root.screen_manager.current = 'calculator'
					root.nav_drawer.set_state('close')
			
			MDNavigationDrawerDivider:
				
#--------NAVIGATION-DRAWER-OTHERS-------

			MDNavigationDrawerLabel:
				text: 'Others'
				
			MDNavigationDrawerItem:
				icon: 'cog'
				text: 'Settings'
				on_release:
					root.nav_drawer.set_state('close')
					root.screen_manager.current = 'settings'
					
			MDNavigationDrawerItem:
				icon: 'information'
				text: 'About'
				on_release:
					root.screen_manager.current = 'about'
					root.nav_drawer.set_state('close')
					
#---------------------TOP-APPBAR------------------------
MDScreen:
	
	MDTopAppBar:
		title: 'TopBar'
		pos_hint: {'top':1}
		left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
		
	MDNavigationLayout:
		
		MDScreenManager:
			id: screen_manager			
					
#--------------------CALCULATOR-----------------------
			MDScreen:
				name: 'calculator'
				
				MDTextField:
					text: ''
					id: display
					hint_text: 'Calculate!'
					pos_hint: {'center_x':0.450, 'center_y':0.675}
					size_hint_x: None
					width:250
					size_hint_y: None
					height: 60
					input_filter: 'float'
					on_text: if self.text == '01': self.text = '1'
					on_text: if self.text == '02': self.text = '2'
					on_text: if self.text == '03': self.text = '3'
					on_text: if self.text == '04': self.text = '4'
					on_text: if self.text == '05': self.text = '5'
					on_text: if self.text == '06': self.text = '6'
					on_text: if self.text == '07': self.text = '7'
					on_text: if self.text == '08': self.text = '8'
					on_text: if self.text == '09': self.text = '9'
					on_text: if self.text == '00': self.text = '0'
					
				MDFlatButton:
					id: comma_button
					text: '.'
					size_hint: 0.25,0.15
					on_press: display.text += self.text
					on_press: if display.text == "": display.text = "0"
					disabled: True if display.text == "" or display.text[-1] == "." else False
					# if there is no text in the display, the comma button is disabled
					# if the last character in the display is a comma, the comma button is disabled
					disabled: True if display.text[-1:] == "." or display.text == "" else False
					
					
				
					
				MDFlatButton:
					text: '0'
					pos_hint: {'center_x': 0.375}
					size_hint: 0.25,0.15
					on_release: display.text += self.text
					on_press: if display.text == "0": display.text = "0"
					disabled: True if display.text == "0" else False
				
				MDFlatButton:
					text: '='
					pos_hint: {'center_x': 0.625}
					size_hint: 0.25,0.15
					on_press: display.text = str(eval(display.text))
					disabled: not any(char.isdigit() for char in display.text)
					disabled: True if display.text == "" or display.text[-1] in "./-*+" else False
					on_press: app.catch_error()
					
				MDFlatButton:
					text: '+'
					pos_hint: {'center_x': 0.875}
					size_hint: 0.25,0.15
					on_press: display.text += self.text
					disabled: True if display.text== "" or display.text[-1] in "+-/*" else False
					
				MDFlatButton:
					text: '1'
					pos_hint: {'center_y': 0.225}
					size_hint: 0.25,0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '2'
					pos_hint: {'center_x': 0.375, 'center_y': 0.225}
					size_hint: 0.25,0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '3'
					pos_hint: {'center_x': 0.625, 'center_y': 0.225}
					size_hint: 0.25,0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '-'
					pos_hint: {'center_x': 0.875, 'center_y': 0.225}
					size_hint: 0.25,0.15
					on_press: display.text += self.text
					disabled: True if display.text == "0" or "-" or display.text[-1] in "-" else False
					
				MDFlatButton:
					text: '4'
					pos_hint: {'center_y': 0.375}
					size_hint: 0.25, 0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '5'
					pos_hint: {'center_x': 0.375, 'center_y': 0.375}
					size_hint: 0.25, 0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '6'
					pos_hint: {'center_x': 0.625, 'center_y': 0.375}
					size_hint: 0.25, 0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '*'
					pos_hint: {'center_x': 0.875, 'center_y': 0.375}
					size_hint: 0.25, 0.15
					on_press: display.text += self.text
					disabled: True if display.text == "" or display.text[-1] in "./-*+" else False
					
				MDFlatButton:
					text: '7'
					pos_hint: {'center_y': 0.525}
					size_hint: 0.25, 0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '8'
					pos_hint: {'center_x': 0.375, 'center_y': 0.525}
					size_hint: 0.25, 0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '9'
					pos_hint: {'center_x': 0.625, 'center_y': 0.525}
					size_hint: 0.25, 0.15
					on_press: display.text += self.text
					
				MDFlatButton:
					text: '/'
					pos_hint: {'center_x': 0.875, 'center_y': 0.525}
					size_hint: 0.25, 0.15
					on_press: display.text += self.text
					disabled: True if display.text == "" or display.text[-1] in "./-*+" else False
				
				
				
					
				MDIconButton:
					icon: 'backspace'
					pos_hint: {'center_x': 0.875, 'center_y': 0.675}
					size_hint: 0.25, 0.15
					on_press: display.text = display.text[:-1]
					# if the text has no numbers, the button is disabled
					disabled: not any(char.isdigit() for char in display.text)
					
		
					

				
				
					
					
					
#----------------------SETTINGS--------------------------
			
			MDScreen:
				name: 'settings'
				
				MDLabel:
					text: 'Welcome to Settings'
					halign: 'center'
	
#-------------------------ABOUT----------------------------

			MDScreen:
				name: 'about'
				
				MDLabel:
					text: 'Welcome to About , My Name is Ahmet I am the developer of this app'
					halign: 'center'
									
#-----------------------------------------------------------------
		MDNavigationDrawer:
			id: nav_drawer
			
			ContentNavigationDrawer:
				screen_manager: screen_manager
				nav_drawer: nav_drawer
				
	
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(helper1)

    def catch_error(self):
        try:
            self.root.ids.display.text = str(eval(self.root.ids.display.text))
        except ZeroDivisionError:
            self.root.ids.display.text = '0'


if __name__ == '__main__':
    MyApp().run()
