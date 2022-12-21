<template>
  <div class="mt-16 pa-8 w-100">
    <div class="d-flex w-100">
      <span class="text-h5">Projects</span> <v-spacer></v-spacer>
      <v-btn @click="create">Create</v-btn>
    </div>
    <ol>
      <li
        class="pointer"
        @click="$router.push(`/project/${project.id}`)"
        v-for="project in projects"
        :key="project.id"
      >
        {{ project.name }}
      </li>
    </ol>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import type { Ref } from "vue";
import { createProject, listProjects } from "@/api/projects";

export default defineComponent({
  setup() {
    const projects: Ref<Array<any>> = ref([]);
    const fetchProjects = async () => {
      try {
        const res = await listProjects();
        projects.value = res.data.projects;
      } catch (error) {
        alert("Error occured!");
      }
    };

    const create = async () => {
      let name = prompt("Please enter project name", "");
      if (name != null) {
        await createProject(name as string);
        await fetchProjects();
      }
    };

    onMounted(async () => {
      await fetchProjects();
    });

    return { projects, create };
  },
});
</script>
