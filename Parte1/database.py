import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''




class Database:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(name +'.db')
        self.conn.execute("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,title TEXT,content TEXT NOT NULL);")

    def add(self,note):
        self.conn.execute(f"INSERT INTO note (title,content) VALUES ('{note.title}','{note.content}');")
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id,title, content FROM note")
        lista_note=[]
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content=linha [2]
            note=Note(id,title,content)
            lista_note.append(note)
        return lista_note

    def get(self,id):
        cursor = self.conn.execute(f"SELECT title, content FROM note WHERE id = '{id}'")

        for i in cursor:
            card=Note(id,i[0],i[1])
        return card
            
    def update(self,entry: Note):
        self.conn.execute(f"UPDATE note SET title= '{entry.title}',content='{entry.content}' WHERE id ='{entry.id}'")
        self.conn.commit()

    def delete(self,note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = '{note_id}'")
        self.conn.commit()



        
        