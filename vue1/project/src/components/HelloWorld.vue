<template>
  <div class="hello">
    <h3>create the following diagram in your language</h3>
    <img alt="intro image" :src="'/intro.svg'" width="1300">
    <div class="content">
      <table>
        <tr>
          <td>x label</td>
          <td><input type="text" name="xlabel"></td>
        </tr>
        <tr>
          <td>y label</td>
          <td><input type="text" name="ylabel"></td>
        </tr>
        <tr>
          <td>z label</td>
          <td><input type="text" name="zlabel"></td>
        </tr>
        <tr>
          <td></td>
          <td>
            <a href="#">create</a>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.content {
  margin-left: auto;
  margin-right: auto;
  width: fit-content;
}
</style>
