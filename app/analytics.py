import pandas as pd
import numpy as np

from app.models import Task


def generate_task_analytics(user_id):

    tasks = Task.query.filter_by(
        user_id=user_id
    ).all()

    task_data = []

    for task in tasks:

        task_data.append({
            "title": task.title,
            "status": task.status
        })

    if not task_data:

        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_percentage": 0
        }

    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    completed_tasks = np.sum(
        df["status"] == "Completed"
    )

    pending_tasks = np.sum(
        df["status"] == "Pending"
    )

    completion_percentage = (
        completed_tasks / total_tasks
    ) * 100

    return {
        "total_tasks": int(total_tasks),
        "completed_tasks": int(completed_tasks),
        "pending_tasks": int(pending_tasks),
        "completion_percentage": round(
            completion_percentage,
            2
        )
    }