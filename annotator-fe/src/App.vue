<script lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";
import AppLayout from "./layouts/AppLayout.vue";
import AuthLayout from "./layouts/AuthLayout.vue";
import { defineComponent } from "vue";

export default defineComponent({
  components: {
    AppLayout,
    AuthLayout
  },
  setup() {
    const route = useRoute();
    const layout = computed(() => {
      if (route.meta.layout) {
        return route.meta.layout;
      }
      return "AppLayout";
    });
    return {
      layout,
    }
  },
});
</script>

<template>
  <div>
    <component :is="layout"> </component>
  </div>

  <!-- <RouterView /> -->
</template>

<style scoped></style>
