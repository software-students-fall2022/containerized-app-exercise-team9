def handle(doc):
    data = []
    misc = ["screen_text", "ouput_text", "_id", "time_created"]
    for prop in doc: 
        if (prop in misc):
            string = doc[prop]
            data.append(string)
        else:
            num = (round(float(doc[prop]),2))
            data.append(num)


    print(type(data[1]) == str)

    return data