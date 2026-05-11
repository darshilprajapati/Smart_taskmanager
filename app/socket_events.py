from flask_socketio import emit

from app import socketio


@socketio.on("task_update")
def handle_task_update(data):

    emit(
        "receive_task_update",
        data,
        broadcast=True
    )