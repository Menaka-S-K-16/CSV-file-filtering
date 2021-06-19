from flask import Flask,render_template,request,session
import pandas as pd

app=Flask(__name__)
app.secret_key="jnvkjhflddfbsjk"

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/index1",methods=["GET","POST"])
def index1():
    session['file_path']=request.form.get("csvFileInput")
    dataset=pd.read_csv(session['file_path'])
    dataset1=dataset.to_dict()
    datasetkeys=dataset1.keys()
    keys_list=[]
    for k in datasetkeys:
        keys_list.append(k)
    session['keys']=keys_list
    datasetvalues=dataset1.values()
    dataset_list=list(range(len(dataset[1:])))
    list1=[]
    for y in datasetvalues:
        list1.append(y)
    return render_template("index.html",dataset_keys=datasetkeys,dataset_values=datasetvalues,dataset_list=dataset_list,len_values=list1)

@app.route("/sort",methods=["GET","POST"])
def sort():
    error=""
    ord_bool=False
    try:
        sorted_dataset=pd.read_csv(session['file_path'])
        sorted_dataset['index_id']=list(range(sorted_dataset.shape[0]))
        keys=session['keys']
        cols=request.form.get('col')
        order=request.form.getlist('srt')
        if order==['asc']:
            ord_bool=True
        sorted_dataset1=sorted_dataset.sort_values(by=[cols],ascending=ord_bool)
        dataset_lists=list(sorted_dataset1['index_id'])
        lists=[]
        sorted_data_dict=sorted_dataset1.to_dict()
        sv=sorted_data_dict.values()
        for s in sv:
            lists.append(s)
    except Exception:
        error+="Invalid Input" 
    finally:
        return render_template("sort.html",dataset_key=sorted_data_dict.keys(),dataset_value=sorted_data_dict.values(),dataset_lists=dataset_lists,len_valued=lists,err=error,keys=keys)

@app.route("/sort_page",methods=["GET","POST"])  
def sort_page():
    error=""
    keys1=session['keys']
    return render_template("sort.html",err=error,keys1=keys1)


