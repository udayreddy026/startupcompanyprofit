from pathlib import Path
from django.shortcuts import render
import pickle

file_dir = Path(__file__).resolve().parent.parent

def home(request):
    return render(request, 'index.html')


def result(request):

    load_model = pickle.load(open(str(file_dir) + "//ml_models/lr_final_model", 'rb'))

    r_d_spend = float(request.POST['R&DSpend'])
    Administration = float(request.POST['Administration'])
    MarketingSpend = float(request.POST['MarketingSpend'])
    State_Florida = float(request.POST['State_Florida'])
    State_NewYork = float(request.POST['State_NewYork'])

    profit_reslult = load_model.predict([[r_d_spend, Administration, MarketingSpend, State_Florida, State_NewYork]])

    final_res = profit_reslult[0,0]
    print(final_res)
    print(type(final_res))
    final_Res=format(final_res, '.2f')
    print(final_Res)
    print(file_dir)

    return render(request, 'index.html', {'res': final_Res})