from BDManager import *

class TaskManager:
    def __init__(self):
        self.db_manager = BDManager()
        self.db_manager.connect()

    def addTask(self, description):
        query = "INSERT INTO tasks (description) VALUES (%s)"
        cursor = self.db_manager.connection.cursor()
        cursor.execute(query, (description,))
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

    def getTasks(self):
        query = "SELECT * FROM tasks"
        cursor = self.db_manager.connection.cursor()
        cursor.execute(query)
        tasks = cursor.fetchall()
        cursor.close()
        return tasks
