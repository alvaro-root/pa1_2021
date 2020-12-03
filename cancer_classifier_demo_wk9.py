"""Classifier for a sample breast cancer dataset
See the accompanying PDF on Brightspace for a diagram representing the process described in this example.

This example is further elaborated in Chapter 10 of Punch & Enbody.

There are many datasets available to anyone for the purpose of data analysis. One such is a dataset of breast cancer
biopsy data from the University of California-Irvine. The original source is from University of Wisconsin Hospitals in
Madison, Wisconsin.

The problem is to determine, based on tumour attributes, whether the tumour is benign or malignant. The data lists about
699 patients with nine tumour attributes for each as well as a result, determined by an oncologist, stating whether the
tumour was benign or malignant.

Thus, for each patient, we have 11 data elements - an ID, nine tumour attributes and a result (4 =benign, 2 = malignant).

By examining the data, we hope to 'predict' based on the attributes alone whether a tumour is benign or malignant. As we
already know the result we can check the quality of our algorithm so that we might usefully apply it to data where we
don't know the result in advance.

Approach: Classification
A classifier begins by training on examples with known solutions. In training, a classifier looks for patterns that
indicate classification. After patterns have been identified, they are tested against "new" examples with known
classification.

Process overview
1. Create training set from data
2. Create classifier using training dataset to determine separator values for each attribute
3. Create test dataset
4. Use classifier to classify data in test set while maintaining accuracy score

Each data row consists of a patient id followed by nine indicators followed by an overall result. 
Sample data row: '1000025','5','1','1','1','2','1','3','1','1','2'. In this case '1000025 is the patient id and the
overall result is indicated as '2' - benign or '4' - malignant.
"""

DATA_URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"

## PERCENT is somewhat arbitrary. We can change this training/test data split to see if the outcome changes.
PERCENT = 75

from read_from_file_and_net import get_file_from_net as read_url


def get_data(url):
    '''
    Here we read our data file directly from the web and split it out into a list of tuples, one tuple per record.

    We do some conversion of factors from string to int and a malignant/benign code, '2'/'4' to 'b'/'m' respectively.
    We also test for value errors and silently drop any malformed rows.
    '''
    bad_records = 0
    cleaned_dataset = []

    data = read_url(url)
    data = data.split("\n")

    for record in data:
        try:
            record = record.strip().split(",")
            if not record:
                raise ValueError("Empty Record")
            for i in range(1, len(record) - 1):
                record[i] = int(record[i])
            if record[-1] == '2':
                record[-1] = 'm'
            elif record[-1] == '4':
                record[-1] = 'b'
            else:
                raise ValueError("b/m status is undefined")
            cleaned_dataset.append(tuple(record))
        except ValueError as val_err:
            bad_records += 1
            print(f"Record {record[0]} rejected: {val_err}")
            continue

    return tuple(cleaned_dataset)


def create_classifier(training_dataset):
    '''For each record we average the values for each attribute in a list of known benign results and, separately, a
    list of known malignant results. The benign and malignant averages are then averaged against each other to
    compute midpoint values. These will be used to compare each attribute in a record and assign it a status -
    benign or malignant. The overall result is the greater of the number of the benign / malignant status values.
    '''
    benign_attributes = [0] * 9
    malignant_attributes = [0] * 9
    benign_count = 0
    malignant_count = 0
    classifier_mid_points = [0] * 9

    # Compute the totals for each factor
    for record in training_dataset:
        if record[-1] == 'b':
            benign_count += 1
            for attribute in range(len(record[1:-1])):
                benign_attributes[attribute] += record[attribute + 1]
        elif record[-1] == 'm':
            malignant_count += 1
            for attribute in range(len(record[1:-1])):
                malignant_attributes[attribute] += record[attribute + 1]

    # Compute the average values for each factor
    for attribute in range(len(benign_attributes)):
        benign_attributes[attribute] = benign_attributes[attribute] / benign_count
    for attribute in range(len(malignant_attributes)):
        malignant_attributes[attribute] = malignant_attributes[attribute] / malignant_count

    # Compute the midpoints - the average of the benign & malignant factors in each case
    for attribute in range(len(classifier_mid_points)):
        classifier_mid_points[attribute] = (benign_attributes[attribute] + malignant_attributes[attribute]) / 2

    print(f"Classifier values\n{'-' * 50}")
    for item in classifier_mid_points:
        print(f"{item:.4f}", end=", ")
    print("\n")

    return tuple(classifier_mid_points)




def test_classifier(testing_dataset, classifier_mid_points):
    pass


def main():
    # Make a tuple of tuples from the raw data (a spreadsheet-like 2D array)
    cleaned_dataset = get_data(DATA_URL)

    # Break out our dataset into a training and test sets where the training set has a number of records determined
    # by the PERCENT value. The test set has the remaining records.
    training_dataset = cleaned_dataset[:int(len(cleaned_dataset) * PERCENT / 100)]
    test_dataset = cleaned_dataset[int(len(cleaned_dataset) * PERCENT / 100):]

    # Create the classifier values
    classifier_mid_points = create_classifier(training_dataset)

    # Apply classifier against test file.
    # Given that we know the outcome for each test record we can verify the classifier
    test_classifier(test_dataset, classifier_mid_points)


if __name__ == "__main__":
    main()
