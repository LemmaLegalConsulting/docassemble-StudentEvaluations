from docassemble.base.core import DAObject, DAList
from docassemble.base.util import today, Person, Individual
import datetime
import dateutil

def evaluation_list_populator(*evaluations):
  populated_evaluations_list = []
  for evaluation in evaluations:
    if evaluation == True:
      populated_evaluations_list.append(evaluation)
  return populated_evaluations_list
      
class Evaluation(DAObject):
    """Represents a particular educational evaluation that may be
        requested by a requestor."""

    def __init__(self, variable, name, requested=False, accepted=True, date_of_evaluation=today()):
            super(Evaluation, self).init(self, variable, name, requested=False, accepted=True, date_of_evaluation=today())

    def types_of_evaluation():
        return [
                {'variable': 'educational_assessment', 'name': 'educational assessment'}, 
                {'variable': 'speech_and_language_therapy', 'name': 'speech and language therapy, including a pragmatic language evaluation/and a functional language assessment'},
                {'variable': 'occupational_therapy', 'name': 'occupational therapy'},
                {'variable': 'functional_behavior_assessment', 'name': 'functional behavior assessment'},
                {'variable': 'psychological_assessment', 'name': 'psychological assessment'},
                {'variable': 'neuropyschological_assessment', 'name': 'neuropsychological assessment'},
                {'variable': 'physical_therapy', 'name': 'physical therapy'}, 
                {'variable': 'augmentative_and_alternative_communication', 'name': 'Augmentative and Alternative Communication'},
                {'variable': 'transition_assessment', 'name': 'transition assessment'},
                {'variable': 'assistive_technology', 'name': 'Assistive Technology'},
                {'variable': 'home_assessment', 'name': 'Home Assessment'}
                ]

    def evaluation_naming_function(self):
        """ fuction takes an EvaluationList as a singular argument, specifically the requested_evaluations returned by evaluation_list_populator(). 
        Is returning self the right approach here, or should there be another argument? """
        types_of_evaluation = Evaluation.types_of_evaluation()
        for item in self:
            item = Evaluation()
            item.requested = True
            item.variable = str(item)
            if str(item) in types_of_evaluation.values():
                item.name = types_of_evaluation[types_of_evaluation.index(item)]['name']
        return self

    
        
class EvaluationList(DAList):
    """A DAList of Evaluation objects. Is returning self the right approach here, or should there be another argument?"""
    def __init__(self, *pargs, **kwargs):
        super(EvaluationList, self).init(*pargs, **kwargs)
        self.auto_gather = False
        self.gathered = True
        self.set_random_instance_name()

    def evaluation_requested(self):
        for item in self:
            item.requested = True

    def latest_date_in_list(self):
        sorted(self, reverse=True)
        return self[0]

        """Use the gathering methods of docassemble to create a list the consits of all of the "variable" values
        in types_of_evaluation. Each of these variable values will have a value of True or False, based on checkboxes. If the value True, that variable value goes into a 
        new list of requested_evaluations. You then feed this requested_evaluations list into the evaluation_naming_function."""
   