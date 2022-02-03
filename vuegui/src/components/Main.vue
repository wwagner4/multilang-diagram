<template>
  <div>
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
    <h3>created diagram</h3>
    <img style="width: 800px" alt="created diagram" :src="this.diagram_url">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      x_label: 'Windgeschwindigkeit (km/h)',
      y_label: 'Gefühlte Temperaturdifferenz (°C)',
      z_label: 'Temperatur (°C)',
      diagram_url: '/diagram.svg'
    }
  },
  methods: {
    create () {
      const self = this
      const data = {
        x_label: this.x_label,
        y_label: this.y_label,
        z_label: this.z_label
      }
      console.log('sending: ' + JSON.stringify(data))
      axios.post('/create', data)
        .then(function (response) {
          console.log('received new diagram: ' + response.data)
          self.diagram_url = '/' + response.data
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
