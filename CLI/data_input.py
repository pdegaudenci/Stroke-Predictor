from __future__ import print_function, unicode_literals
from collections.abc import Mapping
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from colorama import init, Back, Fore

from validations import AgeValidation, GlucoseValidation, HeightValidation, WeightValidation

class Enter_data():
    dictio={}
    ## CONSTANTES CON CADENAS DE PREGUNTAS AL USUARIO
    AGE =" Enter your age ( number between 0 and 99): "
    GENDER ="Enter your gender(Male or female): "
    HYPER="Enter if you have hypertension(Yes or no): "
    HEART_DISEASE = "Enter if you have heart_disease (Yes or no): "
    MARRIED= "Enter if you are married (Yes or no): "
    WORK_TYPE= "Enter your work type (government / self-employed / private / No Working): "

    RESIDENCE_TYPE= "Enter your residence type (urban or rural): "	
    GLUCOSE_LEVEL="Enter your glucose level ( number between 0 and 300): "
    SMOKER = "Enter your smoker status ( never /  formerly / smokes): "
    PESO =" Enter your weight(Kg)"
    ALTURA ="Enter your height(cm)"
    QUESTIONS_COMP= "A continuacion, queremos realizarte una serie de preguntas complementarias, \n a fin de que nos puedas ayudar a mejorar nuestro modelo predictivo. \n Ademas, en cualquiera de nuestras preguntas, tendras la opcion de no contestar.\n "

    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    def show_title(self,message):
        print()
        init()
        print(Back.LIGHTBLUE_EX)
        print(Fore.RED)
        print(message)
        print(Back.BLACK)
        print(Fore.WHITE)

    def user_input(self):
        questions = [
        {
            'type': 'input',
            'name': 'age',
            'message': self.AGE,
            'validate': AgeValidation,
        },

        {
            'type': 'list',
            'name': 'gender',
            'message': self.GENDER,
            'choices': ["Male","Female"],
        },

        {
            'type': 'input',
            'name': 'avg_glucose_level',
            'message':self.GLUCOSE_LEVEL,
            'validate': GlucoseValidation,
        },
     {
            'type': 'input',
            'name': 'weight',
            'message': self.PESO,
            'validate': HeightValidation,
        },
        {
            'type': 'input',
            'name': 'height',
            'message': self.ALTURA,
            'validate': WeightValidation,
        }
        ,
        {
            'type': 'list',
            'name': 'hypertension',
            'message':self.HYPER,
            'choices': ["Yes","No"],
        },
        {
            'type': 'list',
            'name': 'heart_disease',
            'message':self.HEART_DISEASE,
            'choices': ["Yes","No"],
        },
         {
            'type': 'list',
            'name': 'ever_married',
            'message':self.MARRIED,
            'choices': ["Yes","No"],
        },
        {
            'type': 'list',
            'name': 'work_type',
            'message':self.WORK_TYPE,
            'choices': ["Government","Self-employed","Private","No Job"],
        },
        {
            'type': 'list',
            'name': 'Residence_type',
            'message':self.RESIDENCE_TYPE,
            'choices': ["Urban","Rural"],
        },
        {
        'type': 'list',
        'name': 'smoking_status',
        'message':self.SMOKER,
        'choices': ["Never","Formerly","Smokes"],
        }
        ]
        answers = prompt(questions, style=self.style)
        self.dictio = answers
        return (self.dictio)

    def additional_questions(self):
        compl=[
    'Have you suffered an ictus?',
    'Have you suffered loss of sensibility in one of the two sides of your face?',
    'When you smile the left or right side of your mouth does not move?',
    'Have you felt tingling in your face?',
    'Do you find difficult to articulate words?',
    'Raise your arms in front of you. Has one of your arms been lower than the other or one of your arms falls down?'
    'Have you had a sudden loss of vision?',
    'Do you lose vision in one or both eyes for moments?',
    'Do you suffer from migraines?',
    'Do you have difficult walking or have imbalance?',
    'Do you have a family history of stroke(Father/Mother)?',
    'Have you suffer sudden memory loss?',
    'Have you started with menopause?',
    'Are you on birth control?',
    ]
  
        questions  = [
            {
            'type': 'list',
            'name': 'ictus',
            'message': compl[0],
            'choices': ["Yes","No","No answer"],
        },

        {
            'type': 'list',
            'name': 'face_sensibility_loss',
            'message': compl[1],
            'choices': ["Yes","No","No answer"],
        },
        {
            'type': 'list',
            'name': 'immobilized_part_face',
            'message': compl[2],
            'choices': ["Yes","No","No answer"],
        },
        {
            'type': 'list',
            'name': 'tingling_face',
            'message': compl[3],
            'choices': ["Yes","No","No answer"],
        },
        {
            'type': 'list',
            'name': 'speech_difficulty',
            'message': compl[4],
            'choices': ["Yes","No","No answer"],
        },
        {
            'type': 'list',
            'name': 'personal_stroke_test',
            'message': compl[5],
            'choices': ["success","failed","No answer"],
        },
        {
            'type': 'list',
            'name': 'sudden_vision_loss',
            'message': compl[6],
            'choices': ["Yes","No","No answer"],
        },
         {
            'type': 'list',
            'name': 'vision_loss',
            'message': compl[7],
            'choices': ["Yes","No","No answer"],
        },
          {
            'type': 'list',
            'name': 'migraines',
            'message': compl[8],
            'choices': ["Yes","No","No answer"],
        },
          {
            'type': 'list',
            'name': 'family_history_stroke',
            'message': compl[9],
            'choices': ["Father","Mother","No history","No answer"],
        },
        {
            'type': 'list',
            'name': 'sudden_memory_loss',
            'message': compl[10],
            'choices': ["Yes","No","No answer"],
        },
        ]
        

        print()
        self.show_title(self.QUESTIONS_COMP)
        print()
        confirmation = prompt([{
            'type': 'list',
            'name': 'confirmation_comp_questions',
            'message': 'Quieres contestar la encuesta (Yes/No)?',
            'choices': ["Yes","No"],
        }],style=self.style)
        if confirmation['confirmation_comp_questions']== 'Yes':
            if self.dictio =='Female':
                questions.append({
            'type': 'list',
            'name': 'menopausic',
            'message': compl[10],
            'choices': ["Yes","No","No answer"],
            },
            {
            'type': 'list',
            'name': 'contraceptives',
            'message': compl[10],
            'choices': ["Yes","No","No answer"],
            },
            )
            answers = prompt(questions, style=self.style)
            if self.dictio == 'Male':
                answers['menopausic'] = 'No apply'
                answers['contraceptives'] = 'No apply'
            return (answers)
        return None


