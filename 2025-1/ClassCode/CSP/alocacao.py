def is_valid(s,v,problem):

    aula = problem['aulas'][len(s)]
    prof = problem['constraints'][aula]['professor']
    horario = v[1]
    sala = v[0]
    capacidade = problem['salas'][sala]['capacidade']

    #v = (sala, horario)
        
    for a in s:
        # uma sala por horário
        if a['sala'] == sala and a['horario'] == horario:
            return False 

        # um professor só pode dar uma aula por vez
        profa = problem['constraints'][a['aula']]['professor']
        if profa == prof and  a['horario'] == horario:
            return False

    # capacida minima
    if capacidade < problem['constraints'][aula]['alunos']:
        return False

    # Sala específica
    sala_requerida = problem['constraints'][aula]['sala_requerida']
    if sala_requerida:
        if sala != sala_requerida:
            return False
    
    return True


if __name__ == '__main__':
    
    problem = {
    'aulas':['Aula1', 'Aula2', 'Aula3'],
    'dominios': {
    'Aula1': [('Sala1', '08h'), ('Sala1', '10h'), ('Sala2', '08h'), ('Sala2', '10h')],
    'Aula2': [('Sala1', '08h'), ('Sala1', '10h'), ('Sala2', '08h'), ('Sala2', '10h')],
    'Aula3': [('Sala1', '08h'), ('Sala1', '10h'), ('Sala2', '08h'), ('Sala2', '10h')]
    },
    'constraints':{
    'Aula1': {'professor': 'ProfA', 'alunos': 30, 'sala_requerida': None},
    'Aula2': {'professor': 'ProfB', 'alunos': 20, 'sala_requerida': 'Sala2'},
    'Aula3': {'professor': 'ProfA', 'alunos': 15, 'sala_requerida': None}
    },
    'salas': {
    'Sala1': {'capacidade': 40},
    'Sala2': {'capacidade': 25}
    }}


    s = [
        {'aula': 'Aula1', 'sala': 'Sala1', 'horario': '08h', 'professor': 'ProfA'},
        {'aula': 'Aula2', 'sala': 'Sala2', 'horario': '10h', 'professor': 'ProfB'},
        #{'aula': 'Aula3', 'sala': 'Sala1', 'horario': '14h', 'professor': 'ProfA'}
    ]

    
    for v in problem['dominios']['Aula3']:
        print(f'{v}  {is_valid(s,v,problem)}')