def sdr(a,b,c): #función de prueba que sí funciona
    return (a+b)*c


def year(value):
    return (str(value))[0:4] # Lo convierto a str porque el dato es un float


def solo_digitos(value):
    if re.match(r'\d{4}', value):
        return value
    else:
        return "NoData"

def tipo(value):
    value = str(value)
    value = value.split(".")
    value = value[0]
    if len(value)!=4:
        return "NoData"
    else:
        return value

def date(value):
    if (len(value)==4) | (value=="NoData"):
        return value
    elif re.match(r'\d{4}\-\d{4}.*', value):
        value = value.split("-")
        value1 = value[0]
        value2 = value[1]
        value2 = re.search(r"^\d{4}", value2)
        value2 = value2.group()
        value = [int(value1),int(value2)]
        value_mean = int(sum(value)/len(value))
        return str(value_mean)
    elif re.search(r".*\d{4}.*", value):
            value = (re.search(r"\d{4}", value)).group()
            return value
    else:
        return "NoData"

def count_2(n,m):
    count=0
    for e in zip(n, m):
        if (e[0]!=e[1]): 
            count+=1
    return count

def count_3(a,b,c):
    count=0
    for e in zip(a,b,c):
        if (e[0]!=e[1]) | (e[0]!=e[2]) | (e[2]!=e[1]): 
            count+=1
    return count

def activ2(value):
    if (value!="Water sports") & (value!="NoData"):
        return "Others"
    else:
        return value