<template>
  <section>
    <div class="container">
      <div class="title">
        <h1>Welcome to the Task Manager application</h1>
        <h2>Let's create your first Task</h2>
      </div>
      <form>
        <div class="list-title input-row">
          <label>ToDo list title</label>
          <input type="text" placeholder="Home, School, etc.">
        </div>
        <div class="task-title input-row">
          <label>Task title</label>
          <input type="text" placeholder="Do groceries">
        </div>
        <div class="task-text input-row">
          <label>Task description</label>
          <textarea id="desc"></textarea>
        </div>
      </form>
      <div class="arrow-button-div">
        <button type="button" class="arrow-button" onclick="saveFirstTask()"><img src="../assets/arrow.svg" alt="arrow button"></button></div>
      </div>
  </section>
</template>

<script>
import axios from 'axios'

export default {
  name: 'WelcomePage',
  data: () => ({
    listTitle: '',
    taskTitle: '',
    taskDescription: ''
  }),
  methods: {
    saveFirstTask () {
      console.log('Poshlo')
      axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/create',
        data: {
          name: this.taskTitle,
          description: this.taskDescription
        }
      }).then((response) => {
        console.log(response.id)
        localStorage.setItem(this.listTitle, response.id)
        localStorage.setItem('isWelcomePageVisited', '1')
      })
    }
  }
}

</script>

<style>
.container {
  max-width: 680px;
  width: 50%;
  margin: 20vh auto;
}
.input-row {
  font-family: Roboto, sans-serif;
  font-size: 1.5rem;
  display: flex;
  justify-content: space-between;
  margin: 1em 0;
}
input, textarea {
  width: 60%;
}
textarea {
  height: 30vh;
  resize: none;
}
::-webkit-input-placeholder {
  font-style: italic;
}
:-moz-placeholder {
  font-style: italic;
}
::-moz-placeholder {
  font-style: italic;
}
:-ms-input-placeholder {
  font-style: italic;
}
.title {
  text-align: center;
  font-family: Montserrat, sans-serif;
}
h1 {
  color: #2D9CDB;
  font-size: 30px;
  font-weight: bold;
}
h2 {
  font-weight: lighter;
  font-size: 1.5rem;
}
.arrow-button-div {
  display: flex;
  justify-content: right;
  width: 82px;
  margin: 0 0 0 auto;
}
.arrow-button {
  background: none;
  border: none;
}
</style>
