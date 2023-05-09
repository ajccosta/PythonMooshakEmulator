# -*- coding: utf-8 -*-
#This is an example program
"""
Created on Tue Nov 5 10:18:07 2019
Changed on Wed Nov 9 2022

@author: Miguel Goulao
"""

#######################################
# Para o lab 14 exercicio 1 - mooshak #
#######################################

def new_database():
    return {}

def add_entry(name, country, year, database):
    entry = (country, year)
    if name not in database.keys():
        database[name] = []
    database[name].append(entry)

def trips_by(name, database):
    trips=0
    for i in database[name]:
        trips=trips+1
    return trips

def visited_countries(name, database):
    lista=[]
    for viagem in database[name]:
        if viagem not in lista:
            lista.append(viagem)      
    return lista
    
def visited_countries_in_interval(name, start_year, end_year, database):
    lista=[]
    if name not in database:
        lista=[]
    else:
        for v in database[name]:
            if start_year<=v[1]<=end_year:
               lista.append(v[0])
    return lista

    
def top_travellers(database):
    top=[]
    for name in database.keys(): #se pusesse so database era igual
      if top==[] or len(database[top[0]])<len(database[name]):
        top=[name]
      elif len(database[top[0]])==len(database[name]):
        top.append(name)
    lista=[]
    for nome in top:
        lista.append((nome,database[nome]))
    return lista
    

#############################
# Interpretador de comandos #
#############################
    
def next_command():
    return input("Introduza um novo comando: ")

def add_new_trip(database):
    name = input("Nome: ")
    country = input("Pais: ")
    year = int(input("Ano: "))
    add_entry(name, country, year, database)

def print_all(database):
    if len(database) > 0:
        sorted_keys = sorted(database.keys())
        for key in sorted_keys:
            print (key)
            print (sorted(database[key]))
    else:
        print ("Nao ha registos.")

def how_many_trips_by_traveller(database):
    name = input("Nome: ")
    print(trips_by(name, database), "viagens.")
    
def list_countries_visited_by_traveller(database):
    name = input("Nome: ")
    print(sorted(visited_countries(name, database)))
    
def list_countries_visited_by_traveller_in_interval(database):
    name = input("Nome: ")
    start_year = int(input("Ano inicial: "))
    end_year = int(input("Ano final: "))
    print(sorted(visited_countries_in_interval(name, start_year, end_year, database)))

def list_top_travellers(database):
    print(sorted(top_travellers(database)))
    
######################################
# Comandos para o lab 14 exercicio 2 #
######################################
    


####################################################
# Comandos auxiliares do Interpretador de comandos #
####################################################


##############################################
# Fim dos comandos para o lab 14 exercicio 2 #
##############################################
    
#############################
# Interpretador de comandos #
#############################
    
def main():
    database = new_database()
    command = next_command()
    while command != "SAIR":
        if command == "NB":
            database = new_database()
        elif command == "NV":
            add_new_trip(database)
        elif command == "LV":
            print_all(database)
        elif command == "QVP":
            how_many_trips_by_traveller(database)
        elif command == "LVP":
            list_countries_visited_by_traveller(database)
        elif command == "LVPI":
            list_countries_visited_by_traveller_in_interval(database)
        elif command == "RV":
            list_top_travellers(database)
        ####################################
        # Opcoes para o lab 14 exercicio 2 #
        ####################################

        ############################################
        # Fim das opcoes para o lab 14 exercicio 2 #
        ############################################
        else:
            print("Comando desconhecido.")
        command = next_command()

    print ("Obrigado!")

######################
# Programa principal #
######################

main()
