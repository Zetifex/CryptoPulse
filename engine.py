import sqlite3
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

print("===Mile stone 5: The Engine===")

class TrendPredictor(nn.Module):
    def __init__(self):
        super( TrendPredictor, self).__init__()
        self.layer1= nn.Linear(in_features=2 , out_features=16)
        self.layer2= nn.Linear(in_features=16 , out_features=8)
        self.relu= nn.ReLU()
        self.output_layer= nn.Linear(in_features=8 , out_features=1)
    
    def forward(self,x):
        x=self.layer1(x)
        x=self.relu(x)
        x=self.layer2(x)
        x=self.relu(x)
        predicted_price=self.output_layer(x)        
        return predicted_price

conn = sqlite3.connect('cryptopulse.db')
df = pd.read_sql("SELECT * FROM market_history",conn)
conn.close

# define the inputs and outputs

X = torch.tensor(df[['Short_MA' , 'Long_MA']].values , dtype=torch.float32)
Y = torch.tensor(df[['Close_Price']].values , dtype=torch.float32)

#Ignition of system by using model

model = TrendPredictor()
criterion = nn.MSELoss() # Mean squre
optimizer = optim.Adam(model.parameters() , lr=0.01)
# #loops
epochs = 1000

print("\nStarting Training....")

for epoch in range(epochs):
    #Forward path
    predictions = model(X)
    
    loss = criterion(predictions , Y)
    # clears last loop data
    optimizer.zero_grad()
    # backward prop and gradient descent
    loss.backward()
    
    optimizer.step()
    
    if epoch % 100 == 0:
        print(f"Epoch {epoch} | Loss(Error) : {loss.item(): 2f}")
        
print("\nTraining Complete! The network has learned the market gravity.")        
    