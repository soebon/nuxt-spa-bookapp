<template>
  <div>
    <v-app-bar app>
      <v-toolbar-title>{{ title }}</v-toolbar-title>
      <v-spacer />
    </v-app-bar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: false,
      title: 'BookApp',
    };
  },
};
</script>

<style></style>
