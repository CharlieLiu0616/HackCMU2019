import matplotlib.pyplot as plt
import pandas
import math
import numpy
import os
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import csv
numpy.random.seed(7)

one_year = 100

def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)
def predict(csv_name, endDate):
    #adjusting for end date to actual day
    endDate += 2
    endDate += one_year
    ##Manipulating data into dataset
    dataframe = pandas.read_csv(os.path.join("CSVs",csv_name), usecols=[1], engine='python')
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)
    
    ##Adjusting the training set and testing set
    train_size = endDate
    test_size = 4
    train, test = dataset[0:train_size,:], dataset[train_size-2:train_size+test_size-2,:]
    
    look_back = 1
    
    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)
    
    
    
    # reshape input to be [samples, time steps, features]
    trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    
    
    model = Sequential()
    model.add(LSTM(4, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
    
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)
    # invert predictions
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    testY = scaler.inverse_transform([testY])
    # calculate root mean squared error
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
    print('Test Score: %.2f RMSE' % (testScore))
    
    # trainPredictPlot = numpy.empty_like(dataset)
    # trainPredictPlot[:, :] = numpy.nan
    # trainPredictPlot[look_back-1:len(trainPredict)+look_back-1, :] = trainPredict
    # shift test predictions for plotting
    # testPredictPlot = numpy.empty_like(dataset)
    # testPredictPlot[:, :] = numpy.nan
    print("Test predict", testPredict)
    
    # testPredictPlot[len(trainPredict):len(trainPredict) + len(testPredict), :] = testPredict
    # plot baseline and predictions
    # plt.plot(scaler.inverse_transform(dataset[0:len(trainPredict)+len(testPredict)]))
    # plt.plot(trainPredictPlot)
    # plt.plot(testPredictPlot)
    print("Actual", scaler.inverse_transform(dataset[len(trainPredict)-1:len(trainPredict)+len(testPredict)]))
    print("Last day on train", trainPredict[-1])
    # plt.show()
    return testPredict[0] - trainPredict[-1]

def compileCSV(csv_file):
    fields = ['Date', 'predict']
    rows = []
    for i in range(1,31):
        row = [i,predict(csv_file, i).item(0)]
        rows.append(row)
    filename = os.path.join("result",csv_file)
    with open(filename, 'w') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        # writing the fields 
        csvwriter.writerow(fields) 
        # writing the data rows 
        csvwriter.writerows(rows)
    
def wrapper():
    compileCSV("msft.csv")
    compileCSV('FLEX.csv')
    compileCSV('BBBY.csv')
    compileCSV('ACAD.csv')
    compileCSV('CTAS.csv')
    compileCSV('CSGS.csv')
    compileCSV('CSCO.csv')
    compileCSV('DXLG.csv')
    compileCSV('ACHC.csv')
    compileCSV('ABCB.csv')

wrapper()
