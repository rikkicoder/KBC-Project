import json
import mysql.connector

# MySQL connection configuration
config = {
    'user': 'root',
    'password': 'Hadwik@2006',   # Update with your credentials
    'host': '127.0.0.1',
    'database': 'kbc_game'
}

# Connect to MySQL
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def insert_questions(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        questions = data.get('results', [])
        for q in questions:
            question = q.get('question')
            difficulty = q.get('difficulty')
            category = q.get('category', '')
            correct_answer = q.get('correct_answer')
            # Convert the list of incorrect answers to a JSON string
            incorrect_answers = json.dumps(q.get('incorrect_answers'))
            
            query = """
                INSERT INTO questions (question, difficulty, category, correct_answer, incorrect_answers)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (question, difficulty, category, correct_answer, incorrect_answers))
    cnx.commit()


insert_questions('questions/easy.json')
insert_questions('questions/medium.json')
insert_questions('questions/hard.json')


cursor.close()
cnx.close()

print("Questions inserted successfully.")
