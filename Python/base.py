import pandas as pandas

def get_data():
    data = pandas.read_csv('data.csv')
    return data

def get_question():
    data = get_data()
    question = data['question']
    return question

def get_answer():
    data = get_data()
    answer = data['answer']
    return answer

def get_answer_by_question(question):
    data = get_data()
    answer = data.loc[data['question'] == question, 'answer'].values[0]
    return answer

def get_question_by_answer(answer):
    data = get_data()
    question = data.loc[data['answer'] == answer, 'question'].values[0]
    return question