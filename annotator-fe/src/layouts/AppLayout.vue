<template>
  <v-layout>
    <v-app-bar color="primary" dark app>
      <v-btn to="/home"> Home </v-btn>
      <v-spacer></v-spacer>
      <v-btn to="/login"> Logout </v-btn>
    </v-app-bar>
    <RouterView />
  </v-layout>
</template>

<script setup lang="ts">
import { RouterView } from "vue-router";
</script>
