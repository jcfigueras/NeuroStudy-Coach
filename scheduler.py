import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# ---- Encode categorical inputs ----
task_types = ["reading", "writing", "problem_sets", "projects", "review"]
time_of_day_types = ["morning", "afternoon", "evening", "night"]

def encode_task(task):
    vec = [0]*len(task_types)
    vec[task_types.index(task)] = 1
    return vec

def encode_time(time):
    vec = [0]*len(time_of_day_types)
    vec[time_of_day_types.index(time)] = 1
    return vec


# ---- Neural Network ----
class NeuroStudyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(5 + 4 + 4, 128),  # task + time + numeric inputs
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1)  # output: predicted hours
        )

    def forward(self, x):
        return self.model(x)


# ---- Create synthetic training data ----
def generate_data(n=2000):
    X = []
    y = []

    for _ in range(n):
        task = np.random.choice(task_types)
        time = np.random.choice(time_of_day_types)

        baseline = np.random.uniform(0.5, 5.0)
        difficulty = np.random.randint(1, 6)
        interest = np.random.randint(1, 6)
        days = np.random.randint(1, 10)

        # --- "ground truth" formula (same logic as earlier model) ---
        difficulty_factor = 1 + (difficulty - 3) * 0.15
        interest_factor = np.clip(1 - (interest - 3) * 0.2, 0.5, 1.5)
        urgency_factor = 1 + (1 / days) * 0.5

        task_weight = {
            "reading": 0.9,
            "writing": 1.2,
            "problem_sets": 1.3,
            "projects": 1.5,
            "review": 0.8
        }[task]

        time_weight = {
            "morning": 1.0,
            "afternoon": 0.95,
            "evening": 1.1,
            "night": 1.2
        }[time]

        output = baseline * difficulty_factor * interest_factor * urgency_factor * task_weight * time_weight

        features = (
            encode_task(task) +
            encode_time(time) +
            [baseline, difficulty, interest, days]
        )

        X.append(features)
        y.append([output])

    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)


# ---- Train model ----
def train_model():
    model = NeuroStudyNet()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    X, y = generate_data(2000)

    for epoch in range(100):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

    return model


# ---- Predict function ----
def predict(model, task, baseline, difficulty, interest, days, time):
    features = (
        encode_task(task) +
        encode_time(time) +
        [baseline, difficulty, interest, days]
    )

    x = torch.tensor([features], dtype=torch.float32)
    prediction = model(x).item()
    return round(prediction, 2)


# ---- Run example ----
if __name__ == "__main__":
    model = train_model()

    result = predict(
        model,
        task="projects",
        baseline=3.0,
        difficulty=5,
        interest=4,
        days=2,
        time="night"
    )

    print(f"Predicted study time: {result} hours")