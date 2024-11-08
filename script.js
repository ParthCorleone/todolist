function addTask() {
    const taskInput = document.getElementById("taskInput");
    const taskList = document.getElementById("taskList");
  
    if (taskInput.value.trim() === "") {
      alert("Please enter a task.");
      return;
    }
  
    const taskItem = document.createElement("li");
    taskItem.innerText = taskInput.value;
  
    const removeButton = document.createElement("span");
    removeButton.innerText = "×";
    removeButton.classList.add("remove-button");
    removeButton.onclick = () => taskItem.remove();
  
    taskItem.appendChild(removeButton);
    taskList.appendChild(taskItem);
  
    taskInput.value = "";
  }
  