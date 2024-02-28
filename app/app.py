from tf.advanced.app import App
from tf.advanced.display import displaySetup

class TfApp(App):

    def viewtype(app,viewName):
        """
        Configures and displays the Text-Fabric application with specified view options.

        Parameters:
            app (object): The Text-Fabric application instance.
            viewName (str): The name of the view type. Acceptable values are 'wg' and 'syntax'.

        The function sets the parameters 'condensed' to True and 'queryFeatures' to False, respectively.
        It further updates some display configurations based on the chosen view:
           1. If 'wg' (word-group) is selected:
               - Updates the label for sentence nodes
               - It hides the clause, phrase, subphrase, and group node types.
           2. If 'syntax' is selected:
               - Updates the label for sentence nodes
               - It hides the word-group (wg) and subphrase types.
        Returns:
           The function does not return any value, but modifies the application's state.
           It prints a setup confirmation to the console.

        Example Usage within Jupyter Notebook:
             A.Viewtype('wg')

             note: here the A is TF's advanced API which is the implied object passed as argument 'app' to this function.
        """
        feedback='Display is setup for viewtype '
        if viewName=='wg':
           # modify some labels for sentence nodes (note: app.context.typeDisplay contains the data from config.yaml)
           app.context.labels['sentence'] = ('{rule}', ['rule'])
           # Each key-value pair in dictionary OptionDict represents a specific setting or option for the wg-view.
           OptionDict = {'hiddenTypes' : 'clause,phrase,subphrase,group', 'condensed': {True}, 'queryFeatures': {False}, 'suppress' : {''}}
           # Pass the dictionary (with a variable number of pairs) to the displaySetup function to unpack and apply.
           displaySetup(app,**OptionDict)
           feedback+='[wg-view](https://github.com/saulocantanhede/tfgreek2/blob/main/docs/wg-view.md#start)'

        if viewName=='syntax':
           # modify some labels for sentence nodes
           app.context.labels['sentence'] = ('{function}', ['function'])
           # Each key-value pair in dictionary OptionDict represents a specific setting or option for the syntax-view.
           OptionDict = {'hiddenTypes' : 'wg, subphrase', 'condensed': {True}, 'queryFeatures': {False},  'suppress' : {''}}
           # Pass a dictionary (with a variable number of pairs) to the displaySetup function to unpack and apply.
           displaySetup(app,**OptionDict)
           feedback+='[syntax-view](https://github.com/saulocantanhede/tfgreek2/blob/main/docs/syntax-view.md#start)'
        app.dm(feedback)

    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)
        app.viewtype('syntax')
        app.dm('See [here](https://github.com/saulocantanhede/tfgreek2/blob/main/docs/viewtypes.md#start) for more information on viewtypes')


