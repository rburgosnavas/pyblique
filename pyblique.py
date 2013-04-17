#!/usr/bin/python3.3

'''
Created on Apr 14, 2013

@author: roberto
'''
import sqlite3 as sql, random as rand, subprocess as sub, platform

# load strategies from file
def load():
    oblique = open('oblique', 'r')
    oblique_list = oblique.readlines()
    oblique.close()
    return oblique_list

# drop the table
def drop():
    conn = sql.connect('oblique.db')
    cursor = conn.cursor()
    cursor.execute("drop table strategies")
    conn.commit()
    cursor.close()

# create the table
def create():
    conn = sql.connect('oblique.db')
    cursor = conn.cursor()
    cursor.execute("create table strategies (id integer primary key autoincrement, strategy text)")
    conn.commit()
    cursor.close()

# insert to table
def insert(oblique_list):
    conn = sql.connect('oblique.db')
    cursor = conn.cursor()
    for strategy in oblique_list:
        print(strategy.strip())
        cursor.execute("insert into strategies(strategy) values (?)", (strategy.strip(), ))    
    conn.commit()
    cursor.close()

# execute sqlite commands    
def execute():
    create()
    oblique_list = load()
    insert(oblique_list)

# get random strategy from db    
def get_strategy():
    strategy_id = rand.randint(1,195)
    conn = sql.connect('oblique.db')
    cursor = conn.cursor()
    cursor.execute("select strategy from strategies where id = (?)", (strategy_id,))
    strategy = cursor.fetchone()[0]
    cursor.close()
    return strategy

# clears the terminal screen before printing strategy
def clear():
    sub.Popen("cls" if platform.system() == "Windows" else "clear", shell=False)

# print a line of stars that's 6 stars longer than the length of the text
def print_star_line(text):
    for i in range(len(text) + 6):
        print("*", end='')

# print strategy text with a frame of stars around it just to make it pretty
def print_strategy(strategy):
    print("\n")
    print_star_line(strategy)
    print("\n*  " + strategy + "  *")
    print_star_line(strategy)
    print("\n")

# main
def main():
    clear()
    print_strategy(get_strategy())
    
# execute()

if __name__ == '__main__':
    main()

