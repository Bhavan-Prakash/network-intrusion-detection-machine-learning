train_main["Flow Byts/s"] = train_main["Flow Byts/s"].fillna(train_main["Flow Byts/s"].mean())
train_main.isnull().sum()


num_data = train_main.select_dtypes("number")
inf = np.isinf(num_data).sum()
inf


fill_inf_null = train_main.replace([np.inf,-np.inf],np.nan,inplace = True)
train_main.isnull().sum()


train_main["Flow Byts/s"] = train_main["Flow Byts/s"].fillna(train_main["Flow Byts/s"].mean())
train_main["Flow Pkts/s"] = train_main["Flow Pkts/s"].fillna(train_main["Flow Pkts/s"].mean())
train_main.isnull().sum()


train_main.info()


train_main["Timestamp"] = pd.to_datetime(train_main["Timestamp"], format = "%d/%m/%Y %H:%M:%S")
train_main["hour"] = train_main["Timestamp"].dt.hour
train_main["day"] = train_main["Timestamp"].dt.day
train_main["month"] = train_main["Timestamp"].dt.month
train_main["year"] = train_main["Timestamp"].dt.year


train_main.drop("Timestamp",axis=1,inplace=True)


from sklearn.preprocessing import OneHotEncoder
init = OneHotEncoder(sparse_output = False,handle_unknown="ignore")
Label_conversion = init.fit_transform(train_main[["Label"]]) #there are two[[]] for label because the one hot encoder takes 2d array as input

convert_dataframe = pd.DataFrame(Label_conversion,columns= init.get_feature_names_out(["Label"]))

train_main = pd.concat([train_main,convert_dataframe],axis=1)


train_main.drop("Label",axis=1,inplace=True)