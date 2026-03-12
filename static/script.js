const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTaskBtn");
const taskList = document.getElementById("taskList");

async function fetchTasks() {
    const response = await fetch("/api/tasks");
    const tasks = await response.json();
    renderTasks(tasks);
}

function renderTasks(tasks) {
    taskList.innerHTML = "";

    if (tasks.length === 0) {
        taskList.innerHTML = "<li>No tasks yet. Add one above.</li>";
        return;
    }

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.className = "task-item";

        li.innerHTML = `
            <span class="task-title ${task.done ? "done" : ""}">${task.title}</span>
            <div class="actions">
                <button class="complete-btn" onclick="toggleTask(${task.id})">
                    ${task.done ? "Undo" : "Done"}
                </button>
                <button class="delete-btn" onclick="deleteTask(${task.id})">Delete</button>
            </div>
        `;

        taskList.appendChild(li);
    });
}

async function addTask() {
    const title = taskInput.value.trim();

    if (!title) {
        alert("Please enter a task.");
        return;
    }

    const response = await fetch("/api/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ title: title })
    });

    if (response.ok) {
        taskInput.value = "";
        fetchTasks();
    } else {
        const error = await response.json();
        alert(error.error || "Failed to add task");
    }
}

async function toggleTask(taskId) {
    const response = await fetch(`/api/tasks/${taskId}`, {
        method: "PUT"
    });

    if (response.ok) {
        fetchTasks();
    }
}

async function deleteTask(taskId) {
    const response = await fetch(`/api/tasks/${taskId}`, {
        method: "DELETE"
    });

    if (response.ok) {
        fetchTasks();
    }
}

addTaskBtn.addEventListener("click", addTask);

taskInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        addTask();
    }
});

fetchTasks();