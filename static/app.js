const socket = io();

const taskForm = document.getElementById("taskForm");

taskForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    const title = document.getElementById("title").value;

    const description = document.getElementById("description").value;

    const priority = document.getElementById("priority").value;

    const status = document.getElementById("status").value;

    const response = await fetch("/api/tasks", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            title,
            description,
            priority,
            status
        })
    });

    const data = await response.json();

    socket.emit("task_update", data);

    window.location.reload();
});


socket.on(
    "receive_task_update",
    (data) => {

        console.log(
            "Real-time update:",
            data
        );
    }
);

async function deleteTask(taskId) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this task?"
    );

    if (!confirmDelete) {
        return;
    }

    const response = await fetch(
        `/api/tasks/${taskId}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    alert(data.message);

    window.location.reload();
}

async function updateTask(taskId) {

    const title = document.getElementById(
        `title-${taskId}`
    ).value;

    const description = document.getElementById(
        `description-${taskId}`
    ).value;

    const priority = document.getElementById(
        `priority-${taskId}`
    ).value;

    const status = document.getElementById(
        `status-${taskId}`
    ).value;

    const response = await fetch(
        `/api/tasks/${taskId}`,
        {
            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                title,
                description,
                priority,
                status
            })
        }
    );

    const data = await response.json();

    alert(data.message);

    window.location.reload();
}