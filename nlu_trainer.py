from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter

def train (data, config, model_dir):
    training_data = load_data(data)
    configuration = RasaNLUConfig(config)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')

def run():
   interpreter = Interpreter.load('C:/Users/Inspiron/Desktop/Project8/rasa/rasa_files/models/default/chat')
   print(interpreter.parse('I want to order pizza'))
   #print(interpreter.parse(u'What is the reivew for the movie Die Hard?'))

if __name__ == '__main__':
    train('C:/Users/Inspiron/Desktop/Project8/rasa/rasa_files/training_data/ngo_format.json', 'C:/Users/Inspiron/Desktop/Project8/rasa/rasa_files/config/config.json', 'C:/Users/Inspiron/Desktop/Project8/rasa/rasa_files/models/default/')
    #run()