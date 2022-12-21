<template>
  <div class="ma-auto">
    <v-card min-width="500" class="pa-6">
      <v-text-field v-model.trim="email" label="Email"></v-text-field>
      <v-text-field
        type="password"
        v-model.trim="password"
        label="Password"
      ></v-text-field>
      <v-btn @click="submit">Login</v-btn>
    </v-card>
  </div>
</template>
<script lang="ts">
import { login } from "@/api/auth";
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  setup() {
    const router = useRouter();
    const email = ref("");
    const password = ref("");
    const submit = async () => {
      try {
        await login(email.value, password.value);
        router.push("/home");
      } catch (error) {
        alert("Login Failed");
      }
    };
    return {
      email,
      password,
      submit,
    };
  },
});
</script>
