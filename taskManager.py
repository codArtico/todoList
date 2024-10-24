from BDManager import *

class TaskManager:
    def __init__(self):
        self.db_manager = BDManager()
        self.db_manager.connect()

    def addTask(self, description):
        # Consulta o último ID na tabela de tarefas
        query = "SELECT MAX(id) FROM tasks"
        cursor = self.db_manager.connection.cursor()
        cursor.execute(query)
        last_id = cursor.fetchone()[0]
        
        # Se não houver tarefas, inicia o ID em 1
        new_id = (last_id + 1) if last_id is not None else 1

        # Insere a nova tarefa com o novo ID
        insert_query = "INSERT INTO tasks (id, description) VALUES (%s, %s)"
        cursor.execute(insert_query, (new_id, description))
        self.db_manager.connection.commit()
        cursor.close()


    def concluirTask(self, task_id, completed):
        try:
            query = "UPDATE tasks SET completed = %s WHERE id = %s"
            cursor = self.db_manager.connection.cursor()
            cursor.execute(query, (completed, task_id))
            self.db_manager.connection.commit()
        except Exception as e:
            print(f"Erro ao atualizar tarefa: {e}")
        finally:
            cursor.close()

    def deleteTask(self, task_id):
        query = "DELETE FROM tasks WHERE id = %s"
        cursor = self.db_manager.connection.cursor()
        cursor.execute(query, (task_id,))
        self.db_manager.connection.commit()
        cursor.close()
        self.atualizarIDs()

    def getTasks(self):
        query = "SELECT * FROM tasks"
        cursor = self.db_manager.connection.cursor()
        cursor.execute(query)
        tasks = cursor.fetchall()
        cursor.close()
        return tasks
    
    def atualizarIDs(self):
        # Atualiza os IDs das tarefas restantes
        cursor = self.db_manager.connection.cursor()

        # Inicializa a variável
        cursor.execute("SET @count = 0;")
        
        # Atualiza os IDs
        cursor.execute("UPDATE tasks SET id = (@count := @count + 1);")

        self.db_manager.connection.commit()
        cursor.close()