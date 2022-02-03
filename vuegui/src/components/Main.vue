<template>
  <div class="hello">
    <h3>create the following diagram in your language</h3>
    <img alt="intro image" :src="'/initial.png'">
    <div class="content">
      <table>
        <tr>
          <td>x label</td>
          <td><input v-model="x_label" placeholder="x label"></td>
        </tr>
        <tr>
          <td>y label</td>
          <td><input v-model="y_label" placeholder="y label"></td>
        </tr>
        <tr>
          <td>z label</td>
          <td><input v-model="z_label" placeholder="z label"></td>
        </tr>
        <tr>
          <td></td>
          <td>
            <button @click="create()">create</button>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      x_label: 'Windgeschwindigkeit (km/h)',
      y_label: 'Gefühlte Temperaturdifferenz (C°)',
      z_label: 'Temperatur (°C)'
    }
  },
  methods: {
    create () {
      console.log(this.x_label)
      console.log(this.y_label)
      console.log(this.z_label)
      axios.post('/create', {
        x_label: this.x_label,
        y_label: this.y_label,
        z_label: this.z_label
      })
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
.content {
  margin-left: auto;
  margin-right: auto;
  width: fit-content;
}
</style>
