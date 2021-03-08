def load_data(filename):
    """Read in all patient data from a certain format of .txt file

    load_data opens a given text file and create a list of patient with
    corresponding infomation such as first name, last name, age, gender,
    and TSH data.

    Args:
        filename (String): the name of the .txt file
    Returns:
        listOfpatients (List): list of patient objects
    """
    data_file = open(filename, "r")
    linenumber = 0
    listOfpatients = list()
    for eachline in data_file:
        if linenumber % 4 == 0:
            if eachline != "END":
                name_line = eachline.split(' ')
                first = name_line[0]
                last = name_line[-1]
        if linenumber % 4 == 1:
            age = eachline.rstrip()
        if linenumber % 4 == 2:
            gender = eachline.rstrip()
        if linenumber % 4 == 3:
            raw_data = eachline.split(",")
            tsh_data = raw_data[1:]
            for i in tsh_data:
                float(i)
            tsh_data = sorted(tsh_data)
            patient = create_patient(first, last, age, gender, tsh_data)
            listOfpatients.append(patient)
        linenumber += 1
    data_file.close()
    return listOfpatients


def create_patient(first, last, age, gender, tsh_data):
    """Create patients' objects

    Args:
        first (String): patient's first name
        last (String): patient's last name
        age (String): patient's age
        gender (String): patient's gender
        tsh_data (List): list of a string with a patient's all tsh data
    Returns:
        patient (Dict): A dictionary of a patient with all info
    """
    patient = {"First": first,
               "Last": last,
               "Age": age,
               "Gender": gender,
               "TSH Data": tsh_data}
    return patient


def diagnoseTSH(patient):
    """This function outputs if the patient has hyper/hypothyroidism or not.

    Args:
        patient (Dict): patient object containing various properties
    Returns:
        result (String): output string of diagnosis
    """
    if float(patient["TSH Data"][-1]) > 4:
        result = 'hypothyroidism'
    elif float(patient["TSH Data"][0]) < 1:
        result = 'hyperthyroidism'
    else:
        result = 'normal thyroid function'
    return result


def file_output(patient):
    """This function outputs into a json the patient information

    Args:
        patient (Dict): patient object containing various properties
    """
    import json
    outfile = open("{}-{}.json".format(patient["First"], patient["Last"]), "w")
    patient_dict = {}
    patient_dict["First Name"] = patient["First"]
    patient_dict["Last Name"] = patient["Last"]
    patient_dict["Age"] = patient["Age"]
    patient_dict["Gender"] = patient["Gender"]
    patient_dict["TSH"] = patient["TSH Data"]
    patient_dict["Diagnosis"] = patient["TSH Result"]
    json.dump(patient_dict, outfile)
    outfile.close()
    return


def main():
    listOfpatients = load_data("sample_data.txt")
    for patient in listOfpatients:
        result = diagnoseTSH(patient)
        patient["TSH Result"] = result
        file_output(patient)


if __name__ == "__main__":
    main()
