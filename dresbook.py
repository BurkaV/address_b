#!/usr/bin/python
# -*- coding: utf-8 -*-




print('''
	E - Запис нового контакту
	С - змінити дані контакту
	S - шукати контакт
	L - список контактів
	D - видалити дані

	''')
litera = raw_input('Нажміть одну з клавіш, щоб продовжити:  ')

def look():

	if litera.upper() == 'L':
		import pickle
		
		pikl_out = open('proba', 'rb')
		open_dict = pickle.load(pikl_out)
	#print(open_dict)

		for key, dic in open_dict.items():
	   	 	print('- %s %s, місто: %s, номер телефону: %s' % (key, dic['name'], dic['adresa'], dic['mobil_nomer']))

look()

def add_input():
	import pickle
	pikl_out = open('proba', 'rb')
	open_dict = pickle.load(pikl_out)
	
	#print(open_dict)

	if litera.upper() == 'E':
		name1 = raw_input("Введіть призвіще: ")

		name2 = raw_input("Введіть ім'я: ")

		m_nomer = raw_input("Введіть Номер телефону : ")

		address = raw_input("Введіть адресу: ")
	
		d = {name1:{"name":name2, "mobil_nomer": m_nomer, "adresa": address}}
		open_dict.update(d)
		pikl_out.close()

		pikl_in = open('proba', 'wb')

		pickle.dump(open_dict, pikl_in)
	
		print(open_dict)

		pikl_in.close()


add_input()



def change(): 
	if litera.upper() == 'C':
		import pickle
		#from dresbook import look
		pikl_out = open('proba', 'rb')
		open_dict = pickle.load(pikl_out)
		print(open_dict)

	#МОЖЛИВО ВАРТОТ ВСТАВИ ТИ СЮДИ ФУНКЦІЮ ВІДОБРАЖЕННЯ

		key = raw_input('Введіть призвіще для внесення змін: ')
		if key in open_dict:
			key_dir = open_dict[key]
			key_dir['name'] = raw_input("Введіть інше ім'я: ")
			key_dir['mobil_nomer'] = int(raw_input("Введіть інший  номер телефону : "))
			key_dir['adresa'] = raw_input("Введіть іншу адресу: ")
			print(key_dir)
			print(open_dict)

			open_dict.update(open_dict)

		pikl_out.close()




		pikl_in = open('proba', 'wb')

		pickle.dump(open_dict, pikl_in)
	
		print(open_dict)

		pikl_in.close()

change()



def search():
	if litera.upper() == 'S':
		import pickle
		pikl_out = open('proba', 'rb')
		open_dict = pickle.load(pikl_out)
		print(open_dict)



		sou = raw_input('Введіть призвіще: ')

		if sou in open_dict:
			keys_dir = open_dict[sou]
			print('Призвіще: %s ' % sou)
			print('Імя: %s' % keys_dir['name'])
			print('Адреса: %s' %keys_dir['adresa'])
			print('Номер мобільного: %s' % keys_dir['mobil_nomer'])

search()
	


def empty_base():
	import pickle
	
	name1 = raw_input("Введіть призвіще: ")
	name2 = raw_input("Введіть ім'я: ")
	m_nomer = raw_input("Введіть Номер телефону : ")
	address = raw_input("Введіть адресу: ")
	
	d = {name1:{"name":name2, "mobil_nomer": m_nomer, "adresa": address}}
	pikl_in = open('proba', 'wb')
	pickle.dump(d, pikl_in)
	pikl_in.close()


def base_entry():
	import pickle
	pikl_out = open('proba', 'rb')
	open_dict = pickle.load(pikl_out)
	print(open_dict)


def delite():
	if litera.upper() == 'D':
		import pickle
		pikl_out = open('proba', 'rb')
		open_dict = pickle.load(pikl_out)
		print(open_dict)

		key = raw_input('Введіть призвіще дані якого ви хотіли б видалити: ')
		if key in open_dict:
		#dani = open_dict[key]
		#print(dani)
			del open_dict[key]
		

			open_dict.update(open_dict)

	
		pikl_out.close()



		pikl_in = open('proba', 'wb')

		pickle.dump(open_dict, pikl_in)
	
		print(open_dict)

		pikl_in.close()
		

delite()
