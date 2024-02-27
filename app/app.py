from tf.advanced.app import App
from tf.advanced.display import displaySetup

class TfApp(App):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def Viewtype(app,viewName):
    """
    Configures and displays the Text-Fabric application with specified view options.

    Parameters:
        app (object): The Text-Fabric application instance.
        viewName (str): The name of the view type. Acceptable values are 'wg' and 'syntax'.

    The function sets the parameters 'condensed' and 'queryFeatures' to True and False respectively.
    It further updates some display configurations based on the chosen view:
       1. If 'wg' (word-group) is selected:
           - It hides the clause, phrase, and subphrase node types.
           - Displays the setup specific for the word-group view.
       2. If 'syntax' is selected:
           - It hides the word-group (wg) and subphrase types.
           - Displays the setup specific for the syntactic view.

    Returns:
       The function does not return any value, but modifies the application's state.
       It prints a setup confirmation to the console.

    Example Usage within Jupyter Notebook:
         A.Viewtype('wg')
         # note: here the A is TF's advanced API which is the implied object passed as argument 'app' to this function.
    """
        if ViewName=='wg':
           OptionDict = {'hiddenTypes' : 'clause,phrase,subphrase', 'condensed': {True}, 'queryFeatures': {False}}
           displaySetup(app,**OptionDict)
           print ('setup for wg-view')
        if ViewName=='syntax':
           OptionDict = {'hiddenTypes' : 'wg,subphrase', 'condensed': {True}, 'queryFeatures': {False}}
           displaySetup(app,**OptionDict)
           print ('setup for syntax-view')
