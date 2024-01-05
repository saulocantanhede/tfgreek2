from tf.advanced.app import App
from tf.advanced.display import displaySetup

class TfApp(App):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def Viewtype(app,ViewName):
        if ViewName=='wg':
           OptionDict = {'hiddenTypes' : 'clause,phrase,subphrase', 'extraFeatures' : {'wg:subjrefspec','referent','id','framespec','word:type','gloss'}, 'condensed': {True}, 'queryFeatures': {False}, 'suppress' : {'book','chapter','verse'}}
           displaySetup(app,**OptionDict)
           print ('setup for wg-view')
        if ViewName=='syntax':
           OptionDict = {'hiddenTypes' : 'wg,subphrase', 'extraFeatures' : {'gloss','appositioncontainer','rela'}, 'condensed': {True}, 'queryFeatures': {False}, 'suppress' : {'book','chapter','verse','phrase:gloss'} }
           displaySetup(app,**OptionDict)
           print ('setup for syntax-view')
