import pandas as pd

def checkSubmission(path):
    data = pd.read_csv(path,sep=",")
    columnNames = list(data.columns.values)
    if "targets" != columnNames[1] or "id" != columnNames[0]:
        raise ValueError("Ensure that first column is named 'id' and the second column is name 'targets'!")
    preds = list(data['targets'])
    ids = list(data['id'])
    if len(ids) != 50 or len(preds) != 50:
        raise ValueError("Ensure that all samples are contained in your file!")
    print ("All formatted correctly")
        
if __name__ == "__main__":
    checkSubmission("predictions.csv") 
    '''
    change to your actual file! Note that the expected format is: "predictions_{name}_{matrikelnummer}"
    example: "predictions_John_Wayne_1029591"
    all files that cannot be evaluated automatically will be ignored and treated as not submitted!
    '''