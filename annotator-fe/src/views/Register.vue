<template>
  <div class="ma-auto mt-6">
    <v-card min-width="500" class="pa-6">
      <v-text-field v-model.trim="name" label="Name"></v-text-field>
      <v-text-field v-model.trim="email" label="Email"></v-text-field>
      <v-text-field v-model.trim="password" label="Password"></v-text-field>
      <v-btn @click="submit">Register</v-btn>
    </v-card>
  </div>
</template>
<script lang="ts">
import { register } from "@/api/auth";
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const name = ref("");
    const email = ref("");
    const password = ref("");
    const submit = async () => {
      console.log(email.value);
      console.log(password.value);
      try {
        await register(name.value, email.value, password.value);
      } catch (error) {
        alert("Register Failed");
      }
    };
    return {
      name,
      email,
      password,
      submit,
    };
  },
});
</script>
