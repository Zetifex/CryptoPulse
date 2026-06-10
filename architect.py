import torch
import torch.nn as nn

print("Milestone 4: Architect of DL")
# locking the randomness weight
torch.manual_seed(42)

# Build the blueprint
#define our mathematics parameters like gradient descent
class TrendPredictor(nn.Module):
    #define each layer
    def __init__(self):
        # it starts the engine
        super(TrendPredictor, self).__init__()
        #Layer1: now to build the Y=WX+B and define the inputs out features is the neurons
        self.layer1 = nn.Linear(in_features=2, out_features=16)
        self.layer2 = nn.Linear(in_features=16, out_features=8)
        #Layer2: activation function
        self.relu = nn.ReLU()
        #Layer3: The output
        self.output_layer = nn.Linear(in_features=8, out_features=1)
        #define the assembly of network
    def forward(self, x):
        #define the which parts of neurons must take the input
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.relu(x)
        predicted_price = self.output_layer(x)
        return predicted_price
# bring blue print to work
model = TrendPredictor()

print("\nModel Architecture Built Successfully:")
print(model) 

# --- THE DESTRUCTION TEST ---
# Create a fake day of data (1 row, 2 features: Short_MA and Long_MA)
dummy_input = torch.tensor([[1520.5, 1500.0]], dtype=torch.float32)

# Push the fake data through the network
test_prediction = model(dummy_input)

print(f"\nEngine Test Successful! The network predicted: {test_prediction.item():.2f}")
        
