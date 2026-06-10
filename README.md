# CryptoPulse 📈

An end-to-end Machine Learning pipeline for financial time-series prediction, built from scratch with PyTorch.

## Architecture
1. **Data Generation:** Synthetic market simulation (Pandas/NumPy).
2. **Feature Engineering:** SMA crossovers and momentum indicators.
3. **Storage:** Local SQLite database integration.
4. **Deep Learning Engine:** Multi-Layer Perceptron (MLP) built with PyTorch.

## Installation & Usage
1. Clone the repository: `git clone https://github.com/Zetifex/CryptoPulse.git`
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install torch pandas numpy matplotlib`
4. Run the data pipeline: `python data_blacksmith.py`
5. Train the model: `python engine.py`
