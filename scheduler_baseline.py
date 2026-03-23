import random
from datetime import datetime, timedelta
import uuid

def generate_baseline_schedule(assignments):
    sessions = []

    for assignment in assignments:
        days_left = (assignment["due_date"] - datetime.now()).days
        days_left = max(days_left, 1)

        total_hours = assignment["estimated_time"]

        for _ in range(int(total_hours)):
            random_day = random.randint(0, days_left - 1)

            session = {
                "session_id": str(uuid.uuid4()),
                "assignment_id": assignment["assignment_id"],
                "scheduled_time": datetime.now() + timedelta(days=random_day),
                "duration": random.choice([30, 45, 60]),
                "status": "pending"
            }

            sessions.append(session)

    return sessions