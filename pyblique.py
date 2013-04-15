#!/usr/bin/python3

'''
Created on Apr 14, 2013

@author: roberto
'''
import sqlite3 as sql, random as rand

def load():
    oblique = open('oblique', 'r')
    oblique_list = oblique.readlines()
    oblique.close()
    return oblique_list

def create():
    conn = sql.connect('oblique.db')
    cursor = conn.cursor()
    cursor.execute("create table strategies (id integer primary key autoincrement, strategy text)")
    conn.commit()
    cursor.close()

def insert(oblique_list):
    conn = sql.connect('oblique.db')
    cursor = conn.cursor()
    for strategy in oblique_list:
        print(strategy.strip())
        cursor.execute("insert into strategies(strategy) values (?)", (strategy.strip(), ))    
    conn.commit()
    cursor.close()
    
def execute():
    create()
    oblique_list = load()
    insert(oblique_list)
    
def get_strategy():
    strategy_id = rand.randint(1,195)
    conn = sql.connect('oblique.db')
    cursor = conn.cursor()
    cursor.execute("select strategy from strategies where id = (?)", (strategy_id,))
    strategy = cursor.fetchone()[0]
    cursor.close()
    return strategy

def print_star_line(text):
    for i in range(len(text) + 6):
        print("*", end='')

def print_strategy(strategy):
    print_star_line(strategy)
    print("\n** " + strategy + " **")
    print_star_line(strategy)

def main():
    print_strategy(get_strategy())
    
# execute()

if __name__ == '__main__':
    main()

