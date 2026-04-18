def day0():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelBinarizer, LabelEncoder

    test = pd.read_csv('test.csv')
    print(test.head())
    train = pd.read_csv('train.csv')
    sample = pd.read_csv('sample_submission.csv')
    print(train.head())

    def encode_object_cols(df):
        from sklearn.preprocessing import LabelEncoder
        for col in df.columns:
            if df[col].dtype == 'object':
                print(f"编码列: {col}, 值: {df[col].unique()[:5]}")
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col])
        return df

    x = train
    x = x.drop(['Fertilizer Name'], axis=1)
    y = train['Fertilizer Name']
    print(x.head())
    print(y.head())
    lb = LabelBinarizer()
    le = LabelEncoder()
    y = le.fit_transform(y)
    y_oh = lb.fit_transform(y)
    # y_oh = pd.DataFrame(y_oh)
    # print(y_oh.head())
    # y_origin = lb.inverse_transform(y_oh)##这个能将onehot原封不动变回原来的label，但会转向
    # print(y_origin)
    # import numpy as np
    # y_origin = np.array(y_origin)
    # y_origin = y_origin.reshape(y_origin.size,1)
    # print(y_origin[0])
    print(y_oh)
    y_name = [le.classes_[x] for x in range(len(y_oh[0]))]
    print(y_name)
    # encode_object_cols(y_oh)
    print(x.head())
    # le1 = LabelEncoder()
    # lb1 = LabelBinarizer()
    # x = le1.fit_transform(x)
    # x_oh = lb1.fit_transform(x)
    # x_name = [le1.classes_[i] for i in range(len(x_oh[0]))]
    x.columns = range(len(x.columns))
    print(x)
    x = x.drop([4, 5], axis=1)
    x.columns = range(len(x.columns))
    print(x)
    # print(x_oh.head())
    # print(x_name)
    model = RandomForestClassifier()
    x_train, x_test, y_train, y_test = train_test_split(x, y_oh, test_size=0.2)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    from sklearn.metrics import accuracy_score, mean_squared_error
    accuracy = accuracy_score(y_test, y_pred, normalize=True)
    print(accuracy)
def day1():
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelBinarizer, LabelEncoder
    ##从父文件导入方式
    import sys, os
    sys.path.append('..')
    import torch
    from main import MyClassifier  # 从父文件夹的main.py导入

    test = pd.read_csv('test.csv')
    print(test.head())
    train = pd.read_csv('train.csv')
    sample = pd.read_csv('sample_submission.csv')
    print(train.head())

    def encode_object_cols(df):
        from sklearn.preprocessing import LabelEncoder
        for col in df.columns:
            if df[col].dtype == 'object':
                print(f"编码列: {col}, 值: {df[col].unique()[:5]}")
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col])
        return df

    x = train
    x = x.drop(['Fertilizer Name'], axis=1)
    y = train['Fertilizer Name']
    print(x.head())
    print(y.head())
    lb = LabelBinarizer()
    le = LabelEncoder()
    y = le.fit_transform(y)
    y_oh = lb.fit_transform(y)
    # y_oh = pd.DataFrame(y_oh)
    # print(y_oh.head())
    # y_origin = lb.inverse_transform(y_oh)##这个能将onehot原封不动变回原来的label，但会转向
    # print(y_origin)
    # import numpy as np
    # y_origin = np.array(y_origin)
    # y_origin = y_origin.reshape(y_origin.size,1)
    # print(y_origin[0])
    print(y_oh)
    y_name = [le.classes_[x] for x in range(len(y_oh[0]))]
    print(y_name)
    # encode_object_cols(y_oh)
    print(x.head())
    # le1 = LabelEncoder()
    # lb1 = LabelBinarizer()
    # x = le1.fit_transform(x)
    # x_oh = lb1.fit_transform(x)
    # x_name = [le1.classes_[i] for i in range(len(x_oh[0]))]
    x.columns = range(len(x.columns))
    print(x)
    x = x.drop([4, 5], axis=1)
    x.columns = range(len(x.columns))
    print(x)
    # print(x_oh.head())
    # print(x_name)
    print(f"len：{len(x.columns)}")
    model = MyClassifier(input_size=len(x.columns), hidden_size=256, num_classes=len(y_oh[0]))
    x_train, x_test, y_train, y_test = train_test_split(x, y_oh, test_size=0.2)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    from sklearn.metrics import accuracy_score, mean_squared_error
    accuracy = accuracy_score(y_test, y_pred, normalize=True)
    print(accuracy)
day1()